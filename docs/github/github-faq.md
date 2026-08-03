# FAQ

Common questions about GitHub and the collaborative workflow. Each answer links
to the page where the topic is covered in full.

??? question "What is the difference between Git and GitHub?"
    **Git** is the version-control tool that runs on your computer; **GitHub** is
    a website that hosts Git repositories and adds collaboration features (pull
    requests, issues, Actions, Pages). You can use Git with no GitHub; GitHub
    always uses Git underneath. See [What is GitHub](github.md#git-is-not-github).

??? question "Do I have to pay to use GitHub?"
    No. A free account covers everything in this guide: public *and* private
    repositories, unlimited collaborators, GitHub Actions and GitHub Pages. Paid
    plans add higher limits and organisation features you will not need here.

??? question "When do I create a branch and when do I fork?"
    If you have write access to the repository (your own or your team's), create
    a **branch**. If you do not (someone else's public repository), **fork** it —
    make your own copy — then open a pull request back to the original. See
    [Workflow § Branch or fork](workflow.md#branch-or-fork).

??? question "What is a pull request, exactly?"
    A proposal to merge one branch into another, with a diff, a description and a
    discussion attached. It is where review and the automated checks happen
    before code reaches `main`. See [Workflow § Pull request](workflow.md#pull-request).

??? question "What is the difference between an issue and a pull request?"
    An **issue** describes something to do or fix — it is a conversation, no code.
    A **pull request** proposes an actual change and carries a diff. A PR can say
    `Closes #12` to auto-close the issue it resolves when merged. See
    [First steps § Issues and pull requests](first-steps.md#issues-and-pull-requests).

??? question "Git asks for a password when I push, but my GitHub password is rejected. Why?"
    GitHub stopped accepting account passwords for Git operations. Push over
    HTTPS with a **Personal Access Token** in place of the password, or set up an
    **SSH key**. See [First steps § Create an account](first-steps.md#create-an-account).

??? question "What does the green `Verified` badge on a commit mean?"
    That the commit was **cryptographically signed** with a key GitHub associates
    with the author, so its authorship can be trusted. Configure it with GPG or
    SSH signing. See [Workflow § Commit signing](workflow.md#commit-signing).

??? question "What are GitHub Actions?"
    Automation that runs on GitHub's servers when an event happens (a push, a pull
    request). This repository uses them to run tests, check spelling and build the
    documentation automatically. See [GitHub Actions](actions.md).

??? question "A check on my pull request is red. What do I do?"
    Open the failing check in the **Actions** tab and read its log — it names
    exactly what failed. Every check is a command you can run locally (`pytest`,
    `mkdocs build --strict`, `codespell`); fix the problem, push again, and the
    check re-runs. See [GitHub Actions](actions.md).

??? question "Why can't I push directly to `main`?"
    Because the repository has a **ruleset** protecting it: changes must go
    through a reviewed pull request. This is deliberate — it keeps `main` from
    breaking. See [Repository configuration](repository-configuration.md).

??? question "How is this documentation website published?"
    A workflow builds the MkDocs site and pushes it to the `gh-pages` branch,
    which **GitHub Pages** serves at `https://jparisu.github.io/nlp-esperantilo/`.
    Pull requests also get a temporary preview site. See [GitHub Pages](pages.md).

??? question "I opened a pull request but there is no preview link. Why?"
    Most likely the pull request comes from a **fork**, which runs with a
    read-only token and cannot publish a preview. The documentation is still built
    and checked; it just gets no URL. See
    [GitHub Pages § Pull requests from forks](pages.md#previewing-a-pull-request).
