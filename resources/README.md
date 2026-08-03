# Resources

Machine-readable word lists. These files are the single source of truth for the
linguistic data of the project: the library reads them at runtime, and the
documentation renders them as pages at build time
(see [`hooks/word_lists.py`](../hooks/word_lists.py)).

Adding a new list — for example `prepozicioj.json` — is enough for a new
documentation page to appear under *Esperanto → Word lists*. No page has to be
written and no navigation entry has to be added.

## Available lists

| File | Contents |
| --- | --- |
| `ignorindaj-vortoj.json` | Stop-words: the high-frequency, low-content words a pipeline usually filters out. |

## Schema

Field names are in Esperanto, matching the file names. Translatable fields are
objects keyed by [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
locale.

```jsonc
{
  "id": "ignorindaj-vortoj",       // identifier; also the URL of the generated page
  "titolo": { "eo": "…", "en": "…" },
  "priskribo": { "eo": "…", "en": "…" },
  "lingvo": "eo",                  // language the words belong to
  "tradukoj": ["en"],              // locales available in the "traduko" field
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
  "kategorioj": {                  // grammatical categories used by the words
    "prepozicio": { "en": "Preposition" }
  },
  "vortoj": [
    {
      "vorto": "kun",              // the word itself, lowercase
      "kategorio": "prepozicio",   // a key of "kategorioj"
      "traduko": { "en": ["with"] },
      "noto": "…",                 // optional
      "fontoj": ["stopwords-iso"]  // optional; ids from the top-level "fontoj"
    }
  ]
}
```

Only `id`, `titolo` and `vortoj` are mandatory; the documentation build fails if
one of them is missing. Files are UTF-8 and keep the Esperanto diacritics
(`ĉ`, `ĝ`, `ĥ`, `ĵ`, `ŝ`, `ŭ`) as-is, never the `x`-system.

## Using a list

```python
import json
from pathlib import Path

data = json.loads(Path("resources/ignorindaj-vortoj.json").read_text(encoding="utf-8"))
stop_words = {entry["vorto"] for entry in data["vortoj"]}
```

`tests/test_resources.py` validates every file in this directory against the
schema above, so a malformed edit is caught by CI.
