"""The [`WikiPage`][esperantilo.wiki.WikiPage] class.

Re-exported by [`esperantilo.wiki`][esperantilo.wiki], whose docstring describes
the feature as a whole; this module holds only the class itself.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterator, List, Optional, Sequence

from esperantilo.wiki import _wiki_api

# Public API of this module.
__all__ = ["WikiPage"]


@dataclass(repr=False)
class WikiPage:
    """One Wikipedia article, in one language, as plain text.

    Build one with [`look_up`][esperantilo.wiki.WikiPage.look_up]. The
    constructor is plain enough to call directly in tests.

    The body is split into sections, keyed by heading, in the order the article
    presents them. Only top-level headings (`== … ==`) open a new section;
    deeper ones stay inside the text of the section they belong to, so nothing
    is lost and `full_text()` gives back the article as it was fetched.

    Wikipedia leaves the lead — the text before the first heading — untitled,
    so it is keyed by the title of the article itself.

    Args:
        title: The title of the article, after any redirect was followed.
        language: The language code of the wiki it came from, such as `"eo"`.
        qid: The Wikidata identifier of the concept, such as `"Q143"`.
        url: The canonical address of the article.
        sections: The body, mapping each heading to its text, with the lead
            under the title of the article.

    Examples:
        >>> page = WikiPage(
        ...     title="Esperanto",
        ...     language="eo",
        ...     qid="Q143",
        ...     url="https://eo.wikipedia.org/wiki/Esperanto",
        ...     sections={
        ...         "Esperanto": "Esperanto estas planlingvo.",
        ...         "Historio": "Zamenhof publikigis ĝin en 1887.",
        ...     },
        ... )
        >>> page.section_names
        ['Esperanto', 'Historio']
        >>> page.section("historio")
        'Zamenhof publikigis ĝin en 1887.'
    """

    title: str
    language: str
    qid: str
    url: str
    sections: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def look_up(
            cls,
            title: str,
            language: str = "en",
            fallback_languages: Sequence[str] = ("es", "en", "eo"),
            any_language: bool = True,
            timeout: Optional[float] = 10.0,
    ) -> WikiPage:
        """Fetch the article a title refers to.

        The title is looked for in `language` first and then in each of
        `fallback_languages`, stopping at the first wiki that knows it;
        redirects are followed. The article that comes back is the one for the
        *concept* found, in `language` if that wiki has it and in the first
        fallback that does otherwise — which is what makes searching in one
        language and reading in another a single call.

        If no listed language knows the title and `any_language` is set, the
        concept is searched for across every language. That step is a *search*,
        not a lookup: it finds something for almost any plausible word, and what
        it finds is not necessarily what was asked for. Pass
        `any_language=False` to fail instead of guessing.

        Args:
            title: The title of the Wikipedia page.
            language: The language to get the page in. Default is `"en"`.
            fallback_languages: Languages to fall back on, both when searching
                for the title and when choosing which article to return.
            any_language: If True, search across all languages when no listed
                language knows the title.
            timeout: Seconds to wait for each request, or None to wait forever.
                Default is 10.0 seconds.

        Returns:
            The article, in the first available language of the preference list.

        Raises:
            ValueError: If the title is not found in any of the specified
                languages, or if the concept has no article in any of them.
            requests.RequestException: If a request fails, times out, or the
                API answers with an error status.

        Example:
            ```python
            page = WikiPage.look_up("Perejil", language="eo")
            print(page.title)   # Petroselo
            ```
        """
        return cls(*_wiki_api._fetch_by_title(
            title, language, fallback_languages, any_language, timeout
        ))

    @property
    def section_names(self) -> List[str]:
        """The headings of the article, in the order they appear."""
        return list(self.sections)

    def section(self, name: str) -> str:
        """Return the text of one section.

        The name is matched ignoring case and surrounding whitespace: a heading
        is prose written by an editor, and its exact capitalisation is not
        something the caller should have to know.

        Args:
            name: The heading to look for.

        Returns:
            The text of that section, without its heading.

        Raises:
            KeyError: If the article has no such section.
        """
        wanted = name.strip().casefold()
        for key, body in self.sections.items():
            if key.strip().casefold() == wanted:
                return body
        raise KeyError(f"No section {name!r}. Available: {self.section_names}")

    def full_text(self) -> str:
        """Return the whole article as one string, headings included.

        Examples:
            >>> page = WikiPage("Esperanto", "eo", "Q143", "", {"Historio": "En 1887."})
            >>> print(page.full_text())
            == Historio ==
            En 1887.
        """
        return "\n\n".join(
            f"== {name} ==\n{body}" for name, body in self.sections.items()
        )

    def __len__(self) -> int:
        """The number of sections — *not* the length of the text.

        Examples:
            >>> len(WikiPage("Esperanto", "eo", "Q143", "", {"Historio": "En 1887."}))
            1
        """
        return len(self.sections)

    def __getitem__(self, key: str) -> str:
        """Read a section, as `page["Historio"]`.

        Delegates to [`section`][esperantilo.wiki.WikiPage.section], so both
        ways of reading a section match names the same way.
        """
        return self.section(key)

    def __contains__(self, key: str) -> bool:
        """Test for a section, as `"Historio" in page`, ignoring case.

        Examples:
            >>> "HISTORIO" in WikiPage("Esperanto", "eo", "Q143", "", {"Historio": "."})
            True
        """
        try:
            self.section(key)
        except KeyError:
            return False
        return True

    def __iter__(self) -> Iterator[str]:
        """Iterate over the section names, as a mapping would."""
        return iter(self.sections)

    def __str__(self) -> str:
        """The article as plain text — the same as `full_text()`."""
        return self.full_text()

    def __repr__(self) -> str:
        """A one-line summary.

        The repr a dataclass generates would dump every section, which is the
        whole article: unusable in a REPL or a notebook, which is exactly where
        a page is most often looked at.

        Examples:
            >>> WikiPage("Esperanto", "eo", "Q143", "", {"Historio": "En 1887."})
            WikiPage(title='Esperanto', language='eo', qid='Q143', sections=1)
        """
        return (
            f"WikiPage(title={self.title!r}, language={self.language!r}, "
            f"qid={self.qid!r}, sections={len(self.sections)})"
        )
