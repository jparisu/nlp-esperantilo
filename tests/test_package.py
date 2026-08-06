"""Tests for the package itself, as opposed to any single feature.

What is checked here is the *public API*: the promise that a given set of names
is importable straight from `esperantilo` and will stay that way. A test like
this one is what turns "the API" from a documentation claim into something CI
enforces.
"""

import esperantilo

#: Every name the library promises to expose from its top-level module.
PUBLIC_API = {
    "__version__",
    "sentence_tokenizer",
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
