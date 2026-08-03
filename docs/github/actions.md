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
| Documentation | `.github/workflows/docs.yml` | Builds the MkDocs site and publishes it to GitHub Pages from `main`. |
| Documentation preview | `.github/workflows/docs-preview.yml` | Builds the site for a pull request and publishes it to a preview URL. |
| Spell check | `.github/workflows/spellcheck.yml` | Runs `codespell` over the documentation and the code. |

## Running Python tests

Checkout, set up Python, install dependencies, run `pytest`, and use a matrix
to cover several versions.

## Rendering and deploying the documentation

Building with `mkdocs build --strict` on every pull request, and publishing to
GitHub Pages only from the default branch.

## Previewing the documentation of a pull request

How a pull request gets its own published copy of the site, at a URL a reviewer
can open, without changing the public site — and how that copy is deleted when
the pull request closes. See [GitHub Pages](pages.md#previewing-a-pull-request).

This also covers the two workflow concepts it relies on: the `closed` event
type, and why a workflow that writes to the repository needs
`permissions: contents: write`.

## Spell checking

Running a spell checker in CI, and how to teach it project-specific words
(Esperanto terms, proper names) through an ignore list.
