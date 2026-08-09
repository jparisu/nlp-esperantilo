"""Validate the word data of `resources/` against the documented schema.

There are two files and they have different jobs:

* `esperanto/vortoj.json` is the lexicon — every word exactly once;
* `esperanto/listoj.json` defines the lists, each one a filter over that lexicon.

The documentation is generated from both, so a malformed edit must fail here
rather than in the middle of a documentation build.
"""

import json
from pathlib import Path

import pytest

RESOURCES = Path(__file__).resolve().parents[1] / "resources" / "esperanto"
LEXICON = json.loads((RESOURCES / "vortoj.json").read_text(encoding="utf-8"))
LISTS = json.loads((RESOURCES / "listoj.json").read_text(encoding="utf-8"))

WORDS = LEXICON["vortoj"]
CATEGORIES = LEXICON["kategorioj"]
SOURCES = {source["id"] for source in LEXICON["fontoj"]}


# --------------------------------------------------------------------------- #
# The lexicon
# --------------------------------------------------------------------------- #

def test_the_lexicon_has_its_mandatory_fields():
    for field in ("lingvo", "fontoj", "kategorioj", "vortoj"):
        assert field in LEXICON, f"missing '{field}'"
    assert WORDS, "the lexicon is empty"


def test_every_category_has_an_english_label():
    for key, label in CATEGORIES.items():
        assert isinstance(label, str) and label, f"'{key}' has no label"


@pytest.mark.parametrize("word", WORDS, ids=lambda w: w["vorto"])
def test_every_word_is_well_formed(word):
    vorto = word["vorto"]
    assert vorto == vorto.lower(), f"'{vorto}' is not lowercase"
    assert word["kategorio"] in CATEGORIES, f"'{vorto}' has an unknown category"
    assert isinstance(word["traduko"], list) and word["traduko"], (
        f"'{vorto}' has no translation"
    )
    assert isinstance(word["ignorinda"], bool), f"'{vorto}' has no 'ignorinda' flag"
    for source in word.get("fontoj", []):
        assert source in SOURCES, f"'{vorto}' references unknown source {source!r}"


def test_no_word_appears_twice():
    """The point of a single lexicon: a word belongs to many lists, but exists once."""
    seen = [word["vorto"] for word in WORDS]
    duplicates = {v for v in seen if seen.count(v) > 1}
    assert not duplicates, f"duplicated: {sorted(duplicates)}"


# --------------------------------------------------------------------------- #
# The lists
# --------------------------------------------------------------------------- #

def test_list_ids_are_unique():
    ids = [entry["id"] for entry in LISTS]
    assert len(ids) == len(set(ids)), f"duplicated ids in listoj.json: {ids}"


@pytest.mark.parametrize("definition", LISTS, ids=lambda d: d["id"])
def test_every_list_is_well_formed(definition):
    for field in ("id", "titolo", "priskribo", "filtro"):
        assert field in definition, f"missing '{field}'"
    assert definition["filtro"], "the filter is empty: it would match every word"


@pytest.mark.parametrize("definition", LISTS, ids=lambda d: d["id"])
def test_every_list_matches_at_least_one_word(definition):
    """A filter that matches nothing means a typo, and would build an empty page."""
    matching = [
        word
        for word in WORDS
        if all(word.get(k) == v for k, v in definition["filtro"].items())
    ]
    assert matching, f"'{definition['id']}' matches no word"


@pytest.mark.parametrize("definition", LISTS, ids=lambda d: d["id"])
def test_every_filter_uses_a_real_field(definition):
    fields = {key for word in WORDS for key in word}
    unknown = set(definition["filtro"]) - fields
    assert not unknown, f"'{definition['id']}' filters on unknown field(s) {unknown}"
