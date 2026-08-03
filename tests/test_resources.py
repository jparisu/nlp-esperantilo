"""Validate the word lists of `resources/` against the documented schema.

The documentation is generated from these files, so a malformed edit must fail
here rather than in the middle of a documentation build.
"""

import json
from pathlib import Path

import pytest

RESOURCES = Path(__file__).resolve().parents[1] / "resources"
FILES = sorted(RESOURCES.glob("*.json"))


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_resources_directory_is_not_empty():
    assert FILES, f"no word list found in {RESOURCES}"


@pytest.mark.parametrize("path", FILES, ids=lambda p: p.name)
def test_mandatory_fields(path: Path):
    data = _load(path)
    for field in ("id", "titolo", "vortoj"):
        assert field in data, f"missing '{field}'"
    assert data["id"] == path.stem, "'id' must match the file name"
    assert data["vortoj"], "the list is empty"


@pytest.mark.parametrize("path", FILES, ids=lambda p: p.name)
def test_entries_are_well_formed(path: Path):
    data = _load(path)
    categories = set(data.get("kategorioj", {}))
    sources = {source["id"] for source in data.get("fontoj", [])}

    seen = set()
    for entry in data["vortoj"]:
        word = entry.get("vorto")
        assert word, f"an entry has no 'vorto': {entry}"
        assert word == word.lower(), f"'{word}' is not lowercase"
        assert word not in seen, f"'{word}' is duplicated"
        seen.add(word)

        if categories:
            assert entry.get("kategorio") in categories, (
                f"'{word}' has an unknown category {entry.get('kategorio')!r}"
            )

        translations = entry.get("traduko", {})
        assert translations, f"'{word}' has no translation"
        for locale, values in translations.items():
            assert isinstance(values, list) and values, (
                f"'{word}' has an empty '{locale}' translation"
            )

        for source in entry.get("fontoj", []):
            assert source in sources, f"'{word}' references unknown source {source!r}"


@pytest.mark.parametrize("path", FILES, ids=lambda p: p.name)
def test_declared_translations_are_present(path: Path):
    data = _load(path)
    for locale in data.get("tradukoj", []):
        missing = [
            entry["vorto"]
            for entry in data["vortoj"]
            if locale not in entry.get("traduko", {})
        ]
        assert not missing, f"missing '{locale}' translation for: {missing[:10]}"
