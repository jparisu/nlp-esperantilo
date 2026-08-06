# Biblioteko

**`esperantilo`** estas regul-bazita biblioteko por komputila lingvistiko (NLP)
en Esperanto. Ĉi tiu sekcio estas ĝia *referenca manlibro*: kion ĝi faras
hodiaŭ, kiel instali ĝin, kaj kion signifas ĉiu publika nomo.

!!! info "Referenco, ne lernilo"
    Ĉi tiuj paĝoj dokumentas la bibliotekon **tia, kia ĝi estas**. La
    [Gvidilo](../guide/index.md) estas la alia duono de ĉi tiu paĝaro: ĝi
    instruas, kiel oni konstruas, eldonas kaj testas tian bibliotekon. Se vi
    venas por lerni la ilaron, komencu tie.

!!! warning "Nur unu funkcio ĝis nun"
    La biblioteko estas ĉe versio `0.1.0` kaj havas ekzakte unu aferon:
    fraz-dividadon. Ĉio alia — vortoj (*tokens*), lemoj, afiksa analizo — ankoraŭ
    estas [dezajna celo](../guide/python-library/api.md), ne eldonita kodo.

<div class="grid cards" markdown>

- [**1. Fraz-dividado**](sentence-segmentation.md) — dividi tekston en frazojn.
- [**2. API-referenco**](api.md) — ĉiu publika nomo, generita el la fontkodo.

</div>

## Instalado

La biblioteko havas **neniun rultempan dependecon**. Instalu ĝin rekte el
GitHub:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

Paŝon-post-paŝaj instrukcioj, inkluzive de virtualaj medioj kaj notlibroj,
troviĝas en
[Gvidilo → Instalado kaj uzado](../guide/python-library/installation-and-usage.md).

## Rapida komenco

```python
import esperantilo

esperantilo.sentence_tokenizer("Zamenhof kreis Esperanton. Ĉu vere? Jes!")
# ['Zamenhof kreis Esperanton.', 'Ĉu vere?', 'Jes!']
```

## La publika API

Ĉio, kion la biblioteko promesas teni stabila, estas importebla rekte el la
ĉefa modulo `esperantilo`, kaj estas listigita en ĝia `__all__`:

| Nomo | Speco | Kio ĝi estas |
| --- | --- | --- |
| [`sentence_tokenizer`](api.md#esperantilo.tokenizer.sentence_tokenizer) | funkcio | Dividas tekston en frazojn. |
| [`__version__`](api.md#esperantilo.__version__) | konstanto | La instalita versio. |

Kio ne estas en tiu listo — ĉiu privata helpfunkcio, ĉiu interna modulo — estas
efektiviga detalo kaj povas ŝanĝiĝi sen averto. Kial tiu limo gravas, kaj kiel
oni desegnas ĝin en Python, estas klarigita en
[Gvidilo → API](../guide/python-library/api.md).

## Kie loĝas la partoj

```text
src/esperantilo/
├── __init__.py      # la publika API: reeksportoj kaj __all__
└── tokenizer.py     # fraz-dividado
```

La [API-referenco](api.md) estas **generita el tiuj dosieroj** ĉiufoje kiam la
paĝaro estas konstruata, do ŝanĝu dokumentĉenon kaj la paĝo ŝanĝiĝas kun ĝi.
