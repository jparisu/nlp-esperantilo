# Esperanto

This section covers the Esperanto language itself — its history, grammar,
vocabulary and learning resources. It is strongly oriented towards the
linguistics and the regular rules of Esperanto, so that a rule-based NLP
library can be implemented from it.

The pages are ordered from context to data: the story of the language, then its
rules, then the lists those rules produce. If you only need the linguistic data
for the library, jump to [Grammar](grammar.md) and [Vocabulary](vocabulary.md).

<div class="grid cards" markdown>

- [**1. History**](history.md) — creator, motivation and evolution.
- [**2. Grammar**](grammar.md) — the regular rules the library encodes.
- [**3. Vocabulary**](vocabulary.md) — stop-words, affixes and common roots.
- [**4. Resources**](resources.md) — books, courses and websites.
- [**FAQ**](esperanto-faq.md) — quick answers to common doubts.
- [**Word lists**](word-lists/index.md) — the data the library actually reads.

</div>

## Word lists

The reference lists live as JSON files under `resources/` in the repository and
are rendered here automatically, so the documentation and the data the library
loads can never disagree:

- [Stop-words](word-lists/ignorindaj-vortoj.md) — 250 words with their English
  translation and grammatical category.

See [all word lists](word-lists/index.md).
