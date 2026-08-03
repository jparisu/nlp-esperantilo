# Example

This page ties the whole section together by **recreating how this very project,
`nlp-esperantilo`, was started** — from an empty folder to a repository pushed
to GitHub, with a branch and a merge conflict along the way.

You can follow along in an empty folder and reproduce every step. Commands are
the lines starting with `$`; everything else is output.

!!! info "What you need"
    Git installed (`git --version` should print a version) and, for the last
    step, a GitHub account. Configure your identity once, so your commits are
    attributed to you:

    ```console
    $ git config --global user.name "Your Name"
    $ git config --global user.email "you@example.com"
    ```

## 1. Create the repository

Start in an empty folder and turn it into a Git repository:

```console
$ mkdir nlp-esperantilo
$ cd nlp-esperantilo
$ git init
Initialized empty Git repository in /home/user/nlp-esperantilo/.git/
```

Before adding anything, create a **`.gitignore`** so generated files never enter
the history (see [Commands § .gitignore](commands.md#the-gitignore-file)):

```console
$ printf '__pycache__/\n.venv/\nsite/\n' > .gitignore
```

## 2. Add files and make the first commit

Create a first file — the project's README:

```console
$ printf '# NLP Esperantilo\n' > README.md
```

Check the state. Git sees two new files it is not yet tracking:

```console
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md

nothing added to commit but untracked files present
```

Stage both files and record the first commit:

```console
$ git add .
$ git commit -m "Initial commit"
[main (root-commit) 29434cf] Initial commit
 2 files changed, 4 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
```

Add a bit more to the README and make a second commit, so we have some history:

```console
$ printf '\nA rule-based NLP library for Esperanto.\n' >> README.md
$ git add README.md
$ git commit -m "Add README"
[main 7b0978f] Add README
 1 file changed, 2 insertions(+)
```

## 3. Inspect the state

Three commands answer "where am I?":

```console
$ git log --oneline
7b0978f Add README
29434cf Initial commit

$ git status
On branch main
nothing to commit, working tree clean

$ git diff
```

`git log` shows the two commits, `git status` confirms there is nothing pending,
and `git diff` prints nothing because there are no uncommitted changes. This is
the clean starting point for new work.

## 4. Create a branch and work on it

New work goes on its own **branch**, not directly on `main`. Create one and
switch to it:

```console
$ git checkout -b docs-design
Switched to a new branch 'docs-design'
```

Add the design document for the documentation and commit it:

```console
$ printf '# DOCS DESIGN\n\nStructure of the documentation.\n' > docs-design.md
$ git add docs-design.md
$ git commit -m "Add docs design"
[docs-design 5f46a63] Add docs design
 1 file changed, 3 insertions(+)
```

The `docs-design` branch is now one commit ahead of `main`. Nothing on `main`
changed — you can switch back and forth to confirm:

```console
$ git checkout main
Switched to branch 'main'
$ ls
README.md          # docs-design.md is not here; it lives on the other branch

$ git checkout docs-design
Switched to branch 'docs-design'
```

## 5. Merge the branch back — and resolve a conflict

To make a conflict happen, let both branches change **the same line** of the
README.

On `main`, tweak the description line:

```console
$ git checkout main
$ printf '# NLP Esperantilo\n\nAn NLP library for the Esperanto language.\n' > README.md
$ git commit -am "Reword README description"
[main a1b2c3d] Reword README description
```

On `docs-design`, change *the same line* differently:

```console
$ git checkout docs-design
$ printf '# NLP Esperantilo\n\nA rule-based NLP toolkit for Esperanto.\n' > README.md
$ git commit -am "Reword README description"
[docs-design e4f5a6b] Reword README description
```

Now merge `docs-design` into `main`. Git cannot decide which wording wins:

```console
$ git checkout main
$ git merge docs-design
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

Open `README.md`. Git has marked the conflicting region:

```text
# NLP Esperantilo

<<<<<<< HEAD
An NLP library for the Esperanto language.
=======
A rule-based NLP toolkit for Esperanto.
>>>>>>> docs-design
```

- Everything between `<<<<<<< HEAD` and `=======` is **your** version (`main`).
- Everything between `=======` and `>>>>>>> docs-design` is the **incoming**
  version.

**Resolve** it by editing the file into the final text you want and deleting all
three marker lines:

```text
# NLP Esperantilo

A rule-based NLP library for the Esperanto language.
```

Then stage the resolved file and complete the merge:

```console
$ git add README.md
$ git commit -m "Merge docs-design into main"
[main 92c1041] Merge docs-design into main
```

The history now shows both lines of work joined by a **merge commit**:

```console
$ git log --oneline --graph
*   92c1041 Merge docs-design into main
|\
| * e4f5a6b Reword README description
* | a1b2c3d Reword README description
|/
* 7b0978f Add README
* 29434cf Initial commit
```

The `docs-design` branch has served its purpose and can be deleted:

```console
$ git branch -d docs-design
Deleted branch docs-design (was e4f5a6b).
```

## 6. Connect a remote and push

So far everything lives on your machine. To share it, create an empty repository
on GitHub (see the [GitHub section](../github/first-steps.md)), then connect it
as the remote **`origin`** and push:

```console
$ git remote add origin https://github.com/jparisu/nlp-esperantilo.git
$ git push -u origin main
Enumerating objects: 12, done.
Writing objects: 100% (12/12), 1.24 KiB, done.
To https://github.com/jparisu/nlp-esperantilo.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

The `-u` flag links your local `main` to `origin/main`, so from now on a plain
`git push` and `git pull` are enough.

## Recap

In one short session you have used every core idea of this section:

- **`init`** to create a repository and **`.gitignore`** to keep it clean,
- **`add`** and **`commit`** to record snapshots,
- **`status`**, **`log`** and **`diff`** to inspect state,
- **`branch`** / **`checkout`** to work in isolation,
- **`merge`** — including **resolving a conflict** — to bring work together,
- **`remote`** and **`push`** to share it with the world.

This is exactly the loop you will repeat, over and over, for the rest of the
project. The next step is doing it *as a team*, which is what the
[GitHub section](../github/index.md) is about.
