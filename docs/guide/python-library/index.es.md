# Biblioteca Python

Esta sección explica cómo construir una biblioteca de Python: cómo organizarla,
cómo diseñar su API, cómo probarla y cómo instalarla y usarla. El ejemplo
recurrente es `esperantilo`, el propio paquete que distribuye este proyecto.

Las páginas se apoyan unas en otras — estructura, luego instalación, luego el
diseño de la API, luego las pruebas — pero cada una se sostiene por sí sola si ya
conoces lo básico.

<div class="grid cards" markdown>

- [**1. Qué es una biblioteca**](library.md) — paquetes, módulos y distribuciones.
- [**2. Organización**](organization.md) — `pyproject.toml`, `src/`, `tests/`.
- [**3. Instalación y uso**](installation-and-usage.md) — desde GitHub, en un notebook.
- [**4. API**](api.md) — diseñar una interfaz pública clara, al estilo de spaCy.
- [**5. Pruebas**](testing.md) — `pytest` e integración continua.
- [**Preguntas frecuentes**](python-faq.md) — respuestas rápidas a dudas habituales.

</div>

!!! tip "Ve el resultado"
    Cada técnica de estas páginas está aplicada en este repositorio. La sección
    [Biblioteca](../../library/index.md) es el resultado: el manual de
    referencia de `esperantilo`, con una
    [referencia de la API](../../library/api.md) generada a partir de los mismos
    docstrings que esta sección te enseña a escribir.
