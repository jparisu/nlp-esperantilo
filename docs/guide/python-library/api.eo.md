# API

La **API** (Application Programming Interface, programad-interfaco de aplikaĵoj) de
biblioteko estas ĝia *publika vizaĝo*: la objektoj, funkcioj kaj metodoj, kiujn la
uzantoj estas destinitaj tuŝi. Ĉio alia estas realiga detalo, kiun vi rajtas ŝanĝi.
Bone dezajni tiun *vizaĝon* estas tio, kio disigas bibliotekon, kiun oni ĝuas uzi, de
tiu kontraŭ kiu oni batalas.

La pako `esperantilo` eksponas ĝis nun unu klason kaj unu funkcion, do la plej granda parto
de ĉi tiu paĝo estas **dezajna celo**: ĝi montras kiel aspektas NLP-interfaco.

!!! tip "La parto, kiu jam ekzistas"
    Ĉio sube estas ilustrita de reala, eldonita kodo:
    [Biblioteko → API-referenco](../../library/api.md) estas la nuna publika
    surfaco de `esperantilo`, generita el ĝiaj dokumentĉenoj. Legu ĉi tiun paĝon
    por *kial* API aspektas tiel, kaj tiun por *kion* la biblioteko ofertas
    hodiaŭ.

## Kio estas API ĉi tie

Pensu pri biblioteko kiel havanta du flankojn:

- la **publika API** — kion la uzantoj importas kaj vokas, kaj kion vi promesas teni
  stabila trans versioj;
- la **internaĵoj** — helpaj funkcioj, privataj moduloj kaj datumstrukturoj, kiuj igas
  ĝin funkcii, kaj kiujn vi povas reskribi iam ajn.

La valoro de la distingo estas libereco: dum la publika API tenas sian formon, vi
povas refaktorigi ĉion malantaŭ ĝi sen rompi eĉ unu uzanton. La unua tasko de la
API-dezajno estas do **decidi kio estas publika** kaj igi tiun limon evidenta.

En Python, la limon oni tiras per konvencio kaj per `__all__`:

- La nomoj kun antaŭmetita substreko (`_helper`, `_Cache`) estas **privataj** —
  signalo, ke la uzantoj ne dependu de ili.
- La listo `__all__` en modulo nomas ĝiajn **publikajn** objektojn. Ĝi dokumentas la
  celitan surfacon kaj regas kion alportas `from esperantilo import *`:

Jen kiel `esperantilo` faras tion hodiaŭ, kun sia publika API deklarita eksplicite en `__init__.py`:

```python
# esperantilo/__init__.py
from esperantilo.nlp import sentence_tokenizer
from esperantilo.wiki import WikiPage

__version__ = "0.1.0"

__all__ = ["__version__", "WikiPage", "sentence_tokenizer"]   # la publika API, deklarita eksplicite
```

Kun ĉi tio, uzanto skribas `from esperantilo import WikiPage` kaj neniam devas
scii, ke la klaso vere vivas en `esperantilo.wiki.wiki`, nek ke ĉi tiu apogas
sin sur privata modulo `esperantilo.wiki._wiki_api`, kiu povas ŝanĝiĝi sen
averto.

La kompleta listo, generita el la kodo mem, troviĝas en
[Biblioteko → API-referenco](../../library/api.md).

## Dezajni bonan API-on

