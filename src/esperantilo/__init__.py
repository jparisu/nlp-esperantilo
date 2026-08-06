"""Esperantilo: a rule-based Natural Language Processing library for Esperanto.

This module is the **public API** of the library: everything a user is meant to
touch is importable straight from it.

```python
import esperantilo

esperantilo.sentence_tokenizer("Mi lernas Esperanton. Ĝi estas facila.")
```

The library is deliberately incomplete — it currently ships sentence
segmentation and nothing else. Full documentation is at
<https://jparisu.github.io/nlp-esperantilo/>.
"""

from esperantilo.tokenizer import sentence_tokenizer

__version__ = "0.1.0"
"""The installed version of the library, as declared in `pyproject.toml`."""

#: Everything the library promises to keep stable. Names not listed here are
#: implementation details and may change without notice.
__all__ = [
    "__version__",
    "sentence_tokenizer",
]
