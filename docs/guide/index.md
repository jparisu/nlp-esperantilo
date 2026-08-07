# Guide

A guide to building and shipping a Python library like this one: the version
control, the collaborative workflow, the packaging and testing, and the
linguistic knowledge that goes inside.

!!! info "Guide, not reference"
    These pages teach the *how*. The [Library](../library/index.md) section is
    the other half of this site: the reference manual of `esperantilo` itself —
    what it does today and what every public name means. The guide links to it
    whenever a real, working example makes a point better than prose.

## Who this is for

University students who have to build their own Esperanto NLP library. Readers
are expected to have a technical background, but not necessarily experience with
these specific tools.

## The four sections

<div class="grid cards" markdown>

- [**1. Git**](git/index.md) — version control: how it works, the commands you
  need, and how to undo things.
- [**2. GitHub**](github/index.md) — the collaborative workflow: pull requests,
  Actions, repository protection, Pages.
- [**3. Python Library**](python-library/index.md) — packaging, layout, API
  design, installation and testing.
- [**4. Esperanto**](esperanto/index.md) — history, grammar, vocabulary and word
  lists: the rules the library encodes.

</div>

The sections are mostly independent. Read them in order if you are starting from
scratch; jump straight to [Python Library](python-library/index.md) or
[Esperanto](esperanto/index.md) if you already know Git and GitHub.

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

The library does *use* the first of those two — `esperantilo.wiki` calls the
Wikipedia and Wikidata APIs with `requests` — but as shipped code to read, not
as a lesson: see [Library → Reading Wikipedia](../library/wikipedia.md).

## This repository is the worked example

Wherever the guide shows a file, a workflow or a commit, it is a real one from
this repository — not an invented snippet. The
[Library](../library/index.md) section documents the result.

| The guide explains | You can see it running in |
| --- | --- |
| [`pyproject.toml` and the `src/` layout](python-library/organization.md) | [`pyproject.toml`](https://github.com/jparisu/nlp-esperantilo/blob/main/pyproject.toml) |
| [Designing a public API](python-library/api.md) | [Library → API reference](../library/api.md) |
| [Writing tests](python-library/testing.md) | [`tests/test_tokenizer.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py) |
| [GitHub Actions](github/actions.md) | [`.github/workflows/`](https://github.com/jparisu/nlp-esperantilo/tree/main/.github/workflows) |
| [GitHub Pages](github/pages.md) | this site |
