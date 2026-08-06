"""MkDocs hook that renders the word lists of `resources/` as documentation pages.

Every JSON file in `resources/` that follows the schema described in
`resources/README.md` becomes a page under *Esperanto → Word lists*, plus an
index page listing all of them. Dropping a new file there — say
`prepozicioj.json` — is enough for a new page to appear: no page has to be
written by hand and no navigation entry has to be added.

The hook also copies each JSON file into the built site, so that the list can be
downloaded from the documentation itself.
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

#: Directory holding the source data, relative to the repository root.
RESOURCES_DIR = Path(__file__).resolve().parent.parent / "resources"

#: Where the generated pages live inside the documentation tree. They are part
#: of the *guide*: linguistic reference data, not library behaviour.
OUTPUT_DIR = "guide/esperanto/word-lists"

#: Title of the generated section in the navigation.
SECTION_TITLE = "Word lists"

#: Navigation section the generated section is appended to. It is nested (under
#: "Guide"), so it is looked up recursively — see `_find_section`.
PARENT_SECTION = "Esperanto"

#: Repository used to build "view the source file" links.
REPOSITORY_BLOB_URL = (
    "https://github.com/jparisu/nlp-esperantilo/blob/main/resources"
)

#: Locale the generated pages fall back to when a field or string is missing.
FALLBACK_LOCALE = "en"

#: User-interface strings of the generated pages, per locale. A locale missing
#: from here (or a key missing from a locale) falls back to `FALLBACK_LOCALE`.
STRINGS: dict[str, dict[str, str]] = {
    "en": {
        "index_title": "Word lists",
        "index_intro": (
            "Machine-readable word lists the library is built to consume"
            " directly. Each list lives as a JSON file under `resources/` in the"
            " repository, and each page below is generated from that file at"
            " build time — the documentation and the data can never disagree."
        ),
        "adding_title": "Adding a list",
        "adding_body": (
            "Drop a new JSON file in `resources/` following the schema"
            " documented in `resources/README.md`. A page for it appears here"
            " automatically, with no navigation entry to add."
        ),
        "empty": "No word list has been added yet.",
        "col_list": "List",
        "col_entries": "Entries",
        "col_file": "File",
        "open": "Open the list",
        "about_title": "About this list",
        "about_body": (
            "**{count} entries**, generated from [`resources/{filename}`]({url})."
            " The page and the file cannot drift apart: the table below *is* the"
            " file."
        ),
        "download": "Download",
        "sources": "Sources",
        "words": "Words",
        "col_word": "Word",
        "col_translation": "English",
        "col_notes": "Notes",
        "col_source": "Source",
        "usage": "Using this list from the library",
    },
    "es": {
        "index_title": "Listas de palabras",
        "index_intro": (
            "Listas de palabras legibles por máquina que la biblioteca está"
            " pensada para consumir directamente. Cada lista vive como un"
            " archivo JSON bajo `resources/` en el repositorio, y cada página de"
            " abajo se genera a partir de ese archivo en tiempo de construcción"
            " — la documentación y los datos nunca pueden discrepar."
        ),
        "adding_title": "Añadir una lista",
        "adding_body": (
            "Deja un nuevo archivo JSON en `resources/` siguiendo el esquema"
            " documentado en `resources/README.md`. Su página aparece aquí"
            " automáticamente, sin ninguna entrada de navegación que añadir."
        ),
        "empty": "Todavía no se ha añadido ninguna lista de palabras.",
        "col_list": "Lista",
        "col_entries": "Entradas",
        "col_file": "Archivo",
        "open": "Abrir la lista",
        "about_title": "Sobre esta lista",
        "about_body": (
            "**{count} entradas**, generadas a partir de"
            " [`resources/{filename}`]({url}). La página y el archivo no pueden"
            " separarse: la tabla de abajo *es* el archivo."
        ),
        "download": "Descargar",
        "sources": "Fuentes",
        "words": "Palabras",
        "col_word": "Palabra",
        "col_translation": "Inglés",
        "col_notes": "Notas",
        "col_source": "Fuente",
        "usage": "Usar esta lista desde la biblioteca",
    },
    "eo": {
        "index_title": "Vortlistoj",
        "index_intro": (
            "Maŝinlegeblaj vortlistoj, kiujn la biblioteko estas destinita legi"
            " rekte. Ĉiu listo vivas kiel JSON-dosiero sub `resources/` en la"
            " deponejo, kaj ĉiu paĝo sube estas generita el tiu dosiero"
            " konstrutempe — la dokumentaro kaj la datumoj neniam povas"
            " malkonsenti."
        ),
        "adding_title": "Aldoni liston",
        "adding_body": (
            "Metu novan JSON-dosieron en `resources/` laŭ la skemo dokumentita"
            " en `resources/README.md`. Paĝo por ĝi aperas ĉi tie aŭtomate, sen"
            " aldonenda navigada ero."
        ),
        "empty": "Ankoraŭ neniu vortlisto estas aldonita.",
        "col_list": "Listo",
        "col_entries": "Eroj",
        "col_file": "Dosiero",
        "open": "Malfermi la liston",
        "about_title": "Pri ĉi tiu listo",
        "about_body": (
            "**{count} eroj**, generitaj el [`resources/{filename}`]({url})."
            " La paĝo kaj la dosiero ne povas disiĝi: la tabelo sube *estas* la"
            " dosiero."
        ),
        "download": "Elŝuti",
        "sources": "Fontoj",
        "words": "Vortoj",
        "col_word": "Vorto",
        "col_translation": "Angla",
        "col_notes": "Notoj",
        "col_source": "Fonto",
        "usage": "Uzi ĉi tiun liston el la biblioteko",
    },
}


def _string(key: str, locale: str) -> str:
    """Look a user-interface string up, falling back to `FALLBACK_LOCALE`."""
    table = STRINGS.get(locale, {})
    if key in table:
        return table[key]
    return STRINGS[FALLBACK_LOCALE][key]


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #

def _load_lists() -> list[dict[str, Any]]:
    """Read and validate every word list in `resources/`."""
    if not RESOURCES_DIR.is_dir():
        log.warning("word_lists: no resources directory at %s", RESOURCES_DIR)
        return []

    lists: list[dict[str, Any]] = []
    for path in sorted(RESOURCES_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise PluginError(f"{path.name} is not valid JSON: {error}") from error

        for field in ("id", "titolo", "vortoj"):
            if field not in data:
                raise PluginError(f"{path.name} is missing the '{field}' field")

        data["_filename"] = path.name
        lists.append(data)

    return lists


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #

def _translated(value: Any, locale: str, default: str = "") -> str:
    """Pick `locale` out of a translatable field, falling back to English.

    Translatable fields are objects keyed by locale (see `resources/README.md`).
    A plain string is returned as-is, so a list that declares no translations
    still renders.
    """
    if isinstance(value, str):
        return value
    if not isinstance(value, dict):
        return default
    return (
        value.get(locale)
        or value.get(FALLBACK_LOCALE)
        or next(iter(value.values()), default)
    )


def _title(data: dict[str, Any], locale: str) -> str:
    return _translated(data["titolo"], locale)


def _description(data: dict[str, Any], locale: str) -> str:
    return _translated(data.get("priskribo", ""), locale)


def _category_label(data: dict[str, Any], key: str, locale: str) -> str:
    """Heading for one grammatical category.

    The keys of `kategorioj` are already words of the list's own language, so on
    that language's site they are shown bare; every other locale gets the
    translated gloss appended.
    """
    if locale == data.get("lingvo"):
        return key.capitalize()
    label = _translated(data.get("kategorioj", {}).get(key, {}), locale)
    return f"{key.capitalize()} — {label}" if label else key.capitalize()


def _escape(text: str) -> str:
    """Escape the characters that would break a Markdown table cell."""
    return text.replace("|", "\\|")


def _render_list_page(data: dict[str, Any], locale: str) -> str:
    words = data["vortoj"]
    sources = {source["id"]: source for source in data.get("fontoj", [])}
    filename = data["_filename"]

    lines = [
        f"# {_title(data, locale)}",
        "",
        _description(data, locale),
        "",
        f"!!! info \"{_string('about_title', locale)}\"",
        "    "
        + _string("about_body", locale).format(
            count=len(words),
            filename=filename,
            url=f"{REPOSITORY_BLOB_URL}/{filename}",
        ),
        "",
        f"    {_string('download', locale)}: [`{filename}`](./{filename})",
        "",
    ]

    if sources:
        lines += [f"## {_string('sources', locale)}", ""]
        for source in sources.values():
            note = f" — {source['noto']}" if source.get("noto") else ""
            licence = f" ({source['licenco']})" if source.get("licenco") else ""
            lines.append(
                f"- [{source['nomo']}]({source['url']}){licence}{note}"
                if source.get("url")
                else f"- {source['nomo']}{licence}{note}"
            )
        lines.append("")

    # Group by category, keeping the order declared in the file.
    declared = list(data.get("kategorioj", {}))
    present = {word.get("kategorio", "alia") for word in words}
    ordered = [key for key in declared if key in present]
    ordered += sorted(present - set(declared))

    header = " | ".join(
        _string(key, locale)
        for key in ("col_word", "col_translation", "col_notes", "col_source")
    )

    lines += [f"## {_string('words', locale)}", ""]
    for category in ordered:
        rows = [word for word in words if word.get("kategorio", "alia") == category]
        lines += [
            f"### {_category_label(data, category, locale)}",
            "",
            f"| {header} |",
            "| --- | --- | --- | --- |",
        ]
        for word in sorted(rows, key=lambda item: item["vorto"]):
            translations = word.get("traduko", {}).get("en", [])
            origin = ", ".join(
                sources.get(key, {}).get("nomo", key) for key in word.get("fontoj", [])
            )
            lines.append(
                f"| `{word['vorto']}` "
                f"| {_escape(', '.join(translations))} "
                f"| {_escape(word.get('noto', ''))} "
                f"| {_escape(origin)} |"
            )
        lines.append("")

    lines += [
        f"## {_string('usage', locale)}",
        "",
        "```python",
        "import json",
        "from pathlib import Path",
        "",
        f"data = json.loads(Path(\"resources/{filename}\").read_text(encoding=\"utf-8\"))",
        "words = {entry[\"vorto\"] for entry in data[\"vortoj\"]}",
        "```",
        "",
    ]

    return "\n".join(lines)


def _render_index_page(lists: list[dict[str, Any]], locale: str) -> str:
    lines = [
        f"# {_string('index_title', locale)}",
        "",
        _string("index_intro", locale),
        "",
        f"!!! tip \"{_string('adding_title', locale)}\"",
        f"    {_string('adding_body', locale)}",
        "",
    ]

    if not lists:
        lines += [_string("empty", locale), ""]
        return "\n".join(lines)

    header = " | ".join(
        _string(key, locale) for key in ("col_list", "col_entries", "col_file")
    )
    lines += [f"| {header} |", "| --- | --- | --- |"]
    for data in lists:
        lines.append(
            f"| [{_title(data, locale)}]({data['id']}.md) "
            f"| {len(data['vortoj'])} "
            f"| `resources/{data['_filename']}` |"
        )
    lines.append("")

    for data in lists:
        lines += [
            f"## {_title(data, locale)}",
            "",
            _description(data, locale),
            "",
            f"[{_string('open', locale)}]({data['id']}.md){{ .md-button }}",
            "",
        ]

    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# MkDocs events
# --------------------------------------------------------------------------- #

def _find_section(nav: list[Any], title: str) -> list[Any] | None:
    """Find the children of the navigation section called `title`.

    The search is recursive because the navigation is a tree: `Esperanto` is not
    a top-level entry but a subsection of `Guide`. Returns the list of children
    so the caller can append to it, or `None` if no such section exists.
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
    lists = _load_lists()
    if not config.nav:
        return config

    entries: list[Any] = [f"{OUTPUT_DIR}/index.md"]
    entries += [f"{OUTPUT_DIR}/{data['id']}.md" for data in lists]
    section = {SECTION_TITLE: entries}

    parent = _find_section(config.nav, PARENT_SECTION)
    if parent is None:
        # Better a section in the wrong place than pages with no navigation
        # entry at all, which `mkdocs build --strict` rejects.
        log.warning(
            "word_lists: no '%s' section in the navigation, "
            "appending '%s' at the top level",
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


def _current_locale(config) -> str:
    """Locale the generated pages should be written in.

    The pages produced here bypass mkdocs-static-i18n (they never exist on
    disk), so the locale has to be read off the plugin by hand. Without the
    plugin there is a single build, in the fallback locale.
    """
    current, _ = _languages(config)
    return current or FALLBACK_LOCALE


def _locale_prefix(config) -> str:
    """Sub-directory the current mkdocs-static-i18n build writes into.

    The plugin builds the site once per language, the default one at the root
    and the others under `<locale>/`. Files added here bypass the plugin, so
    their destination has to be prefixed by hand.
    """
    current, default = _languages(config)
    return f"{current}/" if current and current != default else ""


def _add(files, config, file: File) -> None:
    prefix = _locale_prefix(config)
    if prefix:
        file.dest_uri = prefix + file.dest_uri
    files.append(file)


@event_priority(-100)
def on_files(files, config):
    """Generate one page per word list, plus an index and the raw JSON files."""
    lists = _load_lists()
    locale = _current_locale(config)

    generated = {
        f"{OUTPUT_DIR}/index.md": _render_index_page(lists, locale),
    }
    for data in lists:
        generated[f"{OUTPUT_DIR}/{data['id']}.md"] = _render_list_page(data, locale)

    for src_uri, content in generated.items():
        if files.get_file_from_path(src_uri) is not None:
            continue
        _add(files, config, File.generated(config, src_uri, content=content))

    # Make the raw data downloadable from the documentation itself.
    for data in lists:
        src_uri = f"{OUTPUT_DIR}/{data['_filename']}"
        if files.get_file_from_path(src_uri) is not None:
            continue
        _add(
            files,
            config,
            File.generated(config, src_uri, abs_src_path=str(RESOURCES_DIR / data["_filename"])),
        )

    log.info("word_lists: generated %d word list page(s)", len(lists))
    return files
