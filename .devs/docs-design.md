# DOCS DESIGN

This repository consists of two parts:

- a Python library for Natural Language Processing in Esperanto,
- an extensive documentation that works as a guide and tutorial to build that library and its related tooling.

This file describes the structure and organization of the documentation.

## Scope

This documentation is **not** a full walkthrough of the course assignment. It deliberately leaves out the topics that are taught in the course lectures, namely:

- **Web scraping and API consumption** (`requests`, `beautifulsoup4`, the Wikipedia API, etc.).
- **Text-mining / Machine-Learning classification techniques** (feature extraction, corpus vectorization, model training and evaluation, metrics).

Instead, the documentation focuses on:

- the **software-engineering tooling** needed to work like a professional team: Git, GitHub and Python packaging (structure, API design and testing),
- the **Esperanto domain knowledge** required to build a *rule-based* NLP library (grammar rules, affixes, stop-words, roots).

In other words: the reader learns *how to build and ship the library*, and *what linguistic rules to encode in it*; the statistical NLP and data-collection techniques are covered elsewhere in the course.

## Sections

The documentation is divided into four main sections:

1. **Git**: what Git is, how it works, its most used commands and some recommendations.
2. **GitHub**: what GitHub is, how to work with it from creating an account to configuring a repository. It also covers the common Git + GitHub workflow with branches and pull requests, repository configuration, GitHub Actions and GitHub Pages.
3. **Python Library**: how to build a Python library, its required files (`pyproject.toml`, `requirements.txt`), how to design its API, how to test it, and how to install and use it.
4. **Esperanto**: the Esperanto language — its history, grammar, vocabulary and learning resources. This section is strongly oriented towards the linguistics and regular rules of Esperanto, so that the reader can implement a rule-based NLP for it.

## Format and style

This documentation is aimed at university students who have to build their own Esperanto NLP library.
Students are expected to have prior technical knowledge and a good understanding of the environment, but not necessarily experience with the specific contents explained here.

For that reason, the documentation must be sober, clear and concise, with a writing style that is easy to read and understand. The use of diagrams, examples, internal cross-references and links to external resources is strongly encouraged.

Every section will count with a FAQ subsection, where the most common questions and doubts will be answered.

## Language

The documentation must be written in English, but in a way that makes it easy to translate into any other language.
The use of neutral, inclusive language is recommended.

## Implementation

The documentation is written in Markdown, generated with MkDocs and hosted on GitHub Pages.

The recommended setup is **Material for MkDocs**, because it is sober, clear and concise, and covers all the required features out of the box:

- **Diagrams** via native Mermaid support.
- **Light and dark themes** with a palette toggle.
- **Language selection** via an internationalization plugin (e.g. `mkdocs-static-i18n`), so translations can be added without restructuring the content.
- Built-in search, admonitions and code highlighting for examples.

---

## 1. Git

This section aims to explain what Git is, its advantages, how it organizes files and versions, its way of working, and its most used commands.

### 1.1 Git

A bit of history and motivation.

### 1.2 Organization

Explanation of the branch system, of diffs, snapshots, etc.
Include clear diagrams to understand branches and how commits build a history.

### 1.3 Commands

Explain the most used commands:
`init`, `clone`, `add`, `commit`, `status`, `log`, `diff`, `branch`, `checkout`, `merge`, `push`, `pull`.

Also introduce the **`.gitignore`** file: what it is, why it matters, and typical entries for a Python project (virtual environments, caches, notebook checkpoints, build artifacts).

Tags and releases are intentionally left out: for this project, understanding `main` and branches is enough.

### 1.4 Undoing changes

A short subsection at the end presenting the common ways to "go back":

- `restore` — discard changes in the working directory.
- `reset` — move the branch pointer / unstage changes.
- `stash` — temporarily set changes aside.

Keep it practical: when to use each one, with a small example.

### 1.5 Example

A step-by-step example: create a repository, add files, make commits, create branches, merge them, etc.

---

## 2. GitHub

This section aims to introduce the tool and the collaborative workflow of GitHub.
This very repository can be used as a live example.

### 2.1 GitHub

Explanation of what GitHub is, some context and motivation, and how it works.

### 2.2 First steps

Create an account, create and set up a repository, explore other repositories or users, pull requests, issues, etc.

### 2.3 Workflow

Explanation of the common Git + GitHub workflow:

- own repository: new branch; external repository: fork.
- changes, `add`, `commit`, `push`.
- **commit best practices**: how to write meaningful commits (atomic changes, clear messages, a convention such as *Conventional Commits*). This connects directly with keeping a clean, readable history.
- **commit signing**: what a signed commit is and why it matters, and how to configure it (GPG or SSH signing) so commits appear as *Verified*.
- pull request.
- review, comments.
- merge, pull.

### 2.4 GitHub Actions

Explanation of what GitHub Actions are, how they work, and how to create one.
Include examples for:

- running Python tests,
- rendering and deploying the documentation,
- spelling check.

### 2.5 Repository configuration

