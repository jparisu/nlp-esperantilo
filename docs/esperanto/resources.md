# Resources

A curated list of places to learn Esperanto, look words up, and find text to test
the library against. The entries are grouped by purpose; the ones marked
**in-repo** ship with this project.

## Courses

For learning the language from scratch:

- **[lernu.net](https://lernu.net)** — a free multilingual site with structured
  courses, grammar explanations and a dictionary. The most common starting point.
- **[Duolingo — Esperanto](https://www.duolingo.com/course/eo/en)** — a free,
  gamified course, good for building a daily habit and basic vocabulary.
- **[Kurso de Esperanto](https://www.kurso.com.br)** — a classic downloadable
  audio-visual course.

Because the grammar is so regular, most learners reach basic reading fluency far
faster than with a natural language — which is convenient when your goal is to
*verify a linguistic library* rather than to become a poet.

## Books

Reference grammars and readers:

- **_A Complete Grammar of Esperanto_**, Ivy Kellerman Reed (1910) — **in-repo**
  at `resources/books/esperanto_grammar.txt`. A public-domain, systematic grammar
  with graded exercises; it is the reference this section's
  [Grammar page](grammar.md) follows. Also available as
  [Project Gutenberg eBook #7787](https://www.gutenberg.org/ebooks/7787).
- **_Fundamento de Esperanto_**, L. L. Zamenhof (1905) — the official, unchangeable
  foundation of the language (the sixteen rules, the *Universala Vortaro* and
  model exercises). The ultimate authority on what is correct Esperanto.
- **_Plena Manlibro de Esperanta Gramatiko_** (PMEG) — a modern, exhaustive
  descriptive grammar in Esperanto, available free at
  [bertilow.com/pmeg](https://bertilow.com/pmeg/). The best deep reference once
  you read Esperanto comfortably.

## Dictionaries

For looking up roots, affixes and meanings:

- **[Reta Vortaro (ReVo)](https://www.reta-vortaro.de/)** — a free, community-built
  monolingual dictionary with translations into many languages, and downloadable
  in machine-readable form.
- **_Plena Ilustrita Vortaro_** (PIV) — the large monolingual dictionary of
  reference, published by SAT; the standard for authoritative definitions.
- **[Vortaro.net](https://vortaro.net)** — a convenient online front-end to PIV.

!!! tip "Machine-readable is what you want"
    For feeding the library, prefer sources that offer a **structured export**
    (ReVo's data files, word lists) over prose dictionaries. They can be
    converted into the JSON format described in
    [Vocabulary § Format](vocabulary.md#format).

## Corpora

Bodies of real Esperanto text, useful for measuring word frequencies and for
testing the tokenizer and lemmatizer on genuine input:

- **[Tekstaro de Esperanto](https://tekstaro.com)** — a searchable corpus of
  Esperanto texts (literature, periodicals, the *Fundamento*), the standard source
  for frequency data.
- **[Esperanto Wikipedia](https://eo.wikipedia.org)** — a large, freely downloadable
  body of contemporary text across many topics.
- **[Project Gutenberg — Esperanto](https://www.gutenberg.org/browse/languages/eo)**
  — public-domain books in Esperanto, including the grammar shipped in this repo.

!!! warning "Check the licence before redistributing text"
    A corpus is fine to *analyse*, but redistributing its text (for example,
    committing it into the repository) is only safe when its licence allows it.
    Public-domain sources like Project Gutenberg and the *Fundamento* are the
    safe default; Wikipedia text is CC BY-SA and must keep its attribution.

## Communities

Where the language is actually used, if you want to see it in the wild:

- **[Universala Esperanto-Asocio (UEA)](https://uea.org)** — the main international
  organisation, with links to national associations and events.
- **[Esperanto on Reddit](https://www.reddit.com/r/Esperanto/)** — an active,
  beginner-friendly English-language community.
- **Pasporta Servo, local clubs and the annual _Universala Kongreso_** — the
  offline community, for those who want to hear it spoken.

## Where to go next

- [History](history.md) — how the language and its community came to be.
- [Grammar](grammar.md) — the rules these resources describe, distilled for the
  library.
