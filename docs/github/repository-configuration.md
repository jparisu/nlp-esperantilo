# Repository configuration

!!! note "Under construction"
    Planned contents are listed below.

How to configure a repository so that the workflow of [§ Workflow](workflow.md)
is actually enforced, which matters most when working as a team.

## Branch protection and rulesets

Block direct pushes to `main` and force every change through a pull request.

## Required reviews

Ask for at least one approval before merging, and what "stale review dismissal"
means.

## Required status checks

Make the [GitHub Actions](actions.md) checks — tests, spell check, docs build —
mandatory before a merge is allowed.

## Other useful settings

Linear history, conversation resolution, auto-delete of merged branches.

## Good practices

Pull requests with well-written commits, linter and test gates, and balanced
contribution from every team member.

!!! info
    Protecting `main` only makes sense once branches, pull requests and CI
    checks exist — that is why this page comes after
    [Workflow](workflow.md) and [GitHub Actions](actions.md).
