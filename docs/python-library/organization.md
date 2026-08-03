# Organization

!!! note "Under construction"
    Planned contents are listed below.

## Recommended layout

The `src/` layout used by this repository:

```text
nlp-esperantilo/
├── pyproject.toml
├── requirements.txt
├── README.md
├── LICENSE
├── mkdocs.yml
├── docs/
├── src/
│   └── esperantilo/
│       └── __init__.py
└── tests/
    └── test_package.py
```

## The files that matter

- **`pyproject.toml`** — the project metadata and the build configuration:
  name, version, dependencies, optional extras and tool settings.
- **`requirements.txt`** — the dependency list, and how it differs from the
  dependencies declared in `pyproject.toml`.
- **`__init__.py`** — what makes a directory a package, and what belongs in it.
- **`src/`** — why keeping the code out of the repository root avoids importing
  the wrong copy.
- **`tests/`** — mirroring the source layout.

## Versioning

Where the version lives and how to bump it.