How to configure a repository to enforce a healthy workflow, especially for teamwork:

- **branch protection / rulesets** on `main` (block direct pushes, force changes through pull requests).
- **required reviews** before merging.
- **required status checks** (e.g. tests and linters from GitHub Actions must pass before merging).
- other useful locks and settings.

Also cover the associated **good practices**: pull requests with well-commented commits, linter and test gates, and balanced contribution from all team members.

This ties back to §2.3 (workflow) and §2.4 (Actions): protecting `main` only makes sense once branches, pull requests and CI checks exist.

### 2.6 GitHub Pages

Explicit subsection on GitHub Pages: what it is and how it hosts a static site directly from the repository.
Explain how the MkDocs-generated documentation is deployed to GitHub Pages (deployment branch / GitHub Actions deploy step, and the resulting public URL), so the reader can publish their own docs.

---

## 3. Python Library

This section aims to explain how to build a Python library, how to organize it, how to design its API, how to test it, and how to install and use it.

### 3.1 Library

Explanation of what a library is and how it works.
Use well-known libraries as an example, such as `scikit-learn`.

### 3.2 Organization

Describe the required files and their purpose, as well as the recommended folder and file structure:

- `pyproject.toml`
- `requirements.txt`
- `tests/`
- `src/`
- `__init__.py`
- etc.

### 3.3 Installation and usage

Guide on how to install and use the library.

Since students will mostly work **in notebooks (Google Colab)** rather than locally, the emphasis is on installing the library directly from its GitHub repository (e.g. `pip install git+https://...`) and importing it inside a notebook.
Installing it locally in a virtual environment is worth mentioning briefly, but does not need to be covered in depth.

Include examples of how to import the library and use it.

### 3.4 API

Explanation of what an API is in the context of a library, and how to design a clear, consistent and readable public interface.

#### 3.4.1 A spaCy-like API

A subsection showing, with examples, what a good NLP API looks like, using **spaCy** as the reference model:

- typed function signatures and typed objects (e.g. `Doc`, `Token`) with type hints,
- short, illustrative code snippets,
- external links to the spaCy API documentation.

This gives the reader a concrete target to imitate when designing the Esperanto library's own `Doc` / `Token` interface.

### 3.5 Testing

Explanation of how to test a Python library:

- what unit tests are and why they matter,
- the `tests/` structure and how it mirrors the source code,
- writing and running tests with `pytest`,
- how tests connect with GitHub Actions (see §2.4) to run automatically on every push.

---

## 4. Esperanto

This section aims to explain the Esperanto language — its history, grammar, vocabulary and learning resources.

### 4.1 History

Explanation of the history of Esperanto: its creator, its motivation and its evolution up to the present day.

### 4.2 Grammar

Explanation of Esperanto grammar, with examples and links to external resources.
This subsection must include **all the regular rules needed to implement the rule-based library** (tokenizer, lemmatizer, POS tagger, stop-word handling). At minimum:

- **Alphabet**: the 28 letters, including the diacritics (`ĉ`, `ĝ`, `ĥ`, `ĵ`, `ŝ`, `ŭ`) — relevant for tokenization and text encoding.
- **Word-class endings** (the core of POS tagging and lemmatization):
  - `-o` → noun, `-a` → adjective, `-e` → adverb, `-i` → verb (infinitive).
- **Grammatical inflections**:
  - `-j` → plural, `-n` → accusative (and their combination `-jn`).
- **Verb system** (tense and mood suffixes): `-as` (present), `-is` (past), `-os` (future), `-us` (conditional), `-u` (imperative/volitive), `-i` (infinitive).
- **The article**: `la` (invariable). No indefinite article.
- **Personal pronouns**: `mi`, `vi`, `li`, `ŝi`, `ĝi`, `ni`, `ili`, `oni`, `si`.
- **Correlatives table** (the `ki-`, `ti-`, `i-`, `ĉi-`, `neni-` prefixes combined with `-o`, `-u`, `-a`, `-e`, `-es`, `-am`, `-al`, `-el`, `-om`).
- **Affixes** used to derive words (essential for lemmatization):
  - prefixes such as `mal-`, `ge-`, `ek-`, `re-`, `dis-`, `mis-`, `bo-`, `pra-`,
  - suffixes such as `-in-`, `-ist-`, `-ej-`, `-il-`, `-ar-`, `-et-`, `-eg-`, `-ul-`, `-an-`, `-ec-`, `-ig-`, `-iĝ-`, `-ind-`, `-em-`, `-aĉ-`.
- **Numbers** and basic compounding rules for word formation.

Include some examples of translated texts to illustrate the rules.

### 4.3 Vocabulary

Exhaustive lists to feed the library directly:

- **stop-words**: adverbs, prepositions, conjunctions, pronouns, the article, etc.
- **affixes**: gender, number, tense, and the derivational prefixes/suffixes listed in §4.2.
- **most common roots**.

### 4.4 Resources

Explanation of resources to learn Esperanto: books, courses, websites, etc.
References to pages, texts, books and other materials.
