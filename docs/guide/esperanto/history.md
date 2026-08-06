# History

Esperanto is a **constructed international auxiliary language**: a language
designed on purpose, rather than one that evolved naturally. Understanding *why*
it was built the way it was explains its most important property for this
project — its **regularity** — which is what makes a rule-based NLP library
feasible in the first place.

## Zamenhof and the *Unua Libro*

Esperanto was created by **L. L. Zamenhof** (1859–1917), an ophthalmologist from
**Białystok**, a town then in the Russian Empire and today in Poland. Białystok
was home to several communities — Poles, Russians, Germans, Jews — who spoke
different languages and often mistrusted one another. Zamenhof came to believe
that a shared, neutral second language could reduce that friction.

He published his project in **1887**, in a booklet whose Russian title translates
to *"International Language"*. He signed it with the pseudonym **Doktoro
Esperanto** — "Doctor One-Who-Hopes" — and the nickname became the name of the
language. That first booklet is known as the **_Unua Libro_** ("First Book"). It
contained the entire language in a tiny space: a preface, sixteen grammatical
rules, and a small dictionary of roots.

!!! quote "The idea behind the sixteen rules"
    The whole grammar fit on a few pages precisely because it has **no
    exceptions**. Every noun ends in `-o`, every present-tense verb in `-as`, and
    those rules never break. That is unusual for a natural language — and it is
    exactly the property a rule-based analyser relies on.

## Motivation

Zamenhof's goal was a language that was **easy to learn** and **neutral** — owned
by no nation. Three design choices followed directly from that goal, and all
three matter to us:

- **Regularity.** The grammar is fully systematic; there are no irregular verbs,
  no irregular plurals, no gendered exceptions to memorise.
- **Simplicity.** A small set of rules combines to express a lot. There is one
  definite article, one plural marker, one accusative marker.
- **Productive word-building.** A modest number of roots plus a set of prefixes
  and suffixes generate a large vocabulary by regular composition (see
  [Grammar § Affixes](grammar.md#affixes)).

For a computational linguist, this is close to ideal: a language whose morphology
can be described by rules that actually hold, rather than by long lists of
exceptions.

## Evolution

To keep the language stable as it spread, Zamenhof published the **_Fundamento de
Esperanto_** in **1905**; later that year the first World Esperanto Congress, in
Boulogne-sur-Mer, declared it the untouchable foundation of the language: its
grammar and core vocabulary could be built upon but not changed. This is why Esperanto
has stayed remarkably consistent for over a century — a text from 1905 is still
perfectly readable today.

Since then the language has grown a living community of speakers around the world,
its own literature (original and translated), periodicals, music and, more
recently, a strong online presence. Estimates of the number of speakers vary
widely, but Esperanto is by a large margin the most successful constructed
language ever created, and the only one with a community of native speakers who
grew up with it at home.

For where to actually learn it and read it, see [Resources](resources.md).

## Why it matters here

The history is not just background: it is the reason this project can be
*rule-based* at all. A language deliberately engineered for regularity can be
tokenized, lemmatized and POS-tagged with hand-written rules to a degree that
would be hopeless for, say, English. The next page turns that regularity into the
concrete rules the library encodes.

## Where to go next

- [Grammar](grammar.md) — the regular rules the library implements.
