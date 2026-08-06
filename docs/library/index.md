# Library

**`esperantilo`** is a rule-based Natural Language Processing library for
Esperanto. This section is its *reference manual*: what it does today, how to
install it, and what every public name means.

!!! info "Reference, not tutorial"
    These pages document the library **as it is**. The
    [Guide](../guide/index.md) is the other half of this site: it teaches how a
    library like this one is built, shipped and tested. If you are here to
    learn the tooling, start there.

!!! warning "One feature so far"
    The library is at version `0.1.0` and ships exactly one thing: sentence
    segmentation. Everything else — tokens, lemmas, affix analysis — is still a
    [design target](../guide/python-library/api.md), not shipped code.

<div class="grid cards" markdown>

- [**1. Sentence segmentation**](sentence-segmentation.md) — splitting a text into sentences.
- [**2. API reference**](api.md) — every public name, generated from the source.

</div>

## Installation

The library has **no runtime dependencies**. Install it straight from GitHub:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

Step-by-step instructions, including virtual environments and notebooks, are in
[Guide → Installation and usage](../guide/python-library/installation-and-usage.md).

## Quick start

```python
import esperantilo

esperantilo.sentence_tokenizer("Zamenhof kreis Esperanton. Ĉu vere? Jes!")
# ['Zamenhof kreis Esperanton.', 'Ĉu vere?', 'Jes!']
```

## The public API

Everything the library promises to keep stable is importable directly from the
top-level `esperantilo` module, and is listed in its `__all__`:

| Name | Kind | What it is |
| --- | --- | --- |
| [`sentence_tokenizer`](api.md#esperantilo.tokenizer.sentence_tokenizer) | function | Splits a text into sentences. |
| [`__version__`](api.md#esperantilo.__version__) | constant | The installed version. |

Anything not in that list — every module-private helper, every internal
module — is an implementation detail and may change without notice. Why that
boundary matters, and how it is drawn in Python, is explained in
[Guide → API](../guide/python-library/api.md).

## Where the pieces live

```text
src/esperantilo/
├── __init__.py      # the public API: re-exports and __all__
└── tokenizer.py     # sentence segmentation
```

The [API reference](api.md) is **generated from those files** every time the
site is built, so change a docstring and the page changes with it.
