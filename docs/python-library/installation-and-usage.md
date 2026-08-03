# Installation and usage

Once a library is packaged ([Organization](organization.md)), using it is a
`pip install` away. Because most of the work in this course happens in
**notebooks (Google Colab)**, the main path is installing straight from GitHub —
no local setup, no cloning by hand.

## Install from GitHub

`pip` can install a package directly from a Git repository. This is the quickest
way to get `esperantilo` into a notebook while the library is still moving:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

This clones the repository behind the scenes, builds the package from its
`pyproject.toml`, and installs it — exactly as if it came from the Python Package
Index.

You can pin a specific **branch**, tag or commit by appending `@<ref>`:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git@main
pip install git+https://github.com/jparisu/nlp-esperantilo.git@jparisu/v0.1
```

!!! tip "Why install from GitHub?"
    While a library is under active development and not yet published to PyPI,
    installing from GitHub means everyone always gets the latest code from a
    chosen branch, with a single command and no manual steps. It is the natural
    fit for a notebook-based workflow.

## Use it in a notebook

In a Colab notebook, install in a cell (the leading `!` runs a shell command),
then import and use the library:

```python
!pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

```python
import esperantilo

print(esperantilo.__version__)   # 0.1.0
```

As the library grows, the same import gives you its public objects — for example
the `Doc` and `Token` types designed on [the API page](api.md):

```python
# Illustrative: the target API, not yet implemented.
import esperantilo

doc = esperantilo.parse("La rapida vulpo saltas.")
for token in doc:
    print(token.text, token.lemma, token.pos)
```

!!! note "Restart the runtime after installing"
    If you had already imported `esperantilo` in a notebook and then install a
    new version, restart the runtime (**Runtime → Restart**) so the new code is
    picked up. Python caches imported modules for the life of the session.

## Install locally

For developing the library itself — rather than just using it — install it
**locally** in a virtual environment. A virtual environment is an isolated Python
installation for one project, so its dependencies do not clash with anything
else on your machine:

```bash
python -m venv .venv          # create the environment
source .venv/bin/activate     # activate it (Windows: .venv\Scripts\activate)
pip install -e ".[test]"      # editable install, with the test extra
```

Two flags make this a *development* install:

- **`-e` (editable).** The package is installed as a link to your source, so your
  edits take effect immediately — no reinstalling after every change.
- **`.[test]`** installs the package *plus* its `test` extra (`pytest`), so you
  can run the suite right away (see [Testing](testing.md)). Use `.[docs]` to work
  on the documentation instead.

This is exactly what the [`tests.yml` workflow](../github/actions.md#running-python-tests)
does in CI, so a green local run means a green run on GitHub.

## Where to go next

- [API](api.md) — what a clean public interface for the library should look
  like.
- [Testing](testing.md) — run and write the test suite.
