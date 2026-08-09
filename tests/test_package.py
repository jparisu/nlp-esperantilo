"""Tests for the package itself, as opposed to any single feature.

What is checked here is the *public API*: the promise that a given set of names
is importable straight from `esperantilo` and will stay that way. A test like
this one is what turns "the API" from a documentation claim into something CI
enforces.

The layout is checked too. The features live in subpackages, and each one
re-exports its own public names, so a name is reachable by two paths — the short
one users are meant to write and the long one it really lives at. Both are
promises, so both are tested.
"""

import importlib

import esperantilo

#: Every name the library promises to expose from its top-level module.
PUBLIC_API = {
    "__version__",
    "WikiPage",
    "sentence_tokenizer",
}

#: Each subpackage and the names it re-exports.
SUBPACKAGES = {
    "esperantilo.nlp": {"sentence_tokenizer"},
    "esperantilo.wiki": {"WikiPage"},
}

#: Where each public name is actually defined, as `__module__` reports it.
DEFINED_IN = {
    "WikiPage": "esperantilo.wiki.wiki",
    "sentence_tokenizer": "esperantilo.nlp.tokenizer",
}


def test_package_is_importable():
    assert esperantilo is not None


def test_version_is_exposed():
    assert isinstance(esperantilo.__version__, str)
    assert esperantilo.__version__


def test_all_declares_the_public_api():
    assert set(esperantilo.__all__) == PUBLIC_API


def test_every_public_name_is_actually_importable():
    for name in esperantilo.__all__:
        assert hasattr(esperantilo, name), f"{name} is in __all__ but not exported"


def test_every_subpackage_is_importable():
    """A subpackage without an `__init__.py` imports here but ships broken."""
    for name in SUBPACKAGES:
        assert importlib.import_module(name) is not None


def test_every_subpackage_re_exports_its_public_names():
    for name, exported in SUBPACKAGES.items():
        module = importlib.import_module(name)
        assert set(module.__all__) == exported
        for public_name in exported:
            assert hasattr(module, public_name)


def test_the_short_and_the_long_path_give_the_same_object():
    for name, exported in SUBPACKAGES.items():
        module = importlib.import_module(name)
        for public_name in exported:
            assert getattr(module, public_name) is getattr(esperantilo, public_name)


def test_public_names_live_where_the_documentation_says():
    for name, module_name in DEFINED_IN.items():
        assert getattr(esperantilo, name).__module__ == module_name