Manpleno da principoj igas interfacon antaŭvidebla kaj agrabla. Ili estas la samaj,
kiuj igas [scikit-learn kaj spaCy](library.md#konkreta-ekzemplo) facile lerneblaj:

- **Konsekvenceco.** Similaj aferoj devus aspekti simile. Se `Doc` estas iterebla por
  doni `Token`-ojn, tiam ajna kolekto en la biblioteko devus esti iterebla same.
- **Malgrandaj, antaŭvideblaj subskriboj.** Malmultaj parametroj, sencoplenaj
  defaŭltoj, kaj neniuj surprizoj. `parse(text)` devus simple funkcii; la opcioj estas
  kromaĵoj, ne devigoj.
- **Sencoplenaj nomoj.** `lemma`, `pos`, `is_stop` diras kio ili estas. Evitu
  mallongigojn, kiujn komprenas nur la aŭtoro.
- **Tipindikoj (type hints).** Anotaciu la parametrojn kaj la revenajn tipojn. Ili
  dokumentas la interfacon, ebligas aŭtomatan kompletigon en la redaktilo, kaj lasas
  ke iloj kaptu erarojn antaŭ la rultempo.
- **Dokumentĉenoj (docstrings).** Ĉiu publika objekto ricevas mallongan docstring, kiu
  diras kion ĝi faras, kion ĝi prenas kaj kion ĝi redonas.

```python
def parse(text: str) -> "Doc":
    """Analyse Esperanto ``text`` and return a :class:`Doc`.

    Args:
        text: the raw Esperanto text to analyse.

    Returns:
        A ``Doc`` holding the analysed tokens.
    """
    ...
```

La tipindikoj (`text: str`, `-> "Doc"`) kaj la docstring kune diras al uzanto ĉion
bezonatan por voki `parse` ĝuste, sen legi ĝian korpon.

## API laŭ la stilo de spaCy

[spaCy](https://spacy.io) estas la modela referenco por ĉi tiu projekto. Ĝian
dezajnon indas kopii, ĉar ĝi transformas la malordan tekstoprilaboradon en malgrandan
aron da tipitaj, antaŭvideblaj objektoj. La kerna ideo: **analizi tekston redonas
`Doc`, kaj `Doc` estas sekvenco de `Token`-oj**, ĉiu portanta siajn lingvajn atributojn.

Jen la formo de spaCy, kiun la Esperanta biblioteko celas speguli:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The quick brown fox jumps.")   # -> Doc

for token in doc:                          # Doc estas iterebla super Token-oj
    print(token.text, token.lemma_, token.pos_, token.is_stop)
```

```text
The    the    DET    True
quick  quick  ADJ    False
brown  brown  ADJ    False
fox    fox    NOUN   False
jumps  jump   VERB   False
.      .      PUNCT  False
```

Du tipitaj objektoj portas la tutan modelon:

| Objekto | Kion ĝi reprezentas | Tipaj atributoj |
| --- | --- | --- |
| **`Doc`** | Analizita peco da teksto | iterebla de `Token`, `text`, `sents` |
| **`Token`** | Unuopa vorto/unuo | `text`, `lemma`, `pos`, `is_stop` |

Aplikite al Esperanto — kie la [regula gramatiko](../esperanto/grammar.md) igas ĉi
tiujn atributojn kalkuleblaj per reguloj — la cela interfaco aspektas jene:

```python
# Ilustra cela API por esperantilo.
import esperantilo

doc = esperantilo.parse("La rapida vulpo saltas.")

for token in doc:
    print(token.text, token.lemma, token.pos, token.is_stop)
```

```text
La      la      DET     True
rapida  rapida  ADJ     False
vulpo   vulpo   NOUN    False
saltas  salti   VERB    False
.       .       PUNCT   False
```

Rimarku kiel la Esperantaj finaĵoj mapas pure sur atributojn — `-a` → adjektivo, `-o`
→ substantivo, `-as` → verbo en prezenco (kun lemo `salti`), kaj `la` estas ignorinda
vorto. Tiu regulceco, priskribita en la [Esperanto-sekcio](../esperanto/grammar.md),
estas ekzakte tio, kio igas realigeblan regul-bazitan efektivigon de `Doc` / `Token`.

Por la kompleta referenco por imiti — nomoj de metodoj, nomoj de atributoj kaj rilatoj
inter objektoj — vidu la [API-dokumentadon de spaCy](https://spacy.io/api).

## Dokumenti la API-on aŭtomate

Mane verkita API-referenco rapide malaktualiĝas:
iu renomas parametron kaj la paĝo plu montras la malnovan.
La solvo estas generi la paĝon **el la dokumentĉenoj**, tiel ke ekzistu nur unu kopio de la vero.

[mkdocstrings](https://mkdocstrings.github.io/) faras tion por MkDocs. Paĝo, kiu
enhavas nenion krom direktivon:

```markdown
::: esperantilo.nlp
    options:
      members:
        - sentence_tokenizer
```

bildigas la signaturon, la tipindikojn, la argument-tabelon kaj la ekzemplojn de
ĉiu listigita objekto, ĉiun kun ligilo al la fontlinioj, el kiuj ĝi venis. Ĝuste
tiel estas konstruita [Biblioteko → API-referenco](../../library/api.md); la
fonto de tiu paĝo estas [kvar direktivoj kaj alineo](https://github.com/jparisu/nlp-esperantilo/blob/main/docs/library/api.md).

Du kutimoj igas la generitan paĝon leginda:

- **Verku dokumentĉenojn en konsekvenca stilo.** Ĉi tiu projekto uzas la
  Google-stilon montritan supre (`Args:`, `Returns:`, `Examples:`), deklaritan
  unufoje en `mkdocs.yml`.
- **Metu ekzemplojn en `Examples:`-blokojn.** Verkitaj kiel `>>>`-seancoj ili
  estas samtempe dokumentado kaj [dokumentteestoj](testing.md) — la
  kontinua integrado rulas ilin, do ili ne povas silente malaktualiĝi.

## Kien iri poste

- [Biblioteko → API-referenco](../../library/api.md) — la samaj ideoj, aplikitaj:
  la reala publika surfaco de `esperantilo`, generita el ĝia fontkodo.
- [Testado](testing.md) — kiel kontroli ke la API kondutas laŭ sia dezajno.
- [Esperanto § Gramatiko](../esperanto/grammar.md) — la reguloj, kiujn enkodigos la
  API.
