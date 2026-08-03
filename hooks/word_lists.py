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

from mkdocs.plugins import event_priority
from mkdocs.structure.files import File

log = logging.getLogger("mkdocs.hooks.word_lists")

#: Directory holding the source data, relative to the repository root.
RESOURCES_DIR = Path(__file__).resolve().parent.parent / "resources"

#: Where the generated pages live inside the documentation tree.
OUTPUT_DIR = "esperanto/word-lists"

#: Title of the generated section in the navigation.
SECTION_TITLE = "Word lists"

#: Navigation section the generated section is appended to.
PARENT_SECTION = "Esperanto"

#: Repository used to build "view the source file" links.
REPOSITORY_BLOB_URL = (
    "https://github.com/jparisu/nlp-esperantilo/blob/main/resources"
)


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


class PluginError(Exception):
    """Raised on malformed input, which aborts the build."""


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #

def _title(data: dict[str, Any], locale: str = "en") -> str:
    titolo = data["titolo"]
    if isinstance(titolo, str):
        return titolo
    return titolo.get(locale) or next(iter(titolo.values()))


def _description(data: dict[str, Any], locale: str = "en") -> str:
    priskribo = data.get("priskribo", "")
    if isinstance(priskribo, str):
        return priskribo
    return priskribo.get(locale) or next(iter(priskribo.values()), "")


def _category_label(data: dict[str, Any], key: str) -> str:
    label = data.get("kategorioj", {}).get(key, {}).get("en")
    return f"{key.capitalize()} — {label}" if label else key.capitalize()


def _escape(text: str) -> str:
    """Escape the characters that would break a Markdown table cell."""
    return text.replace("|", "\\|")


def _render_list_page(data: dict[str, Any]) -> str:
    words = data["vortoj"]
    sources = {source["id"]: source for source in data.get("fontoj", [])}

    lines = [
        f"# {_title(data)}",
        "",
        _description(data),
        "",
        "!!! info \"About this list\"",
        f"    **{len(words)} entries**, generated from"
        f" [`resources/{data['_filename']}`]({REPOSITORY_BLOB_URL}/{data['_filename']})."
        f" The page and the file cannot drift apart: the table below *is* the file.",
        "",
        f"    Download: [`{data['_filename']}`](./{data['_filename']})",
        "",
    ]

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

    # Group by category, keeping the order declared in the file.
    declared = list(data.get("kategorioj", {}))
    present = {word.get("kategorio", "alia") for word in words}
    ordered = [key for key in declared if key in present]
    ordered += sorted(present - set(declared))

    lines += ["## Words", ""]
    for category in ordered:
        rows = [word for word in words if word.get("kategorio", "alia") == category]
        lines += [
            f"### {_category_label(data, category)}",
            "",
            "| Word | English | Notes | Source |",
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
        "## Using this list from the library",
        "",
        "```python",
        "import json",
        "from pathlib import Path",
        "",
        f"data = json.loads(Path(\"resources/{data['_filename']}\").read_text(encoding=\"utf-8\"))",
        "words = {entry[\"vorto\"] for entry in data[\"vortoj\"]}",
        "```",
        "",
    ]

    return "\n".join(lines)


def _render_index_page(lists: list[dict[str, Any]]) -> str:
    lines = [
        "# Word lists",
        "",
        "Machine-readable word lists that the library consumes directly. Each list",
        "lives as a JSON file under `resources/` in the repository, and each page",
        "below is generated from that file at build time — the documentation and the",
        "data can never disagree.",
        "",
        "!!! tip \"Adding a list\"",
        "    Drop a new JSON file in `resources/` following the schema documented in",
        "    `resources/README.md`. A page for it appears here automatically, with no",
        "    navigation entry to add.",
        "",
    ]

    if not lists:
        lines += ["No word list has been added yet.", ""]
        return "\n".join(lines)

    lines += ["| List | Entries | File |", "| --- | --- | --- |"]
    for data in lists:
        lines.append(
            f"| [{_title(data)}]({data['id']}.md) "
            f"| {len(data['vortoj'])} "
            f"| `resources/{data['_filename']}` |"
        )
    lines.append("")

    for data in lists:
        lines += [
            f"## {_title(data)}",
            "",
            _description(data),
            "",
            f"[Open the list]({data['id']}.md){{ .md-button }}",
            "",
        ]

    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# MkDocs events
# --------------------------------------------------------------------------- #

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

    for item in config.nav:
        if isinstance(item, dict) and PARENT_SECTION in item:
            children = item[PARENT_SECTION]
            if isinstance(children, list) and section not in children:
                children.append(section)
            break
    else:
        config.nav.append(section)

    return config


def _locale_prefix(config) -> str:
    """Sub-directory the current mkdocs-static-i18n build writes into.

    The plugin builds the site once per language, the default one at the root
    and the others under `<locale>/`. Files added here bypass the plugin, so
    their destination has to be prefixed by hand.
    """
    plugin = config.plugins.get("i18n") if hasattr(config, "plugins") else None
    if plugin is None:
        return ""
    current = getattr(plugin, "current_language", None)
    default = getattr(plugin, "default_language", None)
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

    generated = {
        f"{OUTPUT_DIR}/index.md": _render_index_page(lists),
    }
    for data in lists:
        generated[f"{OUTPUT_DIR}/{data['id']}.md"] = _render_list_page(data)

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
