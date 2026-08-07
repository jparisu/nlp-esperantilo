"""Internal client for the MediaWiki and Wikidata web APIs.

Not part of the public API. Nothing here is exported by `esperantilo`, nothing
here appears in the API reference, and every name is prefixed with `_`: this is
the plumbing that [`WikiPage`][esperantilo.wiki.WikiPage] sits on, and it is
free to change without notice.

Why two APIs are involved
-------------------------

A Wikipedia article exists once per language, and the same *concept* is a
different page in each one: `Parsley`, `Perejil` and `Petroselo` are three
articles about one plant. What ties them together is the **QID**, the identifier
Wikidata gives to the concept itself — parsley is `Q26980`, in every language.

So a title is resolved in two steps: Wikipedia turns the title into a QID, and
Wikidata turns that QID into the article of whichever language was asked for.
That is what makes "search in Spanish, read in Esperanto" possible at all.

The fetch functions return the arguments of `WikiPage`, not a `WikiPage`, so
that this module never has to import the class it feeds — the public module
imports this one, and not the other way round.

Note:
    Every function that talks to the network can fail for reasons that have
    nothing to do with the title: no connection, a timeout, an API error. Those
    surface as `requests.RequestException`. `ValueError` is reserved for "the
    page is not there".
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple, Sequence

import requests

#: The arguments of `WikiPage`, in order: title, language, qid, url, sections.
#: Returned as a plain tuple so that this module stays independent of the class.
_Fetched = Tuple[str, str, str, str, Dict[str, str]]

#: The API entry point of Wikidata, where QIDs and cross-language links live.
_WIKIDATA_API = "https://www.wikidata.org/w/api.php"

#: Wikimedia asks every client to identify itself, and throttles the ones that
#: do not.
_USER_AGENT = "esperantilo (https://github.com/jparisu/nlp-esperantilo)"

#: A plain-text heading, as `prop=extracts` renders it: `== Historio ==`, with
#: two to six `=` on each side marking how deeply the section is nested.
_HEADING = re.compile(r"^(={2,6})\s*(.+?)\s*\1$")


# --------------------------------------------------------------------------- #
# What the public class calls
# --------------------------------------------------------------------------- #

def _find_qid(
        title: str,
        language: str,
        fallback_languages: Sequence[str],
        any_language: bool,
        timeout: Optional[float],
) -> str:
    """Find the QID of the concept a Wikipedia title refers to.

    The title is looked up in `language` first and then in each of
    `fallback_languages`, stopping at the first wiki that knows it. Redirects
    are followed, so an alias such as `"Zamenhof"` resolves like its target.

    If no listed language knows the title and `any_language` is set, Wikidata
    itself is searched, which matches labels and aliases in every language and
    returns its best hit. That last step is a *search*, not a lookup: it finds
    something for almost any plausible word, and what it finds is not
    necessarily what was asked for.

    Raises:
        ValueError: If no listed language knows the title, or if it is known but
            has no Wikidata item.
    """
    preference = _language_preference(language, fallback_languages)

    for lang in preference:
        qid = _qid_from_title(title, lang, timeout)
        if qid is not None:
            return qid

    if any_language:
        qid = _qid_from_search(title, timeout)
        if qid is not None:
            return qid

    raise ValueError(f"No Wikipedia page titled {title!r} in {preference}")


def _fetch_by_title(
        title: str,
        language: str,
        fallback_languages: Sequence[str],
        any_language: bool,
        timeout: Optional[float],
) -> _Fetched:
    """Resolve a title to a concept, then read that concept's article.

    The language the title is *searched* in and the language the article is
    *read* in need not be the same: the title is looked for in `language` and
    the fallbacks, and the article comes back in `language` if that wiki has
    one, or in the first fallback that does.

    Raises:
        ValueError: If no listed language knows the title, or if the concept has
            no article in any of them.
    """
    preference = _language_preference(language, fallback_languages)
    qid = _find_qid(title, language, fallback_languages, any_language, timeout)

    # The concept exists, but not necessarily as an article in the language that
    # was asked for — a smaller wiki may simply not cover it.
    for lang in preference:
        try:
            return _fetch_by_qid(qid, lang, timeout)
        except ValueError:
            continue

    raise ValueError(f"{qid} ({title!r}) has no article in any of {preference}")


def _fetch_by_qid(
        qid: str,
        language: str,
        timeout: Optional[float],
) -> _Fetched:
    """Read the article a Wikidata concept has in one language.

    Raises:
        ValueError: If the QID does not exist, or has no article in `language`.
    """
    link = _sitelink(qid, language, timeout)
    if link is None:
        raise ValueError(f"{qid} has no {language!r} Wikipedia article")

    linked_title, url = link
    title, extract = _extract(linked_title, language, timeout)
    return title, language, qid, url, _split_sections(extract, title)


# --------------------------------------------------------------------------- #
# Talking to the APIs
# --------------------------------------------------------------------------- #

def _language_preference(
        language: str,
        fallback_languages: Sequence[str],
) -> List[str]:
    """The languages to try, in order, without repeats.

    `language` goes first, and the default fallback list already contains
    `"en"` — without this, the default arguments would query the English wiki
    twice.

    Examples:
        >>> _language_preference("en", ("es", "en", "eo"))
        ['en', 'es', 'eo']
    """
    return [lang for lang in dict.fromkeys((language, *fallback_languages)) if lang]


def _api_get(
        api_url: str,
        params: Dict[str, str],
        timeout: Optional[float],
) -> dict:
    """Call a MediaWiki API and return the decoded JSON response.

    `formatversion=2` is what keeps the responses readable: without it, page
    results come back as an object keyed by numeric page id, which every caller
    would have to walk around instead of simply iterating over.

    Raises:
        requests.RequestException: If the request fails, or the API answers with
            an error status.
    """
    response = requests.get(
        api_url,
        params={**params, "format": "json", "formatversion": "2"},
        headers={"User-Agent": _USER_AGENT},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def _qid_from_title(
        title: str,
        language: str,
        timeout: Optional[float],
) -> Optional[str]:
    """The QID of a title on one wiki, or None if that wiki does not have it."""
    data = _api_get(
        f"https://{language}.wikipedia.org/w/api.php",
        {
            "action": "query",
            "prop": "pageprops",
            "ppprop": "wikibase_item",
            "titles": title,
            "redirects": "1",
        },
        timeout,
    )
    for page in data.get("query", {}).get("pages", []):
        # A title the wiki does not have still comes back, flagged as missing.
        if page.get("missing") or page.get("invalid"):
            continue
        qid = page.get("pageprops", {}).get("wikibase_item")
        if qid:
            return qid
    return None


def _qid_from_search(title: str, timeout: Optional[float]) -> Optional[str]:
    """The best Wikidata hit for a title, searched across every language.

    Namespace 0 is where the items (`Q…`) live; restricting the search to it
    keeps properties and lexemes out of the results.
    """
    data = _api_get(
        _WIKIDATA_API,
        {
            "action": "query",
            "list": "search",
            "srsearch": title,
            "srnamespace": "0",
            "srlimit": "1",
        },
        timeout,
    )
    for hit in data.get("query", {}).get("search", []):
        # On Wikidata the page title of an item *is* its QID.
        return hit["title"]
    return None


def _sitelink(
        qid: str,
        language: str,
        timeout: Optional[float],
) -> Optional[Tuple[str, str]]:
    """The title and URL of the article a concept has on one wiki.

    Returns None if the concept does not exist, or if that wiki does not cover
    it.
    """
    # Wikidata names its links after the site, not the language: `eowiki`. The
    # few language codes that contain a dash use an underscore there.
    site = f"{language.replace('-', '_')}wiki"
    data = _api_get(
        _WIKIDATA_API,
        {
            "action": "wbgetentities",
            "ids": qid,
            "props": "sitelinks/urls",
            "sitefilter": site,
        },
        timeout,
    )

    entities = data.get("entities", {})
    # An item that has been merged into another answers under the target's id,
    # so fall back to whatever single entity came back rather than assume `qid`.
    entity = entities.get(qid)
    if entity is None and len(entities) == 1:
        entity = next(iter(entities.values()))
    if not entity or "missing" in entity:
        return None

    link = entity.get("sitelinks", {}).get(site)
    if not link:
        return None
    return link["title"], link.get("url", "")


def _extract(
        title: str,
        language: str,
        timeout: Optional[float],
) -> Tuple[str, str]:
    """The plain text of an article, together with the title it ended up on.

    `explaintext` is what strips the wiki markup, the infoboxes and the
    reference marks, leaving the prose plus its `== … ==` headings.

    Raises:
        ValueError: If the wiki does not have that article.
    """
    data = _api_get(
        f"https://{language}.wikipedia.org/w/api.php",
        {
            "action": "query",
            "prop": "extracts",
            "explaintext": "1",
            "titles": title,
            "redirects": "1",
        },
        timeout,
    )
    for page in data.get("query", {}).get("pages", []):
        if page.get("missing") or page.get("invalid"):
            continue
        return page.get("title", title), page.get("extract", "")
    raise ValueError(f"No {language!r} Wikipedia article titled {title!r}")


def _split_sections(extract: str, title: str) -> Dict[str, str]:
    """Split the plain text of an article into its sections.

    Only top-level headings open a section. Deeper ones are left inside the text
    of the section that contains them, which keeps the mapping flat without
    losing the nesting, and lets `WikiPage.full_text()` rebuild the article as
    it came in.

    Args:
        extract: The plain text of the article, headings included.
        title: The title of the article, used to key the untitled lead.

    Examples:
        >>> _split_sections("Lead.\\n\\n== Historio ==\\nEn 1887.", "Esperanto")
        {'Esperanto': 'Lead.', 'Historio': 'En 1887.'}
    """
    sections: Dict[str, str] = {}
    current = title
    body: List[str] = []

    def flush() -> None:
        """Store what has been read so far under the heading it belongs to."""
        text = "\n".join(body).strip()
        if not text:
            return
        # A heading repeated within one article — legal, if unusual — would
        # otherwise keep nothing but its last occurrence.
        if current in sections:
            sections[current] = f"{sections[current]}\n\n{text}"
        else:
            sections[current] = text

    for line in extract.splitlines():
        heading = _HEADING.match(line.strip())
        if heading is not None and len(heading.group(1)) == 2:
            flush()
            current = heading.group(2)
            body = []
        else:
            body.append(line)
    flush()

    return sections
