# NLP Esperantilo

[![docs](https://github.com/jparisu/nlp-esperantilo/actions/workflows/docs.yml/badge.svg)](https://github.com/jparisu/nlp-esperantilo/actions/workflows/docs.yml)
[![tests](https://github.com/jparisu/nlp-esperantilo/actions/workflows/tests.yml/badge.svg)](https://github.com/jparisu/nlp-esperantilo/actions/workflows/tests.yml)
[![spellcheck](https://github.com/jparisu/nlp-esperantilo/actions/workflows/spellcheck.yml/badge.svg)](https://github.com/jparisu/nlp-esperantilo/actions/workflows/spellcheck.yml)

This repository contains a collection of tools and resources for natural language processing (NLP) in Esperanto.
The goal is to provide a comprehensive suite of tools for researchers, developers, and enthusiasts working with the Esperanto language.
It also hosts a guide on how to build a similar NLP toolchain, for educational purposes.

📖 **Documentation:** <https://jparisu.github.io/nlp-esperantilo/>

The documentation has two parts:

- **[Library](https://jparisu.github.io/nlp-esperantilo/library/)** — the reference
  manual of the `esperantilo` package: what it does today, and what every public
  name means. Its
  [API reference](https://jparisu.github.io/nlp-esperantilo/library/api/) is
  generated from the docstrings in `src/`.
- **[Guide](https://jparisu.github.io/nlp-esperantilo/guide/)** — how a library
  like it is built and shipped: Git, GitHub, Python packaging and testing, and
  the Esperanto linguistics that go inside.

## Repository structure

```text
nlp-esperantilo/
├── .github/workflows/    # Continuous integration: tests, docs, previews, spell check
├── docs/                 # Documentation sources (MkDocs)
│   ├── library/          #   reference manual of the library
│   ├── guide/            #   the guide: Git, GitHub, Python, Esperanto
│   └── hooks/            #   build-time hooks that turn resources/ into pages
├── resources/            # Machine-readable word lists (JSON)
├── src/esperantilo/      # The Python library
├── tests/                # Test suite (pytest)
├── mkdocs.yml            # Documentation configuration
└── pyproject.toml        # Package metadata and build configuration
```

## Installation

Directly from GitHub, which is the recommended way while the library is still
under development:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

```python
import esperantilo

esperantilo.sentence_tokenizer("Zamenhof kreis Esperanton. Ĉu vere? Jes!")
# ['Zamenhof kreis Esperanton.', 'Ĉu vere?', 'Jes!']
```

The library is at `0.1.0` and ships one feature, sentence segmentation. Tokens,
lemmas and affix analysis are still a design target — building them is the
exercise the guide prepares you for.

## Development

```bash
python -m venv .venv
source .venv/bin/activate

pip install -e ".[test]"   # library and test dependencies
pytest                     # run the test suite
```

### Documentation

```bash
pip install -r docs/requirements.txt
mkdocs serve               # live preview at http://127.0.0.1:8000
mkdocs build --strict      # the same build the CI runs
```

The site is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
and published to GitHub Pages on every push to `main`.
Translations live next to the English pages as `<page>.<locale>.md`; missing
translations fall back to English.

Every pull request also gets a **live preview** of the whole site at
`https://jparisu.github.io/nlp-esperantilo/pr-preview/pr-<number>/`, linked from
a comment on the pull request. The public site is not touched until the pull
request is merged, and the preview is removed when it closes.

### Word lists

The linguistic data lives in [`resources/`](resources/README.md) as JSON, and
the documentation pages under *Esperanto → Word lists* are generated from those
files at build time by [`docs/hooks/word_lists.py`](docs/hooks/word_lists.py). Adding an
entry to `resources/listoj.json` is enough for a new page to appear — no page to
write, no navigation entry to add. The pages are English only.

Every word lives once in [`resources/vortoj.json`](resources/vortoj.json); each
list in [`resources/listoj.json`](resources/listoj.json) is a filter over it, so
a preposition that is also a stop-word is stored once and shown by both lists.

| List | Entries |
| --- | --- |
| Stop-words | 250 |
| Prepositions | 34 |
| Correlatives | 59 |
| Numbers | 27 |

### Spell check

```bash
pip install codespell
codespell                  # settings in [tool.codespell] in pyproject.toml
```

Project-specific vocabulary (Esperanto words, proper names) goes in
[`.codespell/ignore-words.txt`](.codespell/ignore-words.txt).

## License

Apache License 2.0 — see [LICENSE](LICENSE).
