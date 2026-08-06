# Grammar

This is the core reference page of the Esperanto section. It collects the rules a
rule-based pipeline needs — for the tokenizer, the lemmatizer, the POS tagger and
stop-word handling. Because Esperanto's morphology has no exceptions, each rule
below can be turned almost directly into code.

The guiding idea: an Esperanto word is built from a **root** plus **grammatical
endings** and optional **affixes**. Strip the endings and affixes and you have
the lemma; read the endings and you have the part of speech and the inflection.

!!! note "What this page leaves out"
    The **participles** (`-ant-`, `-int-`, `-ont-` active; `-at-`, `-it-`, `-ot-`
    passive), the compound tenses built from them with `esti`, and the passive
    voice are just as regular, but they are not covered here. A pipeline that
    implements only the rules below will mis-analyse forms like `leganta`,
    `legita` or `estas legata`.

!!! quote "Reference"
    The rules and examples on this page follow the classic **_A Complete Grammar
    of Esperanto_** by Ivy Kellerman Reed (1910), a public-domain work included
    in the repository at `resources/books/esperanto_grammar.txt`. See
    [Resources § Books](resources.md#books) for the full citation.

## Alphabet

Esperanto uses a **28-letter** Latin alphabet. It is strictly **phonetic**: every
letter is always pronounced the same way, and every sound is written with exactly
one letter. Six letters carry diacritics: the five circumflexed consonants are
used by no other language, and `ŭ` also appears in the Belarusian Latin alphabet.

| Letter | Name | Sound (approx.) |
| --- | --- | --- |
| `ĉ` | ĉo | *ch* in "church" |
| `ĝ` | ĝo | *g* in "gem" |
| `ĥ` | ĥo | *ch* in Scottish "loch" |
| `ĵ` | ĵo | *s* in "measure" |
| `ŝ` | ŝo | *sh* in "ship" |
| `ŭ` | ŭo | *w* in "how" (used in diphthongs) |

The letters `q`, `w`, `x`, `y` are **not** part of the alphabet.

!!! warning "Encoding matters for tokenization"
    The diacritics are real Unicode letters (`ĉ` is U+0109), not `c` plus a
    combining mark — but text found in the wild may use either form. Two ASCII
    fallbacks also exist for keyboards that cannot type the diacritics:

    - the **x-system**: `cx gx hx jx sx ux` for `ĉ ĝ ĥ ĵ ŝ ŭ`;
    - the **h-system** (from the *Fundamento*): `ch gh hh jh sh u`.

    A robust tokenizer should **normalise** input to a single canonical form
    (Unicode NFC, real diacritics) before applying any other rule. This
    project's data files keep the real diacritics and never the x-system (see
    [Vocabulary § Format](vocabulary.md#format)).

## Word-class endings

This is the single most useful rule for POS tagging and lemmatization: the
**final vowel of a full word marks its part of speech**.

| Ending | Word class | Example | Root | Meaning |
| --- | --- | --- | --- | --- |
| `-o` | noun | `libro` | `libr-` | book |
| `-a` | adjective | `bona` | `bon-` | good |
| `-e` | adverb (derived) | `rapide` | `rapid-` | quickly |
| `-i` | verb (infinitive) | `kanti` | `kant-` | to sing |

From one root you get the whole family: `muziko` (music), `muzika` (musical),
`muzike` (musically). To **lemmatize**, strip the grammatical ending (and any
inflection below) to recover the root, then re-attach the class vowel to get the
dictionary form.

## Grammatical inflections

Nouns and adjectives take two optional endings, always **after** the class vowel:

| Ending | Meaning | Example |
| --- | --- | --- |
| `-j` | plural | `libroj` (books), `bonaj` (good, pl.) |
| `-n` | accusative (direct object) | `libron`, `bonan` |
| `-jn` | plural **and** accusative | `bonajn librojn` |

Two rules make these fully regular:

- **Adjectives agree** with their noun in both number and case: *"la bonaj
  libroj"*, *"mi legas interesajn librojn"*.
- The order is fixed: root → class vowel → `-j` → `-n`. So the parse of
  `librojn` is `libr-` + `-o` (noun) + `-j` (plural) + `-n` (accusative).

The accusative also marks direction of motion, but for morphological analysis the
`-n` suffix is what matters.

## Verb system

Verbs do **not** conjugate for person or number — only for tense and mood, with a
single ending each. The same root takes any of these:

| Ending | Tense / mood | Example (`kant-`, sing) |
| --- | --- | --- |
| `-as` | present | `kantas` (sing / sings) |
| `-is` | past | `kantis` (sang) |
| `-os` | future | `kantos` (will sing) |
| `-us` | conditional | `kantus` (would sing) |
| `-u` | imperative / volitive | `kantu!` (sing!) |
| `-i` | infinitive | `kanti` (to sing) |

`mi kantas`, `vi kantas`, `ili kantas` — the verb never changes for the subject.
To lemmatize a verb, replace its tense/mood ending with `-i` (`kantis → kanti`).

## The article

There is **one** article, the definite `la` ("the"). It is **invariable** — no
plural, no gender, no case:

- `la libro` (the book), `la libroj` (the books), `la bona libro` (the good book).

There is **no indefinite article**: `libro` means both "a book" and simply
"book". `la` is a natural stop-word (see [Vocabulary](vocabulary.md#stop-words)).

## Personal pronouns

The pronouns are a small, closed set — ideal to hard-code:

| Pronoun | Meaning | Possessive (`+ -a`) |
| --- | --- | --- |
| `mi` | I | `mia` |
| `vi` | you (sg. & pl.) | `via` |
| `li` | he | `lia` |
| `ŝi` | she | `ŝia` |
| `ĝi` | it | `ĝia` |
| `ni` | we | `nia` |
| `ili` | they | `ilia` |
| `oni` | one / people (impersonal) | `onia` |
| `si` | reflexive (himself/herself/itself/themselves) | `sia` |

The **accusative** of a pronoun adds `-n`: `min` (me), `vin`, `lin`, `ŝin`, `nin`,
`ilin`. The possessives are ordinary adjectives, so they also inflect: `miajn
librojn` (my books, acc. pl.).

## Correlatives

The **correlatives** are a strikingly regular 5 × 9 grid of 45 common words
(this/that/which/some/every/no + thing/person/place/time/reason…). Each is a
**prefix** (the meaning category) plus an **ending** (the type). Learn the grid
and you get all 45 for free.

The five prefixes:

| Prefix | Meaning |
| --- | --- |
| `ki-` | interrogative / relative (*wh-*, "which") |
| `ti-` | demonstrative ("that") |
| `i-` | indefinite ("some") |
| `ĉi-` | universal ("every", "all") |
| `neni-` | negative ("no", "none") |

The nine endings and the full table:

| Ending → type | `ki-` | `ti-` | `i-` | `ĉi-` | `neni-` |
| --- | --- | --- | --- | --- | --- |
| `-o` thing | kio | tio | io | ĉio | nenio |
| `-u` individual | kiu | tiu | iu | ĉiu | neniu |
| `-a` kind | kia | tia | ia | ĉia | nenia |
| `-es` possession | kies | ties | ies | ĉies | nenies |
| `-e` place | kie | tie | ie | ĉie | nenie |
| `-am` time | kiam | tiam | iam | ĉiam | neniam |
| `-al` reason | kial | tial | ial | ĉial | nenial |
| `-el` manner | kiel | tiel | iel | ĉiel | neniel |
| `-om` quantity | kiom | tiom | iom | ĉiom | neniom |

The `-u` and `-a` correlatives take both `-j` and `-n` (`tiujn`, `kiuj`), like the
nouns and adjectives they resemble. The `-o` correlatives take `-n` but **never**
`-j` (`kion`, `tion` — there is no *tioj*), and the `-e` correlatives take `-n` to
mark direction (`tien`, `kien`). The other five endings are invariable. Most
correlatives are stop-words.

## Affixes

Affixes are what make Esperanto vocabulary **compositional** — and they are the
heart of lemmatization, because a long word is usually a root wrapped in
affixes. They attach *between* the root and the grammatical ending.

### Prefixes

| Prefix | Meaning | Example |
| --- | --- | --- |
| `mal-` | direct opposite | `bona` → `malbona` (good → bad) |
| `ge-` | both sexes together | `patro` → `gepatroj` (father → parents) |
| `ek-` | sudden start / brief action | `iri` → `ekiri` (to go → to set off) |
| `re-` | again / back | `veni` → `reveni` (to come → to return) |
| `dis-` | separation, scattering | `doni` → `disdoni` (to give → to distribute) |
| `mis-` | wrongly | `kompreni` → `miskompreni` (to misunderstand) |
| `bo-` | relation by marriage | `patro` → `bopatro` (father-in-law) |
| `pra-` | primordial / great- (kinship) | `avo` → `praavo` (great-grandfather) |

### Suffixes

| Suffix | Meaning | Example |
| --- | --- | --- |
| `-in-` | female | `patro` → `patrino` (father → mother) |
| `-ist-` | professional / adherent | `instrui` → `instruisto` (teacher) |
| `-ej-` | place for | `lerni` → `lernejo` (to learn → school) |
| `-il-` | tool / instrument | `tranĉi` → `tranĉilo` (to cut → knife) |
| `-ar-` | collection / set | `arbo` → `arbaro` (tree → forest) |
| `-et-` | diminutive (smaller) | `domo` → `dometo` (house → cottage) |
| `-eg-` | augmentative (bigger) | `domo` → `domego` (house → mansion) |
| `-ul-` | person characterised by | `juna` → `junulo` (young → youth) |
| `-an-` | member / inhabitant | `urbo` → `urbano` (city → citizen) |
| `-ec-` | abstract quality | `bona` → `boneco` (good → goodness) |
| `-ig-` | to make / cause | `granda` → `grandigi` (big → to enlarge) |
| `-iĝ-` | to become | `ruĝa` → `ruĝiĝi` (red → to blush) |
| `-ind-` | worthy of | `ami` → `aminda` (to love → lovable) |
| `-em-` | inclined to | `labori` → `laborema` (to work → hardworking) |
| `-aĉ-` | pejorative (bad quality) | `domo` → `domaĉo` (house → hovel) |

Affixes stack. `mal-san-ul-ej-o` = `mal-` (opposite) + `san-` (health) + `-ul-`
(person) + `-ej-` (place) + `-o` (noun) = **hospital** (literally "place for
unhealthy persons"). A lemmatizer that knows this affix table can decompose such
words by rule.

## Numbers and compounding

The cardinal numbers are built from a handful of roots:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 100 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `nul` | `unu` | `du` | `tri` | `kvar` | `kvin` | `ses` | `sep` | `ok` | `naŭ` | `dek` | `cent` | `mil` |

Larger numbers are **compounded** by juxtaposition: `dek du` (12), `dudek` (20),
`dudek unu` (21), `cent tridek kvin` (135). Adding endings derives related words:

- ordinals with `-a`: `unua` (first), `dua` (second);
- multiples with `-obl-`: `duobla` (double);
- fractions with `-on-`: `duono` (a half), `kvarono` (a quarter);
- collectives with `-op-`: `duope` (in twos).

More generally, **any two roots can compound** into one word, with the last root
as the head: `vapor-ŝipo` (steamship), `dorm-o-ĉambro` (bedroom, with a connecting
`-o-` for pronounceability). The compound's word class comes from its final
ending, exactly as for a single root.

## Worked examples

Putting the rules together, here is a sentence parsed word by word:

> **La juna instruistino legas interesan libron.**
> *"The young (female) teacher is reading an interesting book."*

| Word | Decomposition | Analysis |
| --- | --- | --- |
| `La` | `la` | article (stop-word) |
| `juna` | `jun-` + `-a` | adjective — "young" |
| `instruistino` | `instru-` + `-ist-` + `-in-` + `-o` | noun — "female teacher" |
| `legas` | `leg-` + `-as` | verb, present — "reads" (lemma `legi`) |
| `interesan` | `interes-` + `-a` + `-n` | adjective, accusative — "interesting" |
| `libron` | `libr-` + `-o` + `-n` | noun, accusative — "book" (lemma `libro`) |

A second example shows plural, accusative agreement and a correlative:

> **Ĉiuj miaj amikoj legas tiujn librojn.**
> *"All my friends are reading those books."*

`Ĉiuj` (correlative `ĉiu` + `-j`), `miaj` (possessive `mia` + `-j`), `amikoj`
(`amik-o-j`) — the subject is plural, so nothing takes `-n`; `tiujn librojn`
(`tiu-j-n`, `libr-o-j-n`) is the plural accusative object, and the demonstrative
agrees with its noun. This regular agreement is precisely what a rule-based
tagger can verify and exploit.

## Where to go next

- [Vocabulary](vocabulary.md) — the affix and stop-word lists in full, ready to
  feed the library.
- [Python Library § API](../python-library/api.md) — how these rules become a
  `Doc` / `Token` interface.
