# Vortprovizo

Kie [Gramatiko](grammar.md) donas la *regulojn*, ĉi tiu paĝo donas la **listojn** — la
konkretajn datumojn, kiujn ŝargos la biblioteko: la ignorindajn vortojn, la plenan
afiksan inventaron, kaj komencan aron da oftaj radikoj. La listoj ĉi tie estas pensitaj
por esti kopiitaj rekte en la rimedojn de la biblioteko.

## Ignorindaj vortoj

**Ignorindaj vortoj** (angle *stop-words*) estas oftaj vortoj, kiuj per si mem portas
malmultan signifon — la artikolo, prepozicioj, konjunkcioj, pronomoj, korelativoj kaj
oftaj adverboj. NLP-prilabora ĉeno kutime filtras ilin antaŭ la analizo, por ke `la`,
`de`, `kaj` kaj `mi` ne dronigu la enhavajn vortojn.

La Esperantaj ignorindaj vortoj estas facile listigeblaj, ĉar la plimulto apartenas al
la malgrandaj, fermitaj klasoj priskribitaj en [Gramatiko](grammar.md): la sola artikolo
`la`, la personaj pronomoj, la 45 korelativoj, kaj fiksa aro da prepozicioj kaj
konjunkcioj.

!!! abstract "La plena listo jam ekzistas kiel datumoj"
    Ĉi tiu projekto distribuas la plenan liston kiel maŝinlegeblan dosieron,
    prezentatan ĉi tie aŭtomate:

    **[Ignorindaj vortoj →](word-lists/ignorindaj-vortoj.md)** — 250 eroj, ĉiu kun sia
    angla traduko, gramatika kategorio kaj deveno. Ĝi estas generita el
    `resources/esperanto/vortoj.json`, la sama dosiero kiun legos la biblioteko
    rultempe, por ke la dokumentaro kaj la datumoj neniam povu malkonsenti.

Reprezenta specimeno, laŭ kategorio:

| Kategorio | Ekzemploj |
| --- | --- |
| Artikolo | `la` |
| Prepozicioj | `al`, `de`, `en`, `kun`, `por`, `pri`, `sur`, `sub`, `tra` |
| Konjunkcioj | `kaj`, `aŭ`, `sed`, `ke`, `ĉar`, `se`, `nek` |
| Pronomoj | `mi`, `vi`, `li`, `ŝi`, `ĝi`, `ni`, `ili`, `oni`, `si` |
| Korelativoj | `tio`, `kiu`, `ĉiam`, `nenie`, `kiel`, … |
| Oftaj adverboj | `ankaŭ`, `ankoraŭ`, `jam`, `nur`, `tre`, `tro`, `plu` |

La cetero — *kial* ĉiu vorto kvalifikiĝas kaj de kie venas la eroj — vivas kun la
[generita listo](word-lists/ignorindaj-vortoj.md); ĉi tiu paĝo nur resumas.

## Afiksoj

