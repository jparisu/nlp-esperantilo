# NLP Esperantilo

[![docs](https://github.com/jparisu/nlp-esperantilo/actions/workflows/docs.yml/badge.svg)](https://github.com/jparisu/nlp-esperantilo/actions/workflows/docs.yml)
[![tests](https://github.com/jparisu/nlp-esperantilo/actions/workflows/tests.yml/badge.svg)](https://github.com/jparisu/nlp-esperantilo/actions/workflows/tests.yml)
[![spellcheck](https://github.com/jparisu/nlp-esperantilo/actions/workflows/spellcheck.yml/badge.svg)](https://github.com/jparisu/nlp-esperantilo/actions/workflows/spellcheck.yml)

This repository contains a collection of tools and resources for natural language processing (NLP) in Esperanto.
The goal is to provide a comprehensive suite of tools for researchers, developers, and enthusiasts working with the Esperanto language.
It will also host a guide on how to build a similar NLP toolchain, for educational purposes.

📖 **Documentation:** <https://jparisu.github.io/nlp-esperantilo/>

## Repository structure

```text
nlp-esperantilo/
├── .github/workflows/    # Continuous integration: tests, docs, spell check
├── docs/                 # Documentation sources (MkDocs)
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

print(esperantilo.__version__)
```

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

### Spell check

```bash
pip install codespell
codespell                  # configuration in .codespellrc
```

Project-specific vocabulary (Esperanto words, proper names) goes in
`.codespell-ignore-words.txt`.

## License

Apache License 2.0 — see [LICENSE](LICENSE).
