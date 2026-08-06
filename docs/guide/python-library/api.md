# API

The **API** (Application Programming Interface) of a library is its *public
surface*: the objects, functions and methods that users are meant to touch.
Everything else is an implementation detail you are free to change. Designing
that surface well is what separates a library people enjoy using from one they
fight with.

The `esperantilo` package exposes exactly one function so far, so most of this
page is a **design target**: it shows what a clean NLP interface looks like —
modelled on [spaCy](https://spacy.io/api) — so that the library's own
`Doc` / `Token` interface can be built to imitate it.

!!! tip "The part that already exists"
    Everything below is illustrated by real, shipped code:
    [Library → API reference](../../library/api.md) is the current public surface
    of `esperantilo`, generated from its docstrings. Read this page for *why* an
    API looks the way it does, and that one for *what* the library offers today.

## What an API is here

Think of a library as having two sides:

- the **public API** — what users import and call, and what you promise to keep
  stable across versions;
- the **internals** — helper functions, private modules and data structures that
  make it work, which you can rewrite at any time.

The value of the distinction is freedom: as long as the public API keeps its
shape, you can refactor everything behind it without breaking a single user. The
first job of API design is therefore to **decide what is public** and to make
that boundary obvious.

In Python, the boundary is drawn by convention and by `__all__`:

- Names prefixed with an underscore (`_helper`, `_Cache`) are **private** — a
  signal that users should not rely on them.
- The `__all__` list in a module names its **public** objects. It documents the
  intended surface and controls what `from esperantilo import *` brings in:

```python
# esperantilo/__init__.py
from esperantilo.tokens import Doc, Token
from esperantilo.pipeline import parse

__all__ = ["parse", "Doc", "Token"]   # the public API, stated explicitly
```

With this, a user writes `from esperantilo import Doc` and never has to know
which internal module `Doc` really lives in.

## Designing a good one

A handful of principles make an interface predictable and pleasant. They are the
same ones that make [scikit-learn and spaCy](library.md#a-concrete-example) easy
to learn:

- **Consistency.** Similar things should look similar. If a `Doc` is iterable to
  yield `Token`s, then any collection in the library should be iterable the same
  way.
- **Small, predictable signatures.** Few parameters, sensible defaults, and no
  surprises. `parse(text)` should just work; options are extras, not
  obligations.
- **Meaningful names.** `lemma`, `pos`, `is_stop` say what they are. Avoid
  abbreviations that only the author understands.
- **Type hints.** Annotate parameters and return types. They document the
  interface, enable editor autocompletion, and let tools catch mistakes before
  runtime.
- **Docstrings.** Every public object gets a short docstring saying what it does,
  what it takes and what it returns.

```python
def parse(text: str) -> "Doc":
    """Analyse Esperanto ``text`` and return a :class:`Doc`.

    Args:
        text: the raw Esperanto text to analyse.

    Returns:
        A ``Doc`` holding the analysed tokens.
    """
    ...
```

The type hints (`text: str`, `-> "Doc"`) and the docstring together tell a user
everything they need to call `parse` correctly, without reading its body.

## A spaCy-like API

[spaCy](https://spacy.io) is the reference model for this project. Its design is
worth copying because it turns messy text processing into a small set of typed,
predictable objects. The core idea: **analysing text returns a `Doc`, and a
`Doc` is a sequence of `Token`s**, each carrying its linguistic attributes.

Here is the spaCy shape, which the Esperanto library aims to mirror:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The quick brown fox jumps.")   # -> a Doc

for token in doc:                          # a Doc is iterable over Tokens
    print(token.text, token.lemma_, token.pos_, token.is_stop)
```

```text
The    the    DET    True
quick  quick  ADJ    False
brown  brown  ADJ    False
fox    fox    NOUN   False
jumps  jump   VERB   False
.      .      PUNCT  False
```

Two typed objects carry the whole model:

| Object | What it represents | Typical attributes |
| --- | --- | --- |
| **`Doc`** | An analysed piece of text | iterable of `Token`, `text`, `sents` |
| **`Token`** | A single word/unit | `text`, `lemma`, `pos`, `is_stop` |

Applied to Esperanto — where the [regular grammar](../esperanto/grammar.md) makes
these attributes computable by rule — the target interface looks like this:

```python
# Illustrative target API for esperantilo.
import esperantilo

doc = esperantilo.parse("La rapida vulpo saltas.")

for token in doc:
    print(token.text, token.lemma, token.pos, token.is_stop)
```

```text
La      la      DET     True
rapida  rapida  ADJ     False
vulpo   vulpo   NOUN    False
saltas  salti   VERB    False
.       .       PUNCT   False
```

Notice how the Esperanto endings map cleanly onto attributes — `-a` → adjective,
`-o` → noun, `-as` → present-tense verb (with lemma `salti`), and `la` is a
stop-word. That regularity, described in the [Esperanto section](../esperanto/grammar.md),
is exactly what makes a rule-based `Doc` / `Token` implementation feasible.

For the full reference to imitate — method names, attribute names and object
relationships — see the [spaCy API documentation](https://spacy.io/api).

## Documenting the API automatically

An API reference written by hand rots: someone renames a parameter and the page
still shows the old one. The fix is to generate the page **from the docstrings**,
so there is only ever one copy of the truth.

[mkdocstrings](https://mkdocstrings.github.io/) does that for MkDocs. A page
holding nothing but a directive:

```markdown
::: esperantilo.tokenizer
    options:
      members:
        - sentence_tokenizer
```

renders the signature, the type hints, the argument table and the examples of
every listed object, each with a link to the source lines it came from. That is
exactly how [Library → API reference](../../library/api.md) is built; its page
source is [three directives and a paragraph](https://github.com/jparisu/nlp-esperantilo/blob/main/docs/library/api.md).

Two habits make the generated page worth reading:

- **Write docstrings in a consistent style.** This project uses the Google style
  shown above (`Args:`, `Returns:`, `Examples:`), declared once in
  `mkdocs.yml`.
- **Put examples in `Examples:` blocks.** Written as `>>>` sessions they are both
  documentation and [doctests](testing.md#doctests) — CI runs them, so they
  cannot silently go stale.

## Where to go next

- [Library → API reference](../../library/api.md) — the same ideas, applied: the
  real public surface of `esperantilo`, generated from its source.
- [Testing](testing.md) — how to verify the API behaves as designed.
- [Esperanto § Grammar](../esperanto/grammar.md) — the rules the API will encode.
