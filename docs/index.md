# NLP Esperantilo

Welcome to **NLP Esperantilo**, a project made of two complementary parts:

- **A Python library** for rule-based Natural Language Processing in Esperanto.
- **This documentation**, a guide and tutorial to build that library and its
  surrounding tooling from scratch.

!!! warning "Work in progress"
    This site is the scaffold of the documentation. Every section already has
    its structure and its planned contents, but the contents themselves are
    still being written.

## Who is this for

This guide is aimed at university students who have to build their own
Esperanto NLP library. Readers are expected to have some technical background,
but not necessarily experience with the specific tools and topics explained
here.

## What this guide covers

| Section | Contents |
| --- | --- |
| [Git](git/index.md) | Version control: how Git works, its most used commands and how to undo changes. |
| [GitHub](github/index.md) | Collaborative workflow, pull requests, GitHub Actions, repository protection and GitHub Pages. |
| [Python Library](python-library/index.md) | Packaging, project layout, API design, installation and testing. |
| [Esperanto](esperanto/index.md) | History, grammar, vocabulary and resources — the linguistic rules the library encodes. |

## What this guide does *not* cover

Two topics are deliberately left out, because they are taught in the course
lectures:

- **Web scraping and API consumption** (`requests`, `beautifulsoup4`, the
  Wikipedia API, and similar).
- **Text-mining and Machine-Learning classification** (feature extraction,
  vectorization, model training and evaluation, metrics).

The focus here is the *software-engineering tooling* needed to work like a
professional team, and the *Esperanto domain knowledge* needed to write a
rule-based NLP library.

## Reading the documentation

The guide can be read from start to finish, but the four sections are mostly
independent. A reader who already knows Git and GitHub can jump straight to
[Python Library](python-library/index.md) or [Esperanto](esperanto/index.md).

## Building the documentation locally

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

The site is then available at <http://127.0.0.1:8000>. Every push to `main`
rebuilds it and publishes it to GitHub Pages.
