"""Natural Language Processing over Esperanto text.

The rule-based half of the library: everything that takes text that is already
in hand and analyses it. Fetching the text in the first place is the job of
[`esperantilo.wiki`][esperantilo.wiki].

```python
from esperantilo import sentence_tokenizer

sentence_tokenizer("Mi lernas Esperanton. Ĝi estas facila.")
```

One feature so far, sentence segmentation. Tokens, lemmas and affix analysis are
still a design target — building them is the exercise the guide prepares you for.
"""

from esperantilo.nlp.tokenizer import sentence_tokenizer

#: Everything this subpackage promises to keep stable.
__all__ = ["sentence_tokenizer"]
