"""MkDocs hook rendering the word lists of `resources/esperanto/` as doc pages.

There are two data files, and no word is written twice:

* `resources/esperanto/vortoj.json` — the **lexicon**: every word once, with its
  category, its English translation and a note.
* `resources/esperanto/listoj.json` — the **lists**: a title, a description and
  a filter over the lexicon. A word that is both a preposition and a stop-word
  is stored once and shown by both lists.

Adding a list means adding one entry to `listoj.json`; its page and its
navigation entry appear on the next build.

The generated pages are **English only**. They carry a banner saying so, and the
language switcher on them stays on the same page instead of wandering off (see
`on_page_context`).
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority
from mkdocs.structure.files import File

log = logging.getLogger("mkdocs.hooks.word_lists")

#: Directory holding the source data. This file lives in `docs/hooks/`, so the
#: repository root is two levels up.
RESOURCES_DIR = Path(__file__).resolve().parents[2] / "resources" / "esperanto"

#: The lexicon and the list definitions.
LEXICON_FILE = "vortoj.json"
LISTS_FILE = "listoj.json"

#: Where the generated pages live inside the documentation tree.
OUTPUT_DIR = "guide/esperanto/word-lists"

#: Title of the generated section in the navigation.
SECTION_TITLE = "Word lists"

#: Navigation section the generated section is appended to. It is nested (under
#: "Guide"), so it is looked up recursively — see `_find_section`.
PARENT_SECTION = "Esperanto"

#: Repository used to build "view the source file" links.
REPOSITORY_BLOB_URL = (
    "https://github.com/jparisu/nlp-esperantilo/blob/main/resources/esperanto"
)

#: Shown on every generated page: the data is not translated.
ENGLISH_ONLY = (
    '!!! warning "English only"\n'
    "    These pages are generated from the data files, which carry English\n"
    "    translations only. They are not translated into the other languages of\n"
    "    this site."
)


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #

def _read(filename: str) -> Any:
    path = RESOURCES_DIR / filename
    if not path.is_file():
        raise PluginError(f"word_lists: missing {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise PluginError(f"{filename} is not valid JSON: {error}") from error


def _load() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Read the lexicon and resolve every list's filter against it.

    Returns:
        The lexicon, and the lists with their matching words under `"vortoj"`.
    """
    lexicon = _read(LEXICON_FILE)
    for field in ("kategorioj", "vortoj"):
        if field not in lexicon:
            raise PluginError(f"{LEXICON_FILE} is missing the '{field}' field")

    lists = []
    for definition in _read(LISTS_FILE):
        for field in ("id", "titolo", "filtro"):
            if field not in definition:
                raise PluginError(f"{LISTS_FILE}: a list is missing '{field}'")

        matching = [
            word
            for word in lexicon["vortoj"]
            if all(word.get(key) == value for key, value in definition["filtro"].items())
        ]
        if not matching:
            raise PluginError(
                f"{LISTS_FILE}: list '{definition['id']}' matches no word; "
                f"its filter is {definition['filtro']}"
            )

        lists.append({**definition, "vortoj": matching})

    return lexicon, lists


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #

def _escape(text: str) -> str:
    """Escape the characters that would break a Markdown table cell."""
    return text.replace("|", "\\|")


