# NLP Esperantilo

**NLP Esperantilo** son dos cosas a la vez, y este sitio está dividido en
consecuencia.

<div class="grid cards" markdown>

- :material-package-variant:{ .lg .middle } **[Biblioteca](library/index.md)**

    ---

    El manual de referencia de `esperantilo`, una biblioteca de PLN basada en
    reglas para el Esperanto: qué hace hoy y qué significa cada nombre público.
    Su [referencia de la API](library/api.md) se genera desde el código fuente.

- :material-book-open-page-variant:{ .lg .middle } **[Guía](guide/index.md)**

    ---

    Cómo se construye y se publica una biblioteca como esa: Git, GitHub,
    empaquetado y pruebas en Python, y la lingüística del Esperanto que va
    dentro.

</div>

## Cuál te interesa

| Si quieres… | Ve a |
| --- | --- |
| Usar la biblioteca desde tu propio código | [Biblioteca](library/index.md) |
| Saber exactamente qué devuelve una función | [Biblioteca → Referencia de la API](library/api.md) |
| Aprender Git, GitHub, empaquetado o pruebas | [Guía](guide/index.md) |
| Aprender las reglas del Esperanto que codifica un PLN | [Guía → Esperanto](guide/esperanto/index.md) |

Las dos mitades se enlazan constantemente: la guía explica una técnica y después
señala el lugar de la biblioteca donde se usa de verdad.

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
    `esperantilo` está en la versión `0.1.0` y ofrece una sola función:
    [segmentación en frases](library/sentence-segmentation.md). Los tokens, los
    lemas y el análisis de afijos siguen siendo un
    [objetivo de diseño](guide/python-library/api.md), no código publicado.
    Construir el resto es justo el ejercicio para el que este sitio te prepara.

## Para quién es

Estudiantes universitarios que tienen que construir su propia biblioteca de PLN
para el Esperanto. Se espera que quien lea tenga cierta base técnica, pero no
necesariamente experiencia con las herramientas y los temas concretos que aquí
se explican.

Dos temas se dejan fuera de la guía deliberadamente, porque se enseñan en las
clases del curso: **web scraping y consumo de APIs**, y **minería de textos y
clasificación con Machine Learning**. Véase
[Guía → qué no cubre](guide/index.md#que-no-cubre-esta-guia).

## Construir este sitio en local

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

El sitio queda entonces disponible en <http://127.0.0.1:8000>. Cada push a `main`
lo reconstruye y lo publica en GitHub Pages.
