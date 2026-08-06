# Vocabulary

Where [Grammar](grammar.md) gives the *rules*, this page gives the **lists** —
the concrete data the library will load: the stop-words, the full affix
inventory, and a starter set of common roots. The lists here are meant to be
copied straight into the library's resources.

## Stop-words

**Stop-words** are high-frequency words that carry little meaning on their own —
the article, prepositions, conjunctions, pronouns, correlatives and common
adverbs. An NLP pipeline usually filters them out before analysis, so that
`la`, `de`, `kaj` and `mi` do not drown out the content words.

Esperanto stop-words are easy to enumerate because most belong to the small,
closed classes described in [Grammar](grammar.md): the one article `la`, the
personal pronouns, the 45 correlatives, and a fixed set of prepositions and
conjunctions.

!!! abstract "The full list already exists as data"
    This project ships the complete list as a machine-readable file, rendered
    here automatically:

    **[Stop-words →](word-lists/ignorindaj-vortoj.md)** — 250 entries, each with
    its English translation, grammatical category and provenance. It is generated
    from `resources/ignorindaj-vortoj.json`, the same file the library will read
    at runtime, so the documentation and the data can never disagree.

A representative sample, by category:

| Category | Examples |
| --- | --- |
| Article | `la` |
| Prepositions | `al`, `de`, `en`, `kun`, `por`, `pri`, `sur`, `sub`, `tra` |
| Conjunctions | `kaj`, `aŭ`, `sed`, `ke`, `ĉar`, `se`, `nek` |
| Pronouns | `mi`, `vi`, `li`, `ŝi`, `ĝi`, `ni`, `ili`, `oni`, `si` |
| Correlatives | `tio`, `kiu`, `ĉiam`, `nenie`, `kiel`, … |
| Common adverbs | `ankaŭ`, `ankoraŭ`, `jam`, `nur`, `tre`, `tro`, `plu` |

The rest — *why* each word qualifies and where the entries come from — lives with
the [generated list](word-lists/ignorindaj-vortoj.md); this page only summarises.

## Affixes

