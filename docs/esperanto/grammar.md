# Grammar

!!! note "Under construction"
    Planned contents are listed below. This page must end up containing **all**
    the regular rules needed to implement the rule-based library: tokenizer,
    lemmatizer, POS tagger and stop-word handling.

## Alphabet

The 28 letters, including the six diacritics `ĉ`, `ĝ`, `ĥ`, `ĵ`, `ŝ`, `ŭ`, and
what they imply for tokenization and text encoding (Unicode, the `x`- and
`h`-systems).

## Word-class endings

The core of POS tagging and lemmatization.

| Ending | Word class |
| --- | --- |
| `-o` | noun |
| `-a` | adjective |
| `-e` | adverb |
| `-i` | verb (infinitive) |

## Grammatical inflections

| Ending | Meaning |
| --- | --- |
| `-j` | plural |
| `-n` | accusative |
| `-jn` | plural accusative |

## Verb system

| Ending | Tense or mood |
| --- | --- |
| `-as` | present |
| `-is` | past |
| `-os` | future |
| `-us` | conditional |
| `-u` | imperative / volitive |
| `-i` | infinitive |

## The article

`la`, invariable. There is no indefinite article.

## Personal pronouns

`mi`, `vi`, `li`, `ŝi`, `ĝi`, `ni`, `ili`, `oni`, `si` — plus their possessive
and accusative forms.

## Correlatives

The full 5 × 9 table: the prefixes `ki-`, `ti-`, `i-`, `ĉi-`, `neni-` combined
with the endings `-o`, `-u`, `-a`, `-e`, `-es`, `-am`, `-al`, `-el`, `-om`.

## Affixes

Essential for lemmatization.

- **Prefixes**: `mal-`, `ge-`, `ek-`, `re-`, `dis-`, `mis-`, `bo-`, `pra-`.
- **Suffixes**: `-in-`, `-ist-`, `-ej-`, `-il-`, `-ar-`, `-et-`, `-eg-`,
  `-ul-`, `-an-`, `-ec-`, `-ig-`, `-iĝ-`, `-ind-`, `-em-`, `-aĉ-`.

## Numbers and compounding

Cardinal and ordinal numbers, and the rules for building compound words.

## Worked examples

Short translated texts that illustrate the rules above, annotated word by word.
