# Resources

Everything the project ships that is not code, in two directories:

| Directory | What it holds |
| --- | --- |
| [`esperanto/`](esperanto/) | The linguistic data: the lexicon, the list definitions, and reference texts under `books/`. |
| [`notebooks/`](notebooks/) | Notebooks meant to be opened in Google Colab. |

## `esperanto/`

The linguistic data of the project, and the single source of truth for it: the
documentation renders these files as pages at build time (see
[`docs/hooks/word_lists.py`](../docs/hooks/word_lists.py)), and the library will read the
same files at runtime once it grows past its current skeleton.

Two files, with different jobs:

| File | What it holds |
| --- | --- |
| `vortoj.json` | The **lexicon**: every word exactly once. |
| `listoj.json` | The **lists**: each one a filter over the lexicon. |

`books/` holds verbatim public-domain texts. They are cited by the guide but read
by no code, and the spell checker skips them — see `[tool.codespell]` in
[`pyproject.toml`](../pyproject.toml).

### Why two files

Many words belong to several lists. Every preposition is also a stop-word; so
are most correlatives and most numerals. With one file per list, `kun` would be
written twice, with two copies of its translation and its note, free to drift
apart.

Instead the word is stored once, tagged, and each list selects from the lexicon:

```jsonc
// vortoj.json — the word, once
{ "vorto": "kun", "kategorio": "prepozicio", "traduko": ["with"], "ignorinda": true }
```

```jsonc
// listoj.json — two lists, both of which show it
{ "id": "ignorindaj-vortoj", "filtro": { "ignorinda": true } }
{ "id": "prepozicioj",       "filtro": { "kategorio": "prepozicio" } }
```

Adding a list is one entry in `listoj.json`: its page and its navigation entry
appear on the next build, with no page to write.

!!! note
    The data is **English only**. The generated pages say so, and are not
    translated into the other languages of the site.

### `vortoj.json`

Field names are in Esperanto, matching the language the words belong to.

```jsonc
{
  "lingvo": "eo",                  // language of the words
  "licenco": "Apache-2.0",
  "fontoj": [                      // where the data comes from
    {
      "id": "stopwords-iso",       // referenced by each word's "fontoj"
      "nomo": "stopwords-iso/stopwords-eo",
      "url": "https://github.com/stopwords-iso/stopwords-eo",
      "licenco": "MIT",
      "noto": "…"
    }
  ],
  "kategorioj": {                  // grammatical categories, with English labels
    "prepozicio": "Preposition"
  },
  "vortoj": [
    {
      "vorto": "kun",              // the word itself, lowercase, unique
      "kategorio": "prepozicio",   // a key of "kategorioj"
      "traduko": ["with"],         // English glosses
      "noto": "…",                 // optional
      "fontoj": ["stopwords-iso"], // ids from the top-level "fontoj"
      "ignorinda": true            // is it a stop-word?
    }
  ]
}
```

### `listoj.json`

An array of list definitions:

```jsonc
[
  {
    "id": "prepozicioj",           // identifier; also the URL of the page
    "titolo": "Prepositions",
    "priskribo": "…",
    "filtro": { "kategorio": "prepozicio" }   // every key must match
  }
]
```

A `filtro` is a plain equality test: a word is in the list when **all** its keys
match the word's fields. `{"kategorio": "nombro", "ignorinda": true}` selects the
numerals that are also stop-words.

### What is enforced

The documentation build fails if the lexicon lacks `kategorioj` or `vortoj`, if
a list lacks `id`, `titolo` or `filtro`, or if a filter matches no word.

[`tests/test_resources.py`](../tests/test_resources.py) enforces more: every word
is lowercase and appears only once, has a non-empty `traduko`, a `kategorio` that
exists and an `ignorinda` flag; every source it cites is declared; every list id
is unique and filters on a field that words actually have.

Files are UTF-8 and keep the Esperanto diacritics (`ĉ ĝ ĥ ĵ ŝ ŭ`).

## `notebooks/`

| Notebook | What it does |
| --- | --- |
| [`wikipedia.ipynb`](notebooks/wikipedia.ipynb) | Installs the library from GitHub, asks for a page title and a language, and shows what `WikiPage` returns: metadata, section list, one section, and the full plain text. |

These are handed out to students rather than run by CI, so nothing in the test
suite executes them. They install the library from GitHub, so the `BRANCH`
constant in the first code cell decides which version is fetched.
