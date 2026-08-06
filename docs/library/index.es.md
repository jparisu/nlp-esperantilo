# Biblioteca

**`esperantilo`** es una biblioteca de Procesamiento del Lenguaje Natural basada
en reglas para el Esperanto. Esta sección es su *manual de referencia*: qué hace
hoy, cómo se instala y qué significa cada nombre público.

!!! info "Referencia, no tutorial"
    Estas páginas documentan la biblioteca **tal como es**. La
    [Guía](../guide/index.md) es la otra mitad de este sitio: enseña cómo se
    construye, se publica y se prueba una biblioteca como esta. Si vienes a
    aprender las herramientas, empieza allí.

!!! warning "Una sola función por ahora"
    La biblioteca está en la versión `0.1.0` y ofrece exactamente una cosa: la
    segmentación en frases. Todo lo demás —tokens, lemas, análisis de afijos—
    sigue siendo un [objetivo de diseño](../guide/python-library/api.md), no
    código publicado.

<div class="grid cards" markdown>

- [**1. Segmentación en frases**](sentence-segmentation.md) — dividir un texto en frases.
- [**2. Referencia de la API**](api.md) — cada nombre público, generado desde el código.

</div>

## Instalación

La biblioteca **no tiene dependencias en tiempo de ejecución**. Se instala
directamente desde GitHub:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

Las instrucciones paso a paso, incluidos los entornos virtuales y los notebooks,
están en
[Guía → Instalación y uso](../guide/python-library/installation-and-usage.md).

## Inicio rápido

```python
import esperantilo

esperantilo.sentence_tokenizer("Zamenhof kreis Esperanton. Ĉu vere? Jes!")
# ['Zamenhof kreis Esperanton.', 'Ĉu vere?', 'Jes!']
```

## La API pública

Todo lo que la biblioteca se compromete a mantener estable se importa
directamente del módulo `esperantilo` y aparece listado en su `__all__`:

| Nombre | Tipo | Qué es |
| --- | --- | --- |
| [`sentence_tokenizer`](api.md#esperantilo.tokenizer.sentence_tokenizer) | función | Divide un texto en frases. |
| [`__version__`](api.md#esperantilo.__version__) | constante | La versión instalada. |

Lo que no está en esa lista —cada función auxiliar privada, cada módulo interno—
es un detalle de implementación y puede cambiar sin aviso. Por qué importa esa
frontera, y cómo se traza en Python, se explica en
[Guía → API](../guide/python-library/api.md).

## Dónde vive cada pieza

```text
src/esperantilo/
├── __init__.py      # la API pública: reexportaciones y __all__
└── tokenizer.py     # segmentación en frases
```

La [referencia de la API](api.md) se **genera a partir de esos archivos** cada
vez que se construye el sitio, así que cambia un docstring y la página cambia
con él.