La afiksoj estas la plej gravaj vortprovizaj datumoj por **lematizilo**: ili ebligas al
ĝi malkomponi derivitan vorton reen al ĝia radiko. Sube estas la plena inventaro
prezentita en [Gramatiko § Afiksoj](grammar.md#afiksoj), grupigita laŭ rolo kaj preta
por kodigi.

### Gramatikaj finaĵoj (fleksiaj)

Ĉi tiuj estas forigataj unue, en inversa ordo, por atingi la trunkon:

| Grupo | Finaĵoj |
| --- | --- |
| Vortklaso | `-o` (subst.), `-a` (adj.), `-e` (adv.), `-i` (verbo inf.) |
| Nombro / kazo | `-j` (pluralo), `-n` (akuzativo), `-jn` (ambaŭ) |
| Verba tempo / modo | `-as`, `-is`, `-os`, `-us`, `-u`, `-i` |

### Derivaj prefiksoj

| Prefikso | Rolo | Ekzemplo |
| --- | --- | --- |
| `mal-` | malo | `malbona` |
| `ge-` | ambaŭ seksoj | `gepatroj` |
| `ek-` | subita / komenca | `ekiri` |
| `re-` | denove / reen | `reveni` |
| `dis-` | disĵeto | `disdoni` |
| `mis-` | erare | `miskompreni` |
| `bo-` | boparenceco | `bopatro` |
| `pra-` | pratempa / pra- | `praavo` |

### Derivaj sufiksoj

| Sufikso | Rolo | Ekzemplo |
| --- | --- | --- |
| `-in-` | ina | `patrino` |
| `-ist-` | profesiulo | `instruisto` |
| `-ej-` | loko | `lernejo` |
| `-il-` | ilo | `tranĉilo` |
| `-ar-` | kolekto | `arbaro` |
| `-et-` | malpligrandiga | `dometo` |
| `-eg-` | pligrandiga | `domego` |
| `-ul-` | persono | `junulo` |
| `-an-` | membro | `urbano` |
| `-ec-` | abstrakta eco | `boneco` |
| `-ig-` | igi / kaŭzi | `grandigi` |
| `-iĝ-` | iĝi | `ruĝiĝi` |
| `-ind-` | inda je | `aminda` |
| `-em-` | inklina al | `laborema` |
| `-aĉ-` | malestima | `domaĉo` |

!!! tip "Ordo de senŝeligo por la lematizado"
    Por reakiri la radikon de vorto kiel `malsanulejojn`, senŝeligu de ekstere
    internen: `-n` → `-j` → `-o` (finaĵoj), poste `-ej-`, `-ul-` (sufiksoj), poste la
    prefikso `mal-`, lasante `san-` ("sano"). Ĉiu paŝo estas serĉo en tabelo.

## Plej oftaj radikoj

Lematizilo ankaŭ profitas de listo de konataj **radikoj**, kaj por validigi
malkomponadon kaj por kapti la oftajn vortojn, kiuj aperas ĉie. Komenca aro da tre
oftaj radikoj, laŭ klaso:

=== "Verboj"

    | Radiko | Signifo | | Radiko | Signifo |
    | --- | --- | --- | --- | --- |
    | `est-` | esti | | `pov-` | povi |
    | `hav-` | havi | | `vol-` | voli |
    | `far-` | fari | | `dev-` | devi |
    | `ir-` | iri | | `sci-` | scii |
    | `ven-` | veni | | `pens-` | pensi |
    | `vid-` | vidi | | `dir-` | diri |
    | `don-` | doni | | `pren-` | preni |
    | `leg-` | legi | | `skrib-` | skribi |
    | `manĝ-` | manĝi | | `labor-` | labori |
    | `am-` | ami | | `help-` | helpi |

=== "Substantivoj"

    | Radiko | Signifo | | Radiko | Signifo |
    | --- | --- | --- | --- | --- |
    | `hom-` | homo | | `mond-` | mondo |
    | `vir-` | viro | | `temp-` | tempo |
    | `infan-` | infano | | `tag-` | tago |
    | `dom-` | domo | | `jar-` | jaro |
    | `urb-` | urbo | | `akv-` | akvo |
    | `land-` | lando | | `lum-` | lumo |

=== "Adjektivoj"

    | Radiko | Signifo | | Radiko | Signifo |
    | --- | --- | --- | --- | --- |
    | `bon-` | bona | | `bel-` | bela |
    | `grand-` | granda | | `long-` | longa |
    | `nov-` | nova | | `alt-` | alta |

Ĉi tio estas nur semo. Produkta listo plej bone deriviĝas laŭ ofteco el
[korpuso](resources.md#korpusoj); la ideo ĉi tie estas, ke la radikoj, kiel ĉio alia en
Esperanto, estas finia listo, kiun la biblioteko povas teni en dosiero.

## Formato

Ĉiuj ĉi tiuj listoj estas konservataj same, kiel **JSON-dosieroj sub `resources/`**,
por ke unu sola fonto de vero povu nutri kaj la kodon (rultempe) kaj la dokumentaron
(konstrutempe, per
[`docs/hooks/word_lists.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/docs/hooks/word_lists.py)).
La nomoj de la kampoj estas en Esperanto, kongruaj kun la dosiernomoj; la tradukeblaj
kampoj estas objektoj indeksitaj laŭ lingvokodo:

```jsonc
{
  "id": "ignorindaj-vortoj",          // ankaŭ la URL de la generita paĝo
  "titolo": { "eo": "Ignorindaj vortoj", "en": "Stop-words" },
  "lingvo": "eo",
  "tradukoj": ["en"],                 // lingvoj ĉeestantaj en "traduko"
  "kategorioj": {                     // gramatikaj kategorioj uzataj sube
    "prepozicio": { "en": "Preposition" }
  },
  "vortoj": [
    {
      "vorto": "kun",                 // la vorto, minuskle
      "kategorio": "prepozicio",      // ŝlosilo de "kategorioj"
      "traduko": { "en": ["with"] },
      "fontoj": ["stopwords-iso"]     // deveno, laŭvola
    }
  ]
}
```

La konstruo de la dokumentaro postulas nur `id`, `titolo` kaj `vortoj`, sed
[`tests/test_resources.py`](../python-library/testing.md#la-strukturo-tests) estas pli
severa: `id` devas kongrui kun la dosiernomo, kaj ĉiu `vorto` devas esti minuskla,
unika, havi `traduko`-n kaj uzi `kategorio`-n deklaritan en `kategorioj`. La dosieroj
estas UTF-8 kaj konservas la realajn diakritajn signojn (`ĉ ĝ ĥ ĵ ŝ ŭ`), neniam la
x-sistemon. Tiel misformita redakto malsukcesas en CI anstataŭ en konstruo de la
dokumentaro. La plena skemo estas dokumentita en `resources/README.md`.

Uzi liston el la biblioteko estas do afero de du linioj:

```python
import json
from pathlib import Path

data = json.loads(Path("resources/esperanto/vortoj.json").read_text(encoding="utf-8"))
stop_words = {entry["vorto"] for entry in data["vortoj"]}
```

## Kien iri poste

- [Vortlistoj](word-lists/index.md) — la generitaj datumpaĝoj.
- [Rimedoj](resources.md) — vortaroj kaj korpusoj por vastigi ĉi tiujn listojn.
