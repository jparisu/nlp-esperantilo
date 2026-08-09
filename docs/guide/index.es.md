# Guía

Una guía para construir y publicar una biblioteca de Python como esta: el
control de versiones, el flujo de trabajo colaborativo, el empaquetado y las
pruebas, y el conocimiento lingüístico que va dentro.

!!! info "Guía, no referencia"
    Estas páginas enseñan el *cómo*. La sección
    [Biblioteca](../library/index.md) es la otra mitad de este sitio: el manual
    de referencia de `esperantilo`, qué hace hoy y qué significa cada nombre
    público. La guía enlaza con ella siempre que un ejemplo real explique algo
    mejor que la prosa.

## Para quién es

Estudiantes universitarios que tienen que construir su propia biblioteca de NLP
para el Esperanto. Se espera cierta base técnica, pero no necesariamente
experiencia con estas herramientas concretas.

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

## Qué *no* cubre esta guía {#que-no-cubre-esta-guia}

Dos temas se dejan fuera deliberadamente, porque se enseñan en las clases del
curso:

- **Web scraping y consumo de APIs** (`requests`, `beautifulsoup4`, la API de
  Wikipedia y similares).
- **Minería de textos y clasificación con Machine Learning** (extracción de
  características, vectorización, entrenamiento y evaluación de modelos,
  métricas).

Aquí el foco está en las *herramientas de ingeniería de software* necesarias
para trabajar como un equipo profesional, y en el *conocimiento del dominio del
Esperanto* necesario para escribir una biblioteca de NLP basada en reglas.

La biblioteca sí *usa* el primero de esos dos temas —`esperantilo.wiki` llama a
las APIs de Wikipedia y Wikidata con `requests`—, pero como código publicado que
leer, no como lección: véase
[Biblioteca → Leer Wikipedia](../library/wikipedia.md).

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
