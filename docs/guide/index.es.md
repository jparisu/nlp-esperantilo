# Guía

Esta guía te ayudará a construir y publicar una biblioteca de Python como la de este repositorio.
Te guiará por los conceptos básicos del control de versiones, el flujo de trabajo colaborativo, el empaquetado y las
pruebas, y el conocimiento lingüístico que va dentro.

!!! info "Guía, no referencia"
    Estas páginas enseñan el *cómo*. La sección
    [Biblioteca](../library/index.md) es la otra mitad de este sitio: el manual
    de referencia de `esperantilo`, el API y su funcionalidad.

## Las cuatro secciones

<div class="grid cards" markdown>

- [**1. Git**](git/index.md) — control de versiones: cómo funciona, los comandos
  que necesitas y cómo deshacer cambios.
- [**2. GitHub**](github/index.md) — el flujo colaborativo: pull requests,
  Actions, protección del repositorio, Pages.
- [**3. Biblioteca Python**](python-library/index.md) — empaquetado, estructura,
  diseño de la API, instalación y pruebas.
- [**4. Esperanto**](esperanto/index.md) — historia, gramática, vocabulario y
  listas de palabras: las reglas que codifica la biblioteca.

</div>

Las secciones son en gran medida independientes. Léelas en orden si empiezas de
cero; salta directamente a [Biblioteca Python](python-library/index.md) o a
[Esperanto](esperanto/index.md) si ya conoces Git y GitHub.

## Este repositorio es el ejemplo

Cada vez que la guía muestra un archivo, un workflow o un commit, es uno real de
este repositorio, no un fragmento inventado. La sección
[Biblioteca](../library/index.md) documenta el resultado.

| La guía explica | Puedes verlo funcionando en |
| --- | --- |
| [`pyproject.toml` y la estructura `src/`](python-library/organization.md) | [`pyproject.toml`](https://github.com/jparisu/nlp-esperantilo/blob/main/pyproject.toml) |
| [Diseñar una API pública](python-library/api.md) | [Biblioteca → Referencia de la API](../library/api.md) |
| [Escribir pruebas](python-library/testing.md) | [`tests/test_tokenizer.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py) |
| [GitHub Actions](github/actions.md) | [`.github/workflows/`](https://github.com/jparisu/nlp-esperantilo/tree/main/.github/workflows) |
| [GitHub Pages](github/pages.md) | este sitio |
