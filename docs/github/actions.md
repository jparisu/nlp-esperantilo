# GitHub Actions

!!! note "Under construction"
    Planned contents are listed below.

## What a workflow is

Events, jobs, steps and runners; where workflow files live
(`.github/workflows/`) and how to read a run.

## Examples from this repository

The three workflows of this repository are used as the working examples:

| Workflow | File | What it does |
| --- | --- | --- |
| Tests | `.github/workflows/tests.yml` | Runs `pytest` on several Python versions. |
| Documentation | `.github/workflows/docs.yml` | Builds the MkDocs site, and deploys it to GitHub Pages from `main`. |
| Spell check | `.github/workflows/spellcheck.yml` | Runs `codespell` over the documentation and the code. |

## Running Python tests

Checkout, set up Python, install dependencies, run `pytest`, and use a matrix
to cover several versions.

## Rendering and deploying the documentation

Building with `mkdocs build --strict` on every pull request, and publishing to
GitHub Pages only from the default branch. See [GitHub Pages](pages.md).

## Spell checking

Running a spell checker in CI, and how to teach it project-specific words
(Esperanto terms, proper names) through an ignore list.