def _render_list_page(lexicon: dict[str, Any], data: dict[str, Any]) -> str:
    words = data["vortoj"]
    sources = {source["id"]: source for source in lexicon.get("fontoj", [])}
    categories = lexicon["kategorioj"]

    lines = [
        f"# {data['titolo']}",
        "",
        data.get("priskribo", ""),
        "",
        ENGLISH_ONLY,
        "",
        f'!!! info "About this list"',
        f"    **{len(words)} entries**, selected from"
        f" [`resources/{LEXICON_FILE}`]({REPOSITORY_BLOB_URL}/{LEXICON_FILE})"
        f" by the filter `{json.dumps(data['filtro'])}`. The page and the data"
        f" cannot drift apart: the table below *is* the file.",
        "",
        f"    Download the whole lexicon: [`{LEXICON_FILE}`](./{LEXICON_FILE})",
        "",
    ]

    # Group by category, keeping the order declared in the lexicon.
    present = {word.get("kategorio", "alia") for word in words}
    ordered = [key for key in categories if key in present]
    ordered += sorted(present - set(categories))

    lines += ["## Words", ""]
    for category in ordered:
        rows = [w for w in words if w.get("kategorio", "alia") == category]
        label = categories.get(category, category.capitalize())
        heading = f"{category.capitalize()} — {label}" if label else category.capitalize()
        lines += [
            f"### {heading}" if len(ordered) > 1 else "",
            "" if len(ordered) > 1 else "",
            "| Word | English | Notes | Source |",
            "| --- | --- | --- | --- |",
        ]
        for word in sorted(rows, key=lambda item: item["vorto"]):
            origin = ", ".join(
                sources.get(key, {}).get("nomo", key) for key in word.get("fontoj", [])
            )
            lines.append(
                f"| `{word['vorto']}` "
                f"| {_escape(', '.join(word.get('traduko', [])))} "
                f"| {_escape(word.get('noto', ''))} "
                f"| {_escape(origin)} |"
            )
        lines.append("")

    if sources:
        lines += ["## Sources", ""]
        for source in sources.values():
            note = f" — {source['noto']}" if source.get("noto") else ""
            licence = f" ({source['licenco']})" if source.get("licenco") else ""
            lines.append(
                f"- [{source['nomo']}]({source['url']}){licence}{note}"
                if source.get("url")
                else f"- {source['nomo']}{licence}{note}"
            )
        lines.append("")

    return "\n".join(lines)


def _render_index_page(lists: list[dict[str, Any]]) -> str:
    lines = [
        "# Word lists",
        "",
        "Machine-readable word lists the library is built to consume directly."
        " Every word lives once in"
        f" [`resources/{LEXICON_FILE}`]({REPOSITORY_BLOB_URL}/{LEXICON_FILE});"
        " each list below is a filter over it, so a word that belongs to two"
        " lists is still stored once.",
        "",
        ENGLISH_ONLY,
        "",
        '!!! tip "Adding a list"',
        f"    Add an entry to `resources/{LISTS_FILE}` with an `id`, a `titolo`,"
        " a `priskribo` and a `filtro`. Its page appears here automatically,"
        " with no navigation entry to add.",
        "",
        "| List | Entries | Filter |",
        "| --- | --- | --- |",
    ]
    for data in lists:
        lines.append(
            f"| [{data['titolo']}]({data['id']}.md) "
            f"| {len(data['vortoj'])} "
            f"| `{json.dumps(data['filtro'])}` |"
        )
    lines.append("")

    lines += [
        "",
        "## Reading a list from Python",
        "",
        "```python",
        "import json",
        "from pathlib import Path",
        "",
        f'lexicon = json.loads(Path("resources/{LEXICON_FILE}").read_text(encoding="utf-8"))',
        "",
        "# The same filter the pages above apply.",
        'prepositions = {w["vorto"] for w in lexicon["vortoj"]'
        ' if w["kategorio"] == "prepozicio"}',
        "```",
        "",
    ]

    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# MkDocs events
# --------------------------------------------------------------------------- #

def _find_section(nav: list[Any], title: str) -> list[Any] | None:
    """Find the children of the navigation section called `title`.

    The search is recursive because the navigation is a tree: `Esperanto` is not
    a top-level entry but a subsection of `Guide`.
    """
    for item in nav:
        if not isinstance(item, dict):
            continue
        for key, children in item.items():
            if not isinstance(children, list):
                continue
            if key == title:
                return children
            found = _find_section(children, title)
            if found is not None:
                return found
    return None


