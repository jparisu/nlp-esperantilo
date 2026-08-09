# NLP Esperantilo

**NLP Esperantilo** estas projekto kun eduka celo, kiu helpas konstrui
bibliotekon por komputila lingvistiko (NLP) en Esperanto.
La projekto havas 2 partojn:

<div class="grid cards" markdown>

- :material-package-variant:{ .lg .middle } **[Biblioteko](library/index.md)**

    ---

    La referenca manlibro de `esperantilo`, regul-bazita NLP-biblioteko por
    Esperanto: kion ĝi faras hodiaŭ, kaj kion signifas ĉiu publika nomo. Ĝia
    [API-referenco](library/api.md) estas generita el la fontkodo.

- :material-book-open-page-variant:{ .lg .middle } **[Gvidilo](guide/index.md)**

    ---

    Kiel oni konstruas kaj eldonas tian bibliotekon: Git, GitHub, pakado kaj
    Esperanta lingvoscio.

</div>

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
    `esperantilo` estas projekto kun eduka celo; ĝi ne provas esti kompleta kaj
    preta-por-produktado biblioteko.

## Konstrui ĉi tiun paĝaron loke

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

La paĝaro tiam disponeblas ĉe <http://127.0.0.1:8000>. Ĉiu push al `main`
rekonstruas ĝin kaj publikigas ĝin en GitHub Pages.
