# NLP Esperantilo

**NLP Esperantilo** es un proyecto con fines educativos para ayudar a construir una librería de procesamiento de lenguaje natural (NLP) para el Esperanto.
El proyecto cuenta con 2 partes:

<div class="grid cards" markdown>

- :material-package-variant:{ .lg .middle } **[Biblioteca](library/index.md)**

    ---

    El manual de referencia de `esperantilo`, una biblioteca de NLP basada en
    reglas para el Esperanto: qué hace hoy y qué significa cada nombre público.
    Su [referencia de la API](library/api.md) se genera desde el código fuente.

- :material-book-open-page-variant:{ .lg .middle } **[Guía](guide/index.md)**

    ---

    Cómo se construye y se publica una biblioteca como esa: Git, GitHub,
    empaquetado y lingüística del Esperanto.

</div>

## Pruébala

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

```python
import esperantilo

esperantilo.sentence_tokenizer("Zamenhof kreis Esperanton. Ĉu vere? Jes!")
# ['Zamenhof kreis Esperanton.', 'Ĉu vere?', 'Jes!']
```

!!! warning "La biblioteca es deliberadamente pequeña"
    `esperantilo` es un proyecto con caracter educativo, no intenta ser una librería completa y funcional.


## Construir este sitio en local

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

El sitio queda entonces disponible en <http://127.0.0.1:8000>. Cada push a `main`
lo reconstruye y lo publica en GitHub Pages.
