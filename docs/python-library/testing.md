# Testing

!!! note "Under construction"
    Planned contents are listed below.

## Why unit tests

What they protect against, and why they are what makes refactoring safe.

## The `tests/` structure

How the test tree mirrors the source tree, and how to name test files and test
functions.

## Writing and running tests with `pytest`

Assertions, fixtures, parametrization and how to run a subset:

```bash
pip install -e ".[test]"
pytest
```

## Tests in continuous integration

How the `tests.yml` workflow runs the suite on every push and pull request, and
how it becomes a required check before merging. See
[GitHub Actions](../github/actions.md) and
[Repository configuration](../github/repository-configuration.md).
