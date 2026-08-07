# Library

**`esperantilo`** is a rule-based Natural Language Processing library for
Esperanto. This section is its *reference manual*: what it does today, how to
install it, and what every public name means.

!!! info "Reference, not tutorial"
    These pages document the library **as it is**. The
    [Guide](../guide/index.md) is the other half of this site: it teaches how a
    library like this one is built, shipped and tested. If you are here to
    learn the tooling, start there.

!!! warning "Two features so far"
    The library is at version `0.1.0` and ships two things: reading Wikipedia
    articles, and sentence segmentation. Everything else — tokens, lemmas, affix
    analysis — is still a [design target](../guide/python-library/api.md), not
    shipped code.

<div class="grid cards" markdown>

- [**1. Sentence segmentation**](sentence-segmentation.md) — splitting a text into sentences.
- [**2. Reading Wikipedia**](wikipedia.md) — fetching an article as plain text, in any language.
- [**3. API reference**](api.md) — every public name, generated from the source.

</div>

## Installation

The library depends on [`requests`](https://requests.readthedocs.io/), which
`pip` pulls in with it. Install it straight from GitHub:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

Step-by-step instructions, including virtual environments and notebooks, are in
[Guide → Installation and usage](../guide/python-library/installation-and-usage.md).

## Quick start

```python
import esperantilo

# Analyse text you already have.
esperantilo.sentence_tokenizer("Zamenhof kreis Esperanton. Ĉu vere? Jes!")
# ['Zamenhof kreis Esperanton.', 'Ĉu vere?', 'Jes!']

# Or fetch it from Wikipedia first.
page = esperantilo.WikiPage.look_up("Esperanto", language="eo")
esperantilo.sentence_tokenizer(page.section(page.title))
```

## The public API

Everything the library promises to keep stable is importable directly from the
top-level `esperantilo` module, and is listed in its `__all__`:

| Name | Kind | What it is |
| --- | --- | --- |
| [`WikiPage`](api.md#esperantilo.wiki.WikiPage) | class | One Wikipedia article, in one language, as plain text. |
| [`sentence_tokenizer`](api.md#esperantilo.nlp.sentence_tokenizer) | function | Splits a text into sentences. |
| [`__version__`](api.md#esperantilo.__version__) | constant | The installed version. |

Anything not in that list — every module-private helper, every internal
module — is an implementation detail and may change without notice. Why that
boundary matters, and how it is drawn in Python, is explained in
[Guide → API](../guide/python-library/api.md).

## Where the pieces live

```text
src/esperantilo/
├── __init__.py      # the public API: re-exports and __all__
├── nlp/             # analysing text that is already in hand
│   └── tokenizer.py #   sentence segmentation
└── wiki/            # fetching text from Wikipedia
    ├── wiki.py      #   the WikiPage class
    └── _wiki_api.py #   private: the MediaWiki and Wikidata clients
```

The [API reference](api.md) is **generated from those files** every time the
site is built, so change a docstring and the page changes with it.