The affixes are the most important vocabulary data for a **lemmatizer**: they let
it decompose a derived word back to its root. Below is the full inventory
introduced in [Grammar § Affixes](grammar.md#affixes), grouped by role and ready
to encode.

### Grammatical endings (inflectional)

These are stripped first, in reverse order, to reach the stem:

| Group | Endings |
| --- | --- |
| Word class | `-o` (noun), `-a` (adjective), `-e` (adverb), `-i` (verb inf.) |
| Number / case | `-j` (plural), `-n` (accusative), `-jn` (both) |
| Verb tense / mood | `-as`, `-is`, `-os`, `-us`, `-u`, `-i` |

### Derivational prefixes

| Prefix | Role | Example |
| --- | --- | --- |
| `mal-` | opposite | `malbona` (bad) |
| `ge-` | both sexes | `gepatroj` (parents) |
| `ek-` | sudden / inceptive | `ekiri` (to set off) |
| `re-` | again / back | `reveni` (to return) |
| `dis-` | scattering | `disdoni` (to distribute) |
| `mis-` | wrongly | `miskompreni` (to misunderstand) |
| `bo-` | in-law | `bopatro` (father-in-law) |
| `pra-` | primordial / great- | `praavo` (great-grandfather) |

### Derivational suffixes

| Suffix | Role | Example |
| --- | --- | --- |
| `-in-` | female | `patrino` (mother) |
| `-ist-` | professional | `instruisto` (teacher) |
| `-ej-` | place | `lernejo` (school) |
| `-il-` | tool | `tranĉilo` (knife) |
| `-ar-` | collection | `arbaro` (forest) |
| `-et-` | diminutive | `dometo` (cottage) |
| `-eg-` | augmentative | `domego` (mansion) |
| `-ul-` | person | `junulo` (youth) |
| `-an-` | member | `urbano` (citizen) |
| `-ec-` | abstract quality | `boneco` (goodness) |
| `-ig-` | to make / cause | `grandigi` (to enlarge) |
| `-iĝ-` | to become | `ruĝiĝi` (to blush) |
| `-ind-` | worthy of | `aminda` (lovable) |
| `-em-` | inclined to | `laborema` (hardworking) |
| `-aĉ-` | pejorative | `domaĉo` (hovel) |

!!! tip "Order of stripping for lemmatization"
    To recover the root of a word like `malsanulejojn`, peel from the outside
    in: `-n` → `-j` → `-o` (endings), then `-ej-`, `-ul-` (suffixes), then the
    `mal-` prefix, leaving `san-` ("health"). Each step is a table lookup.

## Most common roots

A lemmatizer also benefits from a list of known **roots**, both to validate a
decomposition and to catch the frequent words that appear everywhere. A starter
set of very common roots, by class:

=== "Verbs"

    | Root | Meaning | | Root | Meaning |
    | --- | --- | --- | --- | --- |
    | `est-` | to be | | `pov-` | to be able |
    | `hav-` | to have | | `vol-` | to want |
    | `far-` | to do / make | | `dev-` | must |
    | `ir-` | to go | | `sci-` | to know (facts) |
    | `ven-` | to come | | `pens-` | to think |
    | `vid-` | to see | | `dir-` | to say |
    | `don-` | to give | | `pren-` | to take |
    | `leg-` | to read | | `skrib-` | to write |
    | `manĝ-` | to eat | | `labor-` | to work |
    | `am-` | to love | | `help-` | to help |

=== "Nouns"

    | Root | Meaning | | Root | Meaning |
    | --- | --- | --- | --- | --- |
    | `hom-` | human | | `mond-` | world |
    | `vir-` | man | | `temp-` | time |
    | `infan-` | child | | `tag-` | day |
    | `dom-` | house | | `jar-` | year |
    | `urb-` | city | | `akv-` | water |
    | `land-` | country | | `lum-` | light |

=== "Adjectives"

    | Root | Meaning | | Root | Meaning |
    | --- | --- | --- | --- | --- |
    | `bon-` | good | | `bel-` | beautiful |
    | `grand-` | big | | `long-` | long |
    | `nov-` | new | | `alt-` | high / tall |

This is only a seed. A production list is best derived by frequency from a
[corpus](resources.md#corpora); the point here is that roots, like everything
else in Esperanto, are a finite list the library can hold in a file.

## Format

All of these lists are stored the same way, as **JSON files under `resources/`**,
so that a single source of truth can feed both the code (at runtime) and the
documentation (at build time, via
[`hooks/word_lists.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/hooks/word_lists.py)).
Field names are in Esperanto, matching the file names; translatable fields are
objects keyed by locale:

```jsonc
{
  "id": "ignorindaj-vortoj",          // also the URL of the generated page
  "titolo": { "eo": "Ignorindaj vortoj", "en": "Stop-words" },
  "lingvo": "eo",
  "tradukoj": ["en"],                 // locales present in "traduko"
  "kategorioj": {                     // grammatical categories used below
    "prepozicio": { "en": "Preposition" }
  },
  "vortoj": [
    {
      "vorto": "kun",                 // the word, lowercase
      "kategorio": "prepozicio",      // a key of "kategorioj"
      "traduko": { "en": ["with"] },
      "fontoj": ["stopwords-iso"]     // provenance, optional
    }
  ]
}
```

The documentation build only requires `id`, `titolo` and `vortoj`, but
[`tests/test_resources.py`](../python-library/testing.md#the-tests-structure) is
stricter: `id` must equal the file name, and every `vorto` must be lowercase,
unique, carry a `traduko` and use a `kategorio` declared in `kategorioj`. Files
are UTF-8 and keep the real diacritics (`ĉ ĝ ĥ ĵ ŝ ŭ`), never the x-system. A
malformed edit therefore fails in CI rather than in a documentation build. The
full schema is documented in `resources/README.md`.

Using a list from the library is then a two-liner:

```python
import json
from pathlib import Path

data = json.loads(Path("resources/ignorindaj-vortoj.json").read_text(encoding="utf-8"))
stop_words = {entry["vorto"] for entry in data["vortoj"]}
```

## Where to go next

- [Word lists](word-lists/index.md) — the generated data pages.
- [Resources](resources.md) — dictionaries and corpora to expand these lists.
