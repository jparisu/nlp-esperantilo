# NLP Esperantilo

**NLP Esperantilo** estas du aferoj samtempe, kaj ĉi tiu paĝaro estas dividita
laŭ tio.

<div class="grid cards" markdown>

- :material-package-variant:{ .lg .middle } **[Biblioteko](library/index.md)**

    ---

    La referenca manlibro de `esperantilo`, regul-bazita NLP-biblioteko por
    Esperanto: kion ĝi faras hodiaŭ, kaj kion signifas ĉiu publika nomo. Ĝia
    [API-referenco](library/api.md) estas generita el la fontkodo.

- :material-book-open-page-variant:{ .lg .middle } **[Gvidilo](guide/index.md)**

    ---

    Kiel oni konstruas kaj eldonas tian bibliotekon: Git, GitHub, Python-pakado
    kaj testado, kaj la Esperanta lingvoscio, kiu iras internen.

</div>

## Kiun vi bezonas

| Se vi volas… | Iru al |
| --- | --- |
| Uzi la bibliotekon el via propra kodo | [Biblioteko](library/index.md) |
| Scii precize kion funkcio redonas | [Biblioteko → API-referenco](library/api.md) |
| Lerni Git, GitHub, pakadon aŭ testadon | [Gvidilo](guide/index.md) |
| Lerni la Esperantajn regulojn, kiujn NLP enkodigas | [Gvidilo → Esperanto](guide/esperanto/index.md) |

La du duonoj konstante interligiĝas: la gvidilo instruas teknikon, poste montras
la lokon en la biblioteko, kie ĝi vere estas uzata.

## Provu ĝin

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

```python
import esperantilo

esperantilo.sentence_tokenizer("Zamenhof kreis Esperanton. Ĉu vere? Jes!")
# ['Zamenhof kreis Esperanton.', 'Ĉu vere?', 'Jes!']
```

!!! warning "La biblioteko estas intence malgranda"
    `esperantilo` estas ĉe versio `0.1.0` kaj havas unu solan funkcion:
    [fraz-dividado](library/sentence-segmentation.md). Vortoj (*tokens*),
    lemoj kaj afiksa analizo ankoraŭ estas
    [dezajna celo](guide/python-library/api.md), ne eldonita kodo. Konstrui la
    ceteron estas ĝuste la ekzerco, por kiu ĉi tiu paĝaro preparas vin.

## Por kiu ĝi estas

Universitataj studentoj, kiuj devas konstrui sian propran Esperantan
NLP-bibliotekon. Oni atendas, ke la leganto havas ian teknikan fonon, sed ne
nepre sperton pri la specifaj iloj kaj temoj ĉi tie klarigataj.

Du temoj estas intence lasitaj ekster la gvidilo, ĉar ili estas instruataj en la
kurslecionoj: **retĉerpado kaj konsumo de API-oj**, kaj **teksto-minado kaj
klasifiko per maŝinlernado**. Vidu
[Gvidilo → kion ĝi ne kovras](guide/index.md#kion-gi-ne-kovras).

## Konstrui ĉi tiun paĝaron loke

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

La paĝaro tiam disponeblas ĉe <http://127.0.0.1:8000>. Ĉiu push al `main`
rekonstruas ĝin kaj publikigas ĝin en GitHub Pages.
