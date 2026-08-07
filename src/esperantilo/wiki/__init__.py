"""Reading Wikipedia articles as plain text, in any language.

Where the text comes from, as opposed to what is done with it afterwards —
that half is [`esperantilo.nlp`][esperantilo.nlp].

The whole feature is one class, [`WikiPage`][esperantilo.wiki.WikiPage], and it
knows how to fetch itself:

```python
from esperantilo import WikiPage

page = WikiPage.look_up("Perejil", language="eo")
print(page.title)               # Petroselo
print(page.section("Uzoj"))
```

How the article is found — which APIs are called, in which order, and what
happens when a language does not have it — is the business of the private
`esperantilo.wiki._wiki_api` module, not of anyone using this one.
"""

from esperantilo.wiki.wiki import WikiPage

#: Everything this subpackage promises to keep stable.
__all__ = ["WikiPage"]
