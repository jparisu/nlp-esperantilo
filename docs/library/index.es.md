# Biblioteca

**`esperantilo`** es una biblioteca de Procesamiento del Lenguaje Natural basada en reglas para el Esperanto.
Esta sección es su *manual de referencia*: qué hace, cómo se instala y qué significa cada nombre público.

!!! info "Referencia, no tutorial"
    Estas páginas documentan la biblioteca **tal como es**.
    La guía la encontrarás [aquí](../guide/index.md).

!!! warning "Dos funciones por ahora"
    La biblioteca está en la versión `0.1.0` y ofrece dos cosas: la lectura de
    artículos de Wikipedia y la segmentación en frases. Todo lo demás —tokens,
    lemas, análisis de afijos— sigue siendo un
    [objetivo de diseño](../guide/python-library/api.md), no código publicado.

<div class="grid cards" markdown>

- [**1. Segmentación en frases**](sentence-segmentation.md) — dividir un texto en frases.
- [**2. Leer Wikipedia**](wikipedia.md) — obtener un artículo como texto plano, en cualquier idioma.
- [**3. Referencia de la API**](api.md) — cada nombre público, generado desde el código.

</div>

## Instalación

La biblioteca depende de [`requests`](https://requests.readthedocs.io/), que
`pip` instala junto con ella. Se instala directamente desde GitHub:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

Las instrucciones paso a paso, incluidos los entornos virtuales y los notebooks,
están en
[Guía → Instalación y uso](../guide/python-library/installation-and-usage.md).

## Inicio rápido

```python
import esperantilo

# Obtén un artículo de Wikipedia en Esperanto.
page = esperantilo.WikiPage.look_up("Esperanto", language="eo")

# Divide el texto en frases.
sentences = esperantilo.sentence_tokenizer(page.full_text())
```

## La API pública

Todo lo que la biblioteca se compromete a mantener estable se importa
directamente del módulo `esperantilo`:

| Nombre | Tipo | Qué es |
| --- | --- | --- |
| [`WikiPage`](api.md#esperantilo.wiki.WikiPage) | clase | Un artículo de Wikipedia, en un idioma, como texto plano. |
| [`sentence_tokenizer`](api.md#esperantilo.nlp.sentence_tokenizer) | función | Divide un texto en frases. |
| [`__version__`](api.md#esperantilo.__version__) | constante | La versión instalada. |

## Estructura

```text
src/esperantilo/
├── __init__.py      # la API pública: reexportaciones y __all__
├── nlp/             # analizar texto que ya se tiene
│   └── tokenizer.py #   segmentación en frases
└── wiki/            # obtener texto de Wikipedia
    ├── wiki.py      #   la clase WikiPage
    └── _wiki_api.py #   privado: los clientes de MediaWiki y Wikidata
```

La [referencia de la API](api.md) se **genera a partir de esos archivos** cada
vez que se construye el sitio, así que cambia un docstring y la página cambia
con él.
