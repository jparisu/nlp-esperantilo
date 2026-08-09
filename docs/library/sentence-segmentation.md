# Sentence segmentation

Splitting a text into sentences is the first step of almost every NLP pipeline.
`esperantilo` does it with
[`sentence_tokenizer`](api.md#esperantilo.nlp.sentence_tokenizer).

```python
from esperantilo import sentence_tokenizer

sentence_tokenizer("Mi lernas Esperanton. Ĉu vere? Jes!")
# ['Mi lernas Esperanton.', 'Ĉu vere?', 'Jes!']
```

## The current rule

This tokenizer uses the characters given as an input argument to split the text
into sentences.
By default, they are `.`, `!` and `?`.

An example using specific characters would be:

```python
sentence_tokenizer("Unua. Dua! Tria?", end_of_sentence=("!",))
# ['Unua. Dua!', 'Tria?']
```

## Improvements

This tokenizer is a very simplified first version.
Some improvements worth implementing are:

1. Do not cut on abbreviations such as `Dr.` or `S-ro`.
2. Do not cut on decimal numbers such as `3.14`, or on other punctuation cases
   such as `...` or `?!`.
3. Do not cut on URLs, e-mail addresses and other tokens that contain `.` or `?`.
4. etc.

## See also

- [API reference](api.md) — the generated signature, arguments and examples.
- [Guide → Testing](../guide/python-library/testing.md) — how `pytest` pins the
  rule above down.
