# Sentence segmentation

Splitting a text into sentences is the first step of almost every NLP pipeline.
`esperantilo` does it with
[`sentence_tokenizer`](api.md#esperantilo.tokenizer.sentence_tokenizer).

```python
from esperantilo import sentence_tokenizer

sentence_tokenizer("Mi lernas Esperanton. Ĉu vere? Jes!")
# ['Mi lernas Esperanton.', 'Ĉu vere?', 'Jes!']
```

## The rule

A sentence ends at `.`, `!` or `?`. The character stays with the sentence it
closes, and surrounding whitespace is stripped. Empty sentences are dropped, so
a text of only whitespace gives `[]`.

Which characters end a sentence is an argument:

```python
sentence_tokenizer("Unua. Dua! Tria?", end_of_sentence=["!"])
# ['Unua. Dua!', 'Tria?']
```

## What it does not do

The tokenizer is deliberately naive — every terminator cuts, whatever surrounds
it:

| Input | Result |
| --- | --- |
| `"Pi estas 3.14."` | `['Pi estas 3.', '14.']` |
| `"Vidu esperanto.net."` | `['Vidu esperanto.', 'net.']` |
| `"Dr. Zamenhof venis."` | `['Dr.', 'Zamenhof venis.']` |

These are the `ToDo` recorded in the function's docstring, and they are
[pinned by `xfail` tests](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py)
that turn into failures the day they are fixed. Doing it is exactly the kind of
exercise the [Guide](../guide/index.md) prepares you for.

## See also

- [API reference](api.md) — the generated signature, arguments and examples.
- [Guide → Testing](../guide/python-library/testing.md) — how `pytest` pins the
  rule above down.
