"""Tests for `esperantilo.tokenizer.sentence_tokenizer`."""

import pytest

from esperantilo import sentence_tokenizer


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        pytest.param(
            "Mi lernas Esperanton. Ĝi estas facila.",
            ["Mi lernas Esperanton.", "Ĝi estas facila."],
            id="two-sentences",
        ),
        pytest.param("Unua. Dua. Tria.", ["Unua.", "Dua.", "Tria."], id="three"),
        pytest.param("Unu frazo.", ["Unu frazo."], id="one-sentence"),
        pytest.param("Sen punkto", ["Sen punkto"], id="no-terminator"),
        pytest.param("Unua.\nDua.", ["Unua.", "Dua."], id="line-break"),
        pytest.param("  Unua.   Dua.  ", ["Unua.", "Dua."], id="extra-whitespace"),
        pytest.param("Ĉu vere? Jes!", ["Ĉu vere?", "Jes!"], id="question-and-bang"),
    ],
)
def test_splits_on_an_end_of_sentence_character(text, expected):
    assert sentence_tokenizer(text) == expected


def test_a_sentence_survives_the_passes_of_the_other_terminators():
    """`Unua.` contains no `!` and no `?`, and must still come out intact."""
    assert sentence_tokenizer("Unua. Dua.") == ["Unua.", "Dua."]


def test_mixed_terminators_keep_their_order():
    """Each terminator is handled in its own pass; the order must not change."""
    assert sentence_tokenizer("Ĉu? Jes! Fino.") == ["Ĉu?", "Jes!", "Fino."]


def test_the_terminators_are_configurable():
    """With only `!` listed, the dot and the question mark stop being cuts."""
    text = "Unua. Dua! Tria?"
    assert sentence_tokenizer(text) == ["Unua.", "Dua!", "Tria?"]
    assert sentence_tokenizer(text, end_of_sentence=["!"]) == ["Unua. Dua!", "Tria?"]


@pytest.mark.parametrize(
    "text",
    [pytest.param("", id="empty"), pytest.param("  \n ", id="only-whitespace")],
)
def test_text_without_content_yields_no_sentence(text):
    assert sentence_tokenizer(text) == []


def test_no_sentence_is_empty_or_padded():
    for sentence in sentence_tokenizer("  Unua.  Dua!  Tria?  "):
        assert sentence and sentence == sentence.strip()


@pytest.mark.xfail(strict=True, reason="ToDo: dots inside a token and abbreviations")
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        pytest.param("Pi estas 3.14.", ["Pi estas 3.14."], id="decimal"),
        pytest.param("Vidu esperanto.net.", ["Vidu esperanto.net."], id="domain"),
        pytest.param("Dr. Zamenhof venis.", ["Dr. Zamenhof venis."], id="abbreviation"),
    ],
)
def test_known_limitations(text, expected):
    """The `ToDo` of the function, pinned down.

    `strict=True` means these turn into failures the day the ToDo is done, which
    is the reminder to delete this marker.
    """
    assert sentence_tokenizer(text) == expected
