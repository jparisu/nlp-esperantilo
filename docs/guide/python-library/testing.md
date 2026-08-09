# Testing

Tests are code that checks your code. They are what let you change a library with
confidence: if a change breaks something, a test catches it immediately instead
of a user finding out later. This page explains why they matter, how the
`tests/` folder is organised, how to write and run them with **pytest**, and how
they become an automatic gate on every pull request.

## Why unit tests

A **unit test** exercises one small piece of the library in isolation and asserts
that it behaves as expected. Their real value shows up over time:

- **They catch regressions.** When you change the tokenizer, the tests tell you at
  once whether you broke the lemmatizer that depends on it.
- **They make refactoring safe.** You can rewrite the internals of the
  [API](api.md) freely, because a passing suite proves the public behaviour is
  unchanged.
- **They document behaviour.** A test is an executable example of how a function
  is meant to be called and what it should return.
- **They enable collaboration.** On a team, tests are how you trust a teammate's
  pull request without re-reading all of it — the checks are green.

The cost is small and paid once; the benefit compounds every time the code
changes.

## The `tests/` structure

Tests live in a top-level `tests/` folder, kept out of the shipped package (see
[Organization](organization.md)). The suite **mirrors the source**: each part of
the library has a matching `test_*.py` file, so it is obvious where a test lives
and where one is missing.

```text
tests/
├── test_package.py     # the package imports and exposes its public API
├── test_resources.py   # the data files are valid
└── test_tokenizer.py   # sentence segmentation behaves as documented
```

`test_tokenizer.py` pairs with `src/esperantilo/nlp/tokenizer.py`, whose behaviour is
described in
[Library → Sentence segmentation](../../library/sentence-segmentation.md). One
source module, one test module: that pairing is the whole convention.

Two naming conventions let pytest **discover** tests automatically, with no
registration:

- test *files* are named `test_*.py`,
- test *functions* are named `test_*`.

This project's smoke test shows the shape — import the thing, then assert
something about it:

```python
# tests/test_package.py
import esperantilo


def test_package_is_importable():
    assert esperantilo is not None


def test_version_is_exposed():
    assert isinstance(esperantilo.__version__, str)
    assert esperantilo.__version__
```

Each function tests one fact, and its name says what that fact is — so a failure
report reads like a sentence: `test_version_is_exposed failed`.

## Writing and running tests with `pytest`

[pytest](https://docs.pytest.org/) is the de-facto standard test runner for
Python. Install it via the test extra and run the whole suite with one word:

```bash
pip install -e ".[test]"
pytest
```

!!! tip "`pytest` works without installing anything"
    The package lives under `src/`, which Python does not search by default, so
    a bare `pytest` on a fresh clone would fail with
    `No module named 'esperantilo'`. `pythonpath = ["src"]` in
    `pyproject.toml` puts it on the path for the test run, so `pytest` works
    straight after `git clone`.

```console
$ pytest
===================== test session starts =====================
configfile: pyproject.toml
testpaths: tests, src
collected 300 items

tests/test_package.py ........                            [  2%]
tests/test_resources.py ...........................       [ 18%]
tests/test_tokenizer.py .............xxx                  [ 97%]
src/esperantilo/nlp/tokenizer.py .                        [ 97%]
src/esperantilo/wiki/_wiki_api.py ..                      [ 98%]
src/esperantilo/wiki/wiki.py .....                        [100%]

=============== 297 passed, 3 xfailed in 0.13s ================
```

The everyday features you will reach for:

- **Assertions.** Plain `assert` statements — pytest rewrites them to show the
  actual values on failure, so you rarely need anything else.
- **Parametrization.** Run the same test over many inputs with
  `@pytest.mark.parametrize`, instead of copy-pasting. This project uses it to
  run the same checks over *every* file in `resources/`:

    ```python
    @pytest.mark.parametrize("path", FILES, ids=lambda p: p.name)
    def test_mandatory_fields(path):
        data = json.loads(path.read_text(encoding="utf-8"))
        for field in ("id", "titolo", "vortoj"):
            assert field in data, f"missing '{field}'"
    ```

- **Fixtures.** Reusable setup shared across tests (a sample document, a temporary
  file), declared once and requested by name.
- **Running a subset** while you focus on one area:

    ```bash
    pytest tests/test_package.py           # one file
    pytest -k version                      # tests whose name matches "version"
    pytest -x                              # stop at the first failure
    ```

!!! tip "Test behaviour, not implementation"
    Assert on what a function *returns or does*, not on how it does it. Then your
    tests keep passing through internal refactors and only fail when behaviour
    actually changes — which is the whole point.

## Tests in continuous integration

Running tests locally is good; running them **automatically on every change** is
what makes them a real safety net. The [`tests.yml` workflow](../github/actions.md#running-python-tests)
runs `pytest` on every push and pull request to `main`, so a broken change is
flagged on GitHub before anyone merges it.

The final step is to make that check **mandatory**: with
[branch protection](../github/repository-configuration.md#required-status-checks),
a pull request cannot be merged while its tests are red. Local `pytest`, CI and
branch protection then form a chain — you catch problems early, CI catches what
you missed, and the rules make sure nothing broken reaches `main`.

## Where to go next

- [GitHub Actions](../github/actions.md) — the workflow that runs these tests.
- [Esperanto](../esperanto/index.md) — the linguistic rules the library, and its
  tests, will encode.
- [Library → Sentence segmentation](../../library/sentence-segmentation.md) — the
  behaviour that
  [`tests/test_tokenizer.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py)
  pins down, and a worked example of the conventions on this page.
