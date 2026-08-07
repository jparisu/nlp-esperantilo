# Organization

A library is more than its source code: it needs a handful of files that tell
Python (and `pip`) how to build, install and describe it. This page walks
through the layout this repository uses and the purpose of each file, so you can
reproduce it in your own project.

## Recommended layout

This project uses the **`src/` layout**, the current best practice for Python
packages:

```text
nlp-esperantilo/
├── pyproject.toml        # project metadata and build configuration
├── README.md             # front page
├── LICENSE               # licence text
├── mkdocs.yml            # documentation configuration
├── docs/                 # the documentation you are reading
│   └── hooks/            #   build-time hooks that turn resources/ into pages
├── resources/            # data files (word lists) and notebooks
├── .github/workflows/    # continuous integration
├── src/
│   └── esperantilo/      # the package itself
│       ├── __init__.py   # the public API: re-exports and __all__
│       ├── nlp/          # one subpackage per feature area
│       │   └── tokenizer.py
│       └── wiki/
│           ├── wiki.py       # the public class
│           └── _wiki_api.py  # private: the HTTP clients
└── tests/
    ├── test_package.py    # the package imports and exposes its public API
    ├── test_resources.py  # validation of the data files
    └── test_tokenizer.py  # one test module per source module
```

Note the pairing: `tokenizer.py` in `src/`, `test_tokenizer.py` in `tests/`. It
scales without thinking — a new feature is a new module and a new test module —
and it makes a missing test obvious. What that particular module does is
documented in
[Library → Sentence segmentation](../../library/sentence-segmentation.md).

Once a feature grows past a single module it becomes a **subpackage**: a
directory with its own `__init__.py` that re-exports the feature's public names.
`wiki/` is one — a public class in `wiki.py` and a private HTTP client in
`_wiki_api.py`, of which only the class is re-exported. Users still write
`from esperantilo import WikiPage` and never learn either filename.

The distinguishing feature is that the importable package lives under `src/`, not
at the repository root. The reason is subtle but important — see
[The `src/` layout](#the-src-layout) below.

## The files that matter

### `pyproject.toml`

This single file describes the whole project: its **metadata** (name, version,
description), its **dependencies**, and how it is **built**. It is the modern,
standardised replacement for the older `setup.py`. Here are the key parts of this
project's file:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "esperantilo"
version = "0.1.0"
description = "A rule-based Natural Language Processing library for Esperanto"
requires-python = ">=3.9"
dependencies = ["requests>=2.25"]      # the only runtime dependency

[project.optional-dependencies]
test = ["pytest>=7.0"]                 # installed with .[test]
docs = ["mkdocs>=1.6", "mkdocs-material>=9.5", "mkdocs-static-i18n>=1.2"]

[tool.setuptools.packages.find]
where = ["src"]                        # find the package under src/

[tool.pytest.ini_options]
pythonpath = ["src"]      # so `pytest` works without installing
testpaths = ["tests", "src"]
```

Three parts are worth understanding:

- **`[project]`** — the identity of the library. `name` is what people
  `pip install`; `version` is what they pin; `dependencies` is what gets
  installed *with* it (empty here, because the library is rule-based).
- **`[project.optional-dependencies]`** — *extras*, installed on demand. `.[test]`
  adds `pytest`, `.[docs]` adds the MkDocs tools. Users of the library need
  neither; developers do.
- **`[tool.*]`** — configuration for other tools kept in one place. Here
  `[tool.setuptools.packages.find]` tells the build where the package is, and
  `[tool.pytest.ini_options]` configures the test runner.

### `requirements.txt`

A plain list of dependencies, one per line, traditionally used with
`pip install -r requirements.txt`. It overlaps with `pyproject.toml`, so which
does what?

- **`pyproject.toml`** declares what the *library* needs to run, as part of its
  identity. This is the source of truth when someone installs `esperantilo`.
- **`requirements.txt`** is a convenience list, often used to pin exact versions
  for a reproducible *environment*.

**This project has no root `requirements.txt`.** The library is rule-based and
has no runtime dependency, so the file would hold nothing that
`pyproject.toml` does not already say — and an empty file that looks meaningful
is worse than no file. Development extras are declared as
`[project.optional-dependencies]` and installed with `pip install -e ".[test]"`.

The one place a pinned list *does* earn its keep is
[`docs/requirements.txt`](https://github.com/jparisu/nlp-esperantilo/blob/main/docs/requirements.txt):
it fixes exact versions of the documentation toolchain so that the
[CI workflows](../github/actions.md) build the site the same way every time.

### `__init__.py`

An `__init__.py` file marks a directory as a **regular package**. Since Python 3.3
a folder without one can still be imported, as a *namespace package*, but a
library should be explicit: the file runs when the package is first imported, and
it defines the package's **public surface**. This project's is deliberately
minimal:

```python
"""Esperantilo: a rule-based NLP library for Esperanto."""

__version__ = "0.1.0"

__all__ = ["__version__"]
```

For now it only exposes the version. As the library grows, this is where you
would import and re-export the public classes and functions (the `Doc` and
`Token` objects designed on [the API page](api.md)), so that users can write
`from esperantilo import Doc` instead of reaching into internal modules. The
`__all__` list is explained there too.

### `src/` — why the code is not at the root {#the-src-layout}

Placing the package under `src/` prevents a classic and confusing bug. If the
package sat at the repository root, then running Python *from* the root would
import the local folder directly — even if the library was never installed. Tests
would pass against the raw source while a real user's installed copy behaves
differently.

With the `src/` layout, the root is *not* importable, so you are forced to
**install the package** (`pip install -e .`) before importing it. Your tests then
run against the library exactly as a user would receive it. It is one extra step
that removes a whole category of "works on my machine" problems.

### `tests/` — mirroring the source

The `tests/` folder holds the test suite, kept separate from the shipped code so
that tests are not installed for end users. It mirrors what it tests:
[`test_package.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_package.py)
checks the package imports and exposes its version, and
[`test_resources.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_resources.py)
validates the data files under `resources/`. Testing has its own page:
[Testing](testing.md).

## Versioning

The library's version is declared as `version` in `pyproject.toml` and mirrored by
`__version__` in `__init__.py`, so it is readable at runtime:

```python
>>> import esperantilo
>>> esperantilo.__version__
'0.1.0'
```

The numbers follow **semantic versioning**, `MAJOR.MINOR.PATCH`:

- **PATCH** (`0.1.0 → 0.1.1`) — backward-compatible bug fixes.
- **MINOR** (`0.1.0 → 0.2.0`) — new features, still backward-compatible.
- **MAJOR** (`0.1.0 → 1.0.0`) — changes that break the existing API.

To release a new version, bump the number (in both places) and merge it through
the usual [pull-request workflow](../github/workflow.md).

## Where to go next

- [Installation and usage](installation-and-usage.md) — install this package and
  import it.
- [API](api.md) — design the public interface that `__init__.py` will expose.
