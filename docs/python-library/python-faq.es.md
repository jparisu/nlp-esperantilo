# Preguntas frecuentes

Preguntas habituales sobre construir, instalar y probar la biblioteca de Python.
Cada respuesta enlaza a la página donde el tema se trata en detalle.

??? question "¿Cuál es la diferencia entre un módulo, un paquete y una biblioteca?"
    Un **módulo** es un único archivo `.py`; un **paquete** es una carpeta de
    módulos con un `__init__.py`; una **biblioteca** es un paquete pensado para ser
    reutilizado por otro código. Una **distribución** es el paquete instalable que
    `pip` descarga. Véase
    [Qué es una biblioteca](library.md#modulo-paquete-biblioteca-distribucion).

??? question "¿Necesito `setup.py`? ¿Qué es `pyproject.toml`?"
    No — `pyproject.toml` es el reemplazo moderno y estandarizado de `setup.py`.
    Contiene los metadatos del proyecto, las dependencias y la configuración de
    construcción en un solo archivo. Véase
    [Organización § pyproject.toml](organization.md#pyprojecttoml).

??? question "¿Por qué el código está bajo `src/` en lugar de en la raíz del repositorio?"
    Para que el paquete no sea importable *por accidente* desde la raíz del
    proyecto. La estructura `src/` te obliga a instalar el paquete antes de
    importarlo, de modo que tus pruebas se ejecutan contra la biblioteca instalada
    exactamente como la obtendría un usuario. Véase
    [Organización § src](organization.md#the-src-layout).

??? question "¿Cuál es la diferencia entre `requirements.txt` y `pyproject.toml`?"
    `pyproject.toml` declara lo que la *biblioteca* necesita como parte de su
    identidad — la fuente de verdad cuando alguien la instala. `requirements.txt`
    es una lista de conveniencia para fijar un *entorno* reproducible. Esta
    biblioteca está basada en reglas, así que no tiene dependencias de ejecución y
    `requirements.txt` está esencialmente vacío. Véase
    [Organización § requirements.txt](organization.md#requirementstxt).

??? question "¿Qué hace `__init__.py`?"
    Marca un directorio como **paquete** y define qué expone el paquete al
    importarse. Aquí declara la versión y, a medida que la biblioteca crezca, es
    donde se reexportan las clases públicas. Véase
    [Organización § __init__.py](organization.md#__init__py).

??? question "¿Cómo instalo la biblioteca en un notebook de Google Colab?"
    Instálala directamente desde GitHub en una celda, luego impórtala:

    ```python
    !pip install git+https://github.com/jparisu/nlp-esperantilo.git
    import esperantilo
    ```

    Véase [Instalación y uso](installation-and-usage.md#usarlo-en-un-notebook).

??? question "¿Qué significa `pip install -e \".[test]\"`?"
    `-e` instala el paquete en modo **editable** (un enlace a tu código fuente, de
    modo que las ediciones surten efecto de inmediato), y `.[test]` instala además
    el extra `test` (`pytest`). Es la configuración estándar para *desarrollar* la
    biblioteca. Véase
    [Instalación y uso § Instalar en local](installation-and-usage.md#instalar-en-local).

??? question "Instalé una nueva versión en un notebook pero nada cambió. ¿Por qué?"
    Python cachea los módulos importados durante la sesión. Tras instalar una nueva
    versión, **reinicia el entorno de ejecución** (Runtime → Restart) para que se
    cargue el código nuevo. Véase
    [Instalación y uso](installation-and-usage.md#usarlo-en-un-notebook).

??? question "¿Para qué sirve `__all__`?"
    Nombra los objetos **públicos** de un módulo: documenta la API prevista y
    controla qué trae `from esperantilo import *`. Los nombres fuera de ella (y los
    que empiezan por `_`) se tratan como privados. Véase
    [API § Qué es aquí una API](api.md#que-es-aqui-una-api).

??? question "¿Por qué modelar la API sobre spaCy?"
    Porque el diseño tipado `Doc` / `Token` de spaCy es una forma probada y
    agradable de representar texto analizado, y la gramática regular del Esperanto
    hace que esos atributos sean calculables por reglas. Da un objetivo concreto a
    imitar. Véase [API § Una API al estilo de spaCy](api.md#una-api-al-estilo-de-spacy).

??? question "¿Cómo ejecuto las pruebas?"
    Instala el extra de pruebas y ejecuta pytest:

    ```bash
    pip install -e ".[test]"
    pytest
    ```

    pytest descubre automáticamente los archivos llamados `test_*.py` y las
    funciones llamadas `test_*`. Véase
    [Pruebas](testing.md#escribir-y-ejecutar-pruebas-con-pytest).

??? question "¿Se ejecutan las pruebas automáticamente?"
    Sí. El workflow `tests.yml` de GitHub Actions ejecuta `pytest` en cada push y
    pull request, y la protección de ramas puede hacer que pasar las pruebas sea
    **obligatorio** antes de una fusión. Véase
    [Pruebas § Pruebas en integración continua](testing.md#pruebas-en-integracion-continua).
