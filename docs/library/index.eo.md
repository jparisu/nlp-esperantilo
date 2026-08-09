# Biblioteko

**`esperantilo`** estas regul-bazita biblioteko por komputila lingvistiko (NLP) en Esperanto.
Ĉi tiu sekcio estas ĝia *referenca manlibro*: kion ĝi faras, kiel instali ĝin, kaj kion signifas ĉiu publika nomo.

!!! info "Referenco, ne lernilo"
    Ĉi tiuj paĝoj dokumentas la bibliotekon **tia, kia ĝi estas**.
    La gvidilon vi trovos [ĉi tie](../guide/index.md).

!!! warning "Nur du funkcioj ĝis nun"
    La biblioteko estas ĉe versio `0.1.0` kaj havas du aferojn: legadon de
    Vikipediaj artikoloj kaj fraz-dividadon. Ĉio alia — vortoj (*tokens*), lemoj,
    afiksa analizo — ankoraŭ estas [dezajna celo](../guide/python-library/api.md),
    ne eldonita kodo.

<div class="grid cards" markdown>

- [**1. Fraz-dividado**](sentence-segmentation.md) — dividi tekston en frazojn.
- [**2. Legi Vikipedion**](wikipedia.md) — havigi artikolon kiel platan tekston, en iu ajn lingvo.
- [**3. API-referenco**](api.md) — ĉiu publika nomo, generita el la fontkodo.

</div>

## Instalado

La biblioteko dependas de [`requests`](https://requests.readthedocs.io/), kiun
`pip` instalas kune kun ĝi. Instalu ĝin rekte el GitHub:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

Paŝon-post-paŝaj instrukcioj, inkluzive de virtualaj medioj kaj notlibroj,
troviĝas en
[Gvidilo → Instalado kaj uzado](../guide/python-library/installation-and-usage.md).

## Rapida komenco

```python
import esperantilo

# Havigi Vikipedian artikolon en Esperanto.
page = esperantilo.WikiPage.look_up("Esperanto", language="eo")

# Dividi la tekston en frazojn.
sentences = esperantilo.sentence_tokenizer(page.full_text())
```

## La publika API

Ĉio, kion la biblioteko promesas teni stabila, estas importebla rekte el la
ĉefa modulo `esperantilo`:

| Nomo | Speco | Kio ĝi estas |
| --- | --- | --- |
| [`WikiPage`](api.md#esperantilo.wiki.WikiPage) | klaso | Unu Vikipedia artikolo, en unu lingvo, kiel plata teksto. |
| [`sentence_tokenizer`](api.md#esperantilo.nlp.sentence_tokenizer) | funkcio | Dividas tekston en frazojn. |
| [`__version__`](api.md#esperantilo.__version__) | konstanto | La instalita versio. |

## Strukturo

```text
src/esperantilo/
├── __init__.py      # la publika API: reeksportoj kaj __all__
├── nlp/             # analizi tekston jam havatan
│   └── tokenizer.py #   fraz-dividado
└── wiki/            # havigi tekston el Vikipedio
    ├── wiki.py      #   la klaso WikiPage
    └── _wiki_api.py #   privata: la klientoj de MediaWiki kaj Vikidatumoj
```

La [API-referenco](api.md) estas **generita el tiuj dosieroj** ĉiufoje kiam la
paĝaro estas konstruata, do ŝanĝu dokumentĉenon kaj la paĝo ŝanĝiĝas kun ĝi.
