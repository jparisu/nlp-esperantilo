# API

!!! note "Under construction"
    Planned contents are listed below.

## What an API is here

The public surface of a library: what users are allowed to touch, and what is
an implementation detail.

## Designing a good one

Consistency, small and predictable signatures, meaningful names, type hints and
docstrings. What `__all__` is for.

## A spaCy-like API

spaCy is the reference model for this project. This subsection shows, with
short examples, what a good NLP interface looks like:

- typed objects such as `Doc` and `Token`,
- typed function signatures with type hints,
- illustrative snippets,
- links to the [spaCy API documentation](https://spacy.io/api).

The goal is a concrete target to imitate when designing the `Doc` / `Token`
interface of the Esperanto library.
