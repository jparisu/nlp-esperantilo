# Referencia de la API

Todos los nombres públicos de `esperantilo`, con su firma, sus argumentos y sus
ejemplos.

!!! info "Generada desde el código fuente"
    Nada de esta página está escrito a mano. Se construye a partir de los
    docstrings de
    [`src/esperantilo/`](https://github.com/jparisu/nlp-esperantilo/tree/main/src/esperantilo)
    con [mkdocstrings](https://mkdocstrings.github.io/) cada vez que se genera
    el sitio, así que no puede contradecir al código. Los ejemplos `>>>` también
    los ejecuta `pytest`: véase
    [Guía → Pruebas](../guide/python-library/testing.md#doctests).

    Cada entrada enlaza con las líneas exactas que documenta: despliega
    *Source* para leerlas.

!!! note "Contenido en inglés"
    El código fuente y sus docstrings están escritos en inglés, así que esta
    página se muestra en inglés en todos los idiomas del sitio. La explicación
    en castellano de lo que hace la función está en
    [Segmentación en frases](sentence-segmentation.md).

::: esperantilo
    options:
      heading_level: 2
      members: false

::: esperantilo.__version__
    options:
      heading_level: 3

::: esperantilo.nlp
    options:
      heading_level: 2
      members:
        - sentence_tokenizer

::: esperantilo.wiki
    options:
      heading_level: 2
      members:
        - WikiPage
