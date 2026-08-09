# Legi Vikipedion

NLP-biblioteko estas senutila sen teksto por prilabori. `esperantilo` havigas
tiun tekston el Vikipedio per [`WikiPage`](api.md#esperantilo.wiki.WikiPage),
jam senigita je vikia marklingvo.

```python
from esperantilo import WikiPage

page = WikiPage.look_up("Esperanto", language="eo")

page.title          # 'Esperanto'
page.qid            # 'Q143'
len(page)           # nombro da sekcioj
```

## Titoloj, konceptoj kaj lingvoj

Artikolo ekzistas unufoje por ĉiu lingvo, kaj la sama *koncepto* estas alia paĝo
en ĉiu el ili: `Parsley`, `Perejil` kaj `Petroselo` estas tri artikoloj pri unu
sama planto. Kio ligas ilin estas la **QID**, la identigilo kiun Vikidatumoj
donas al la koncepto mem — petroselo estas `Q26980`, en ĉiu lingvo.

`look_up` uzas tion. Ĝi solvas la titolon al koncepto kaj poste legas la
artikolon por ĝi, do la lingvo en kiu vi *serĉas* kaj la lingvo en kiu vi
*legas* ne devas esti la sama:

```python
WikiPage.look_up("Perejil", language="eo").title
# 'Petroselo'
```

La titolo estas serĉata unue en `language` kaj poste en ĉiu el
`fallback_languages`, sekvante alidirektilojn. La artikolo revenas en
`language`, se tiu vikio havas ĝin, aŭ en la unua rezerva lingvo kiu havas ĝin —
do kontrolu `page.language`, kiu eble ne estas la kodo kiun vi petis.

Se neniu listigita lingvo konas la titolon, `any_language=True` (la defaŭlto)
serĉas en Vikidatumoj tra ĉiuj lingvoj. Tiu paŝo estas *serĉo*, ne konsulto: ĝi
trovas ion por preskaŭ ĉiu kredebla vorto, kaj kion ĝi trovas ne nepre estas
tio, kion vi celis. Uzu `any_language=False` por ricevi `ValueError` anstataŭ
divenon.

## Sekcioj

La korpo estas mapo de titolo al teksto, en la ordo en kiu la artikolo
prezentas ilin. Nur unuanivelaj titoloj malfermas sekcion; pli profundaj restas
ene de la teksto de la sekcio al kiu ili apartenas. Vikipedio lasas la
enkondukon sentitola, do ĝi estas ŝlosita sub la titolo de la artikolo.

```python
page.section_names          # ['Esperanto', 'Historio', 'Gramatiko', …]
page.section("historio")    # komparata ignorante usklecon
page["Historio"]            # la sama afero
"Historio" in page          # True
page.full_text()            # ĉiu sekcio, kun siaj titoloj
```

## Kio povas misiri

| Situacio | Kio okazas |
| --- | --- |
| Neniu listigita lingvo konas la titolon | `ValueError` |
| La koncepto havas artikolon en neniu el ili | `ValueError` |
| Ne ekzistas sekcio kun tiu nomo | `KeyError` |
| Neniu konekto, tempolimo, API-eraro | `requests.RequestException` |

`ValueError` signifas «la paĝo ne estas tie». Ĉio rilata al la reto aperas kiel
escepto de `requests`, do la du estas kapteblaj aparte.

Ĉiu konsulto kostas inter unu kaj ok HTTP-petoj, depende de kiom da lingvoj oni
devas provi. Nenio estas konservata en kaŝmemoro: voki `look_up` dufoje kun la
samaj argumentoj elŝutas ĉion dufoje.

## Permesilo

La teksto de Vikipedio estas **CC BY-SA**. Se vi reeldonas tion, kion vi
havigas, konservu la atribuon kaj la permesilon; `page.url` estas la ligilo por
citi.

## Lingvoj

Jen listo de kelkaj el la plej uzataj lingvoj, kun iliaj Vikipediaj kodoj:

| Lingvo | Kodo |
| --- | --- |
| Esperanto | `eo` |
| Angla | `en` |
| Hispana | `es` |
| Franca | `fr` |
| Germana | `de` |
| ... | ... |

La kompleta listo de kodoj troviĝas en
[Wikipedia:List of ISO 639 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).

## Vidu ankaŭ

- [API-referenco](api.md#esperantilo.wiki.WikiPage) — la generita signaturo, la
  argumentoj kaj la ekzemploj.
- [`resources/notebooks/wikipedia.ipynb`](https://github.com/jparisu/nlp-esperantilo/blob/main/resources/notebooks/wikipedia.ipynb)
  — notlibro preta por ruli en Google Colab.
- [Fraz-dividado](sentence-segmentation.md) — la evidenta sekva paŝo por la
  teksto kiun vi ĵus havigis.
