"""Esperantilo: a rule-based Natural Language Processing library for Esperanto.

This module is the **public API** of the library: everything a user is meant to
touch is importable straight from it, whichever subpackage it actually lives in.

```python
import esperantilo

page = esperantilo.WikiPage.look_up("Esperanto", language="eo")
esperantilo.sentence_tokenizer(page.section(page.title))
```

Two subpackages, split by what they do to text:

| Subpackage | What it does |
| --- | --- |
| [`esperantilo.wiki`][esperantilo.wiki] | Fetches text: Wikipedia articles, as plain text, in any language. |
| [`esperantilo.nlp`][esperantilo.nlp] | Analyses text that is already in hand. |

The library is deliberately incomplete — it currently ships sentence
segmentation and a Wikipedia reader, and nothing else. Full documentation is at
<https://jparisu.github.io/nlp-esperantilo/>.
"""

from esperantilo.nlp import sentence_tokenizer
from esperantilo.wiki import WikiPage

__version__ = "0.1.0"
"""The installed version of the library, as declared in `pyproject.toml`."""

#: Everything the library promises to keep stable. Names not listed here are
#: implementation details and may change without notice.
__all__ = [
    "__version__",
    "WikiPage",
    "sentence_tokenizer",
]
