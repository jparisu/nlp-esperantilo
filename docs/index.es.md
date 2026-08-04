# NLP Esperantilo

Bienvenido a **NLP Esperantilo**, un proyecto formado por dos partes
complementarias:

- **Una biblioteca de Python** para el Procesamiento del Lenguaje Natural
  basado en reglas para el Esperanto.
- **Esta documentación**, una guía y un tutorial para construir esa biblioteca y
  las herramientas que la rodean desde cero.

!!! warning "Trabajo en curso"
    Este sitio es el esqueleto de la documentación. Cada sección ya tiene su
    estructura y sus contenidos previstos, pero los contenidos en sí todavía se
    están redactando.

## Para quién es

Esta guía está dirigida a estudiantes universitarios que tienen que construir su
propia biblioteca de PLN para el Esperanto. Se espera que quien la lea tenga
cierta base técnica, pero no necesariamente experiencia con las herramientas y
los temas concretos que aquí se explican.

## Qué cubre esta guía

| Sección | Contenidos |
| --- | --- |
| [Git](git/index.md) | Control de versiones: cómo funciona Git, sus comandos más usados y cómo deshacer cambios. |
| [GitHub](github/index.md) | Flujo de trabajo colaborativo, pull requests, GitHub Actions, protección del repositorio y GitHub Pages. |
| [Biblioteca Python](python-library/index.md) | Empaquetado, estructura del proyecto, diseño de la API, instalación y pruebas. |
| [Esperanto](esperanto/index.md) | Historia, gramática, vocabulario y recursos: las reglas lingüísticas que codifica la biblioteca. |

## Qué *no* cubre esta guía

Dos temas se dejan fuera deliberadamente, porque se enseñan en las clases del
curso:

- **Web scraping y consumo de APIs** (`requests`, `beautifulsoup4`, la API de
  Wikipedia y similares).
- **Minería de textos y clasificación con Machine Learning** (extracción de
  características, vectorización, entrenamiento y evaluación de modelos,
  métricas).

Aquí el foco está en las *herramientas de ingeniería de software* necesarias
para trabajar como un equipo profesional, y en el *conocimiento del dominio del
Esperanto* necesario para escribir una biblioteca de PLN basada en reglas.

## Cómo leer la documentación

La guía puede leerse de principio a fin, pero las cuatro secciones son en gran
medida independientes. Quien ya conozca Git y GitHub puede saltar directamente a
[Biblioteca Python](python-library/index.md) o a [Esperanto](esperanto/index.md).

## Construir la documentación en local

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

El sitio queda entonces disponible en <http://127.0.0.1:8000>. Cada push a `main`
lo reconstruye y lo publica en GitHub Pages.
