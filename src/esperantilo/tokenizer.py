"""Sentence segmentation: splitting a text into the sentences it is made of."""

from __future__ import annotations

from typing import Iterable

# Public API of this module.
__all__ = ["sentence_tokenizer"]


#: Characters that end a sentence unless the caller says otherwise. A tuple, so
#: it cannot be mutated by one caller and leak into the next.
_DEFAULT_END_OF_SENTENCE = (".", "!", "?")


def sentence_tokenizer(
    text: str,
    end_of_sentence: Iterable[str] = _DEFAULT_END_OF_SENTENCE,
) -> list[str]:
    """Split `text` into sentences.

    A sentence ends at one of the `end_of_sentence` characters, which stays with
    the sentence it closes.

    Args:
        text: The text to split.
        end_of_sentence: The characters that end a sentence. Defaults to
            `(".", "!", "?")`.

    Returns:
        The sentences found, each stripped of surrounding whitespace. Empty ones
        are dropped, so a text of only whitespace yields an empty list.

    Examples:
        >>> sentence_tokenizer("Mi lernas Esperanton. Ĉu vere? Jes!")
        ['Mi lernas Esperanton.', 'Ĉu vere?', 'Jes!']

    ToDo:
        - Do not split on a dot inside a token, like `3.14` or `esperanto.net`.
        - Do not split after a known abbreviation, like `Dr.` or `Mr.`.
    """
    sentences = [text]

    # Cut the text after every end-of-sentence character.
    for end_char in end_of_sentence:
        new_sentences = []

        # For each sentence in the input
        for sentence in sentences:

            # Separate by char
            sentence_separation = sentence.split(end_char)

            # Strip whitespace
            sentence_separation = [s.strip() for s in sentence_separation]

            # Add the end-of-sentence character back to all but the last piece.
            # The last piece is whatever followed the final character
            sentence_separation = [
                s + end_char for s in sentence_separation[:-1]
            ] + sentence_separation[-1:]

            # Remove empty sentences
            sentence_separation = [s for s in sentence_separation if s]

            # Store the sentences found
            new_sentences.extend(sentence_separation)

        # Convert the list of sentences found into the input for the next iteration
        sentences = new_sentences

    return sentences