# The low priority makes these handlers run *after* every plugin, in particular
# after mkdocs-static-i18n, which only knows how to deal with files that exist
# on disk inside docs_dir.
@event_priority(-100)
def on_config(config):
    """Append the generated section to the navigation of the parent section."""
    _, lists = _load()
    if not config.nav:
        return config

    entries: list[Any] = [f"{OUTPUT_DIR}/index.md"]
    entries += [f"{OUTPUT_DIR}/{data['id']}.md" for data in lists]
    section = {SECTION_TITLE: entries}

    parent = _find_section(config.nav, PARENT_SECTION)
    if parent is None:
        log.warning(
            "word_lists: no '%s' section in the navigation, appending '%s' at "
            "the top level",
            PARENT_SECTION,
            SECTION_TITLE,
        )
        config.nav.append(section)
    elif section not in parent:
        parent.append(section)

    return config


def _languages(config) -> tuple[str | None, str | None]:
    """Language mkdocs-static-i18n is currently building, and the default one."""
    plugin = config.plugins.get("i18n") if hasattr(config, "plugins") else None
    if plugin is None:
        return None, None
    return (
        getattr(plugin, "current_language", None),
        getattr(plugin, "default_language", None),
    )


def _locale_prefix(config) -> str:
    """Sub-directory the current mkdocs-static-i18n build writes into.

    The plugin builds the site once per language, the default one at the root
    and the others under `<locale>/`. Files added here bypass the plugin, so
    their destination has to be prefixed by hand.
    """
    current, default = _languages(config)
    return f"{current}/" if current and current != default else ""


class _Alternate:
    """The one attribute mkdocs-static-i18n reads off an alternate file.

    Its language switcher does `page.file.alternates[lang].url`. The generated
    pages have no real `File` in the other languages — they are produced once
    per build, after the plugin has run — so a stand-in carrying the URL is
    enough, and is what keeps the switcher on the current page.
    """

    def __init__(self, url: str) -> None:
        self.url = url


def _teach_i18n_about(file: File, config) -> None:
    """Give a generated file the attributes the language switcher needs.

    Without them the plugin skips the file (it checks `hasattr(file, "locale")`)
    and leaves the switcher pointing at whatever page it handled last — which is
    how these pages used to send readers to an unrelated one.

    Every language builds the same page at the same relative path, so the
    alternate URL of a language is just its prefix plus that path.
    """
    current, default = _languages(config)
    if current is None:
        return

    # `guide/…/prepozicioj.md` -> `guide/…/prepozicioj/`, `…/index.md` -> `…/`
    path = file.src_uri[: -len(".md")]
    url = path.rsplit("/", 1)[0] + "/" if path.endswith("/index") else f"{path}/"

    file.locale = current
    file.locale_alternate_of = current
    file.alternates = {
        alternate["lang"]: _Alternate(
            f"{'' if alternate['lang'] == default else alternate['lang'] + '/'}{url}"
        )
        for alternate in config.extra.get("alternate", [])
    }


def _add(files, config, file: File) -> None:
    prefix = _locale_prefix(config)
    if prefix:
        file.dest_uri = prefix + file.dest_uri
    if file.src_uri.endswith(".md"):
        _teach_i18n_about(file, config)
    files.append(file)


@event_priority(-100)
def on_files(files, config):
    """Generate one page per list, plus an index and the raw lexicon."""
    lexicon, lists = _load()

    generated = {f"{OUTPUT_DIR}/index.md": _render_index_page(lists)}
    for data in lists:
        generated[f"{OUTPUT_DIR}/{data['id']}.md"] = _render_list_page(lexicon, data)

    for src_uri, content in generated.items():
        if files.get_file_from_path(src_uri) is not None:
            continue
        _add(files, config, File.generated(config, src_uri, content=content))

    # Make the raw data downloadable from the documentation itself.
    for filename in (LEXICON_FILE, LISTS_FILE):
        src_uri = f"{OUTPUT_DIR}/{filename}"
        if files.get_file_from_path(src_uri) is not None:
            continue
        _add(
            files,
            config,
            File.generated(
                config, src_uri, abs_src_path=str(RESOURCES_DIR / filename)
            ),
        )

    log.info("word_lists: generated %d word list page(s)", len(lists))
    return files
