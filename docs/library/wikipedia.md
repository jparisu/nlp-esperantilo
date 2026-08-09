# Reading Wikipedia

An NLP library is useless without text to run it on. `esperantilo` fetches that
text from Wikipedia with [`WikiPage`](api.md#esperantilo.wiki.WikiPage), already
stripped of wiki markup.

```python
from esperantilo import WikiPage

page = WikiPage.look_up("Esperanto", language="eo")

page.title          # 'Esperanto'
page.qid            # 'Q143'
len(page)           # number of sections
```

## Titles, concepts and languages

An article exists once per language, and the same *concept* is a different page
in each one: `Parsley`, `Perejil` and `Petroselo` are three articles about one
plant. What ties them together is the **QID**, the identifier Wikidata gives to
the concept itself — parsley is `Q26980`, in every language.

`look_up` uses that. It resolves the title to a concept, then reads the article
for it, so the language you *search* in and the language you *read* in do not
have to be the same:

```python
WikiPage.look_up("Perejil", language="eo").title
# 'Petroselo'
```

The title is looked for in `language` first, then in each of
`fallback_languages`, and redirects are followed. The article comes back in
`language` if that wiki has one, or in the first fallback that does — so check
`page.language`, which may not be the code you asked for.

If no listed language knows the title, `any_language=True` (the default) falls
back to searching Wikidata across every language. That step is a *search*, not a
lookup: it finds something for almost any plausible word, and what it finds is
not necessarily what you meant. Pass `any_language=False` to get a `ValueError`
instead of a guess.

## Sections

The body is a mapping of heading to text, in the order the article presents
them. Only top-level headings open a section; deeper ones stay inside the text
of the section they belong to. Wikipedia leaves the lead untitled, so it is
keyed by the title of the article.

```python
page.section_names          # ['Esperanto', 'Historio', 'Gramatiko', …]
page.section("historio")    # matched ignoring case
page["Historio"]            # the same thing
"Historio" in page          # True
page.full_text()            # every section, headings included
```

## What can go wrong

| Situation | What happens |
| --- | --- |
| No listed language knows the title | `ValueError` |
| The concept has no article in any listed language | `ValueError` |
| No section by that name | `KeyError` |
| No connection, a timeout, an API error | `requests.RequestException` |

`ValueError` means "the page is not there". Anything network-shaped surfaces as
a `requests` exception instead, so the two can be caught apart.

Each lookup costs between one and eight HTTP requests, depending on how many
languages have to be tried. Nothing is cached: calling `look_up` twice with the
same arguments fetches everything twice.

## Licensing

Wikipedia text is **CC BY-SA**. If you republish what you fetch, keep the
attribution and the licence; `page.url` is the link to credit.

## Languages

Here is a list of some of the most used languages, with their Wikipedia codes:

| Language | Code |
| --- | --- |
| Esperanto | `eo` |
| English | `en` |
| Spanish | `es` |
| French | `fr` |
| German | `de` |
| ... | ... |

The full list of codes is in
[Wikipedia:List of ISO 639 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).

## See also

- [API reference](api.md#esperantilo.wiki.WikiPage) — the generated signature,
  arguments and examples.
- [`resources/notebooks/wikipedia.ipynb`](https://github.com/jparisu/nlp-esperantilo/blob/main/resources/notebooks/wikipedia.ipynb)
  — a ready-to-run notebook for Google Colab.
- [Sentence segmentation](sentence-segmentation.md) — the obvious next step for
  the text you just fetched.
