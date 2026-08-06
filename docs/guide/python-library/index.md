# Python Library

This section explains how to build a Python library: how to organize it, how to
design its API, how to test it, and how to install and use it. The running
example is `esperantilo`, the very package this project ships.

The pages build on each other — layout, then installation, then the API design,
then testing — but each stands on its own if you already know the basics.

<div class="grid cards" markdown>

- [**1. What is a library**](library.md) — packages, modules and distributions.
- [**2. Organization**](organization.md) — `pyproject.toml`, `src/`, `tests/`.
- [**3. Installation and usage**](installation-and-usage.md) — from GitHub, in a notebook.
- [**4. API**](api.md) — designing a clear public interface, spaCy-style.
- [**5. Testing**](testing.md) — `pytest` and continuous integration.
- [**FAQ**](python-faq.md) — quick answers to common doubts.

</div>

!!! tip "See the result"
    Every technique on these pages is applied in this repository. The
    [Library](../../library/index.md) section is the outcome: the reference
    manual of `esperantilo`, with an
    [API reference](../../library/api.md) generated from the very docstrings
    this section teaches you to write.
