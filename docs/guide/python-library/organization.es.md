# Organización

Una biblioteca es más que su código fuente: necesita un puñado de archivos que le
dicen a Python (y a `pip`) cómo construirla, instalarla y describirla. Esta página
recorre la estructura que usa este repositorio y el propósito de cada archivo,
para que puedas reproducirla en tu propio proyecto.

## Estructura recomendada

Este proyecto usa la **estructura `src/`**, la mejor práctica actual para paquetes
de Python:

```text
nlp-esperantilo/
├── src/
│   └── esperantilo/       # el paquete en sí
│       ├── __init__.py    # la API pública: reexportaciones y __all__
│       ├── nlp/           # un subpaquete por área funcional
│       │   └── tokenizer.py
│       └── ...            # otros subpaquetes y módulos
└── tests/                 # scripts de test para la biblioteca
    ├── test_tokenizer.py  # un módulo de pruebas por módulo de código
    └── ...

# Otros ficheros y directorios auxiliares
├── pyproject.toml         # metadatos del proyecto y configuración de construcción
├── README.md              # portada
├── LICENSE                # texto de la licencia
├── mkdocs.yml             # configuración de la documentación
├── docs/                  # la documentación que estás leyendo
├── resources/             # archivos de datos (listas de palabras) y notebooks
├── .github/workflows/     # integración continua
```

Fíjate en el emparejamiento: `tokenizer.py` en `src/`, `test_tokenizer.py` en
`tests/`. Escala sin pensar: una función nueva es un módulo nuevo y un módulo de
test nuevo.
Lo que hace ese módulo en concreto está documentado en
[Biblioteca → Segmentación en frases](../../library/sentence-segmentation.md).

Cuando una función crece más allá de un solo módulo se convierte en un
**subpaquete**: un directorio con su propio `__init__.py` que reexporta los
nombres públicos de esa función. `wiki/` es uno — una clase pública en `wiki.py`
y un cliente HTTP privado en `_wiki_api.py`, del que solo se reexporta la clase.
Quien lo usa sigue escribiendo `from esperantilo import WikiPage` y no llega a
conocer ninguno de los dos nombres de archivo.

El rasgo distintivo es que el paquete importable vive bajo `src/`, no en la raíz
del repositorio. La razón es sutil pero importante — véase
[La estructura `src/`](#the-src-layout) más abajo.

## Los archivos que importan

### `pyproject.toml`

Este único archivo describe todo el proyecto: sus **metadatos** (nombre, versión,
descripción), sus **dependencias** y cómo se **construye**. Es el reemplazo
moderno y estandarizado del antiguo `setup.py`. Estas son las partes clave del
archivo de este proyecto:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "esperantilo"
version = "0.1.0"
description = "A rule-based Natural Language Processing library for Esperanto"
requires-python = ">=3.9"
dependencies = ["requests>=2.25"]      # la única dependencia de ejecución

[project.optional-dependencies]
test = ["pytest>=7.0"]                 # se instala con .[test]
docs = ["mkdocs>=1.6", "mkdocs-material>=9.5", "mkdocs-static-i18n>=1.2"]

[tool.setuptools.packages.find]
where = ["src"]                        # encuentra el paquete bajo src/

[tool.pytest.ini_options]
pythonpath = ["src"]      # so `pytest` works without installing
testpaths = ["tests", "src"]
```

Vale la pena entender tres partes:

- **`[project]`** — la identidad de la biblioteca. `name` es lo que la gente hace
  `pip install`; `version` es lo que fijan; `dependencies` es lo que se instala
  *con* ella.
- **`[project.optional-dependencies]`** — *extras*, instalados a demanda. `.[test]`
  añade `pytest`, `.[docs]` añade las herramientas de MkDocs. Los usuarios de la
  biblioteca no necesitan ninguno; los desarrolladores sí.
- **`[tool.*]`** — configuración de otras herramientas reunida en un solo sitio.
  Aquí `[tool.setuptools.packages.find]` le dice a la construcción dónde está el
  paquete, y `[tool.pytest.ini_options]` configura el ejecutor de pruebas.

### `__init__.py`

Un archivo `__init__.py` marca un directorio como **paquete regular**. Desde
Python 3.3 una carpeta sin él sigue siendo importable, como *paquete de espacio de
nombres*, pero una biblioteca debe ser explícita: el archivo se ejecuta cuando el
paquete se importa por primera vez, y define la **superficie pública** del
paquete. El de este proyecto es deliberadamente mínimo:

```python
"""Esperantilo: a rule-based NLP library for Esperanto."""

__version__ = "0.1.0"

__all__ = ["__version__"]
```

Por ahora solo expone la versión. A medida que la biblioteca crezca, aquí es donde
importarías y reexportarías las clases y funciones públicas, para que los usuarios puedan
impportar sus elementos de forma rápida y sencilla.

### `src/` — por qué el código no está en la raíz {#the-src-layout}

Colocar el paquete bajo `src/` evita un error clásico y confuso. Si el paquete
estuviera en la raíz del repositorio, ejecutar Python *desde* la raíz importaría la
carpeta local directamente — aunque la biblioteca nunca se hubiera instalado. Las
pruebas pasarían contra el código en bruto mientras que la copia instalada de un
usuario real se comporta de otra forma.

Con la estructura `src/`, la raíz *no* es importable, así que te ves obligado a
**instalar el paquete** (`pip install -e .`) antes de importarlo. Tus pruebas se
ejecutan entonces contra la biblioteca exactamente como la recibiría un usuario. Es
un paso extra que elimina toda una categoría de problemas del tipo "en mi máquina
funciona".

### `tests/` — reflejando el código fuente

La carpeta `tests/` contiene la suite de pruebas, mantenida aparte del código que
se distribuye para que las pruebas no se instalen a los usuarios finales. Refleja
lo que prueba:
[`test_package.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_package.py)
comprueba que el paquete se importa y expone su versión, y
[`test_resources.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_resources.py)
valida los archivos de datos bajo `resources/`. Las pruebas tienen su propia
página: [Pruebas](testing.md).

### `requirements.txt`

En muchos casos se usa este fichero como una lista simple de dependencias, una por línea, usada tradicionalmente con
`pip install -r requirements.txt`.
Este es un sistema tradicional para mantener compatibilidades, pero que se ve redundante con `pyproject.toml`, que ya contiene la lista de dependencias y sus versiones.

## Versionado

La versión de la biblioteca se declara como `version` en `pyproject.toml` y se
refleja en `__version__` en `__init__.py`, para que sea legible en tiempo de
ejecución:

```python
>>> import esperantilo
>>> esperantilo.__version__
'0.1.0'
```

Los números siguen el **versionado semántico**, `MAJOR.MINOR.PATCH`:

- **PATCH** (`0.1.0 → 0.1.1`) — correcciones de errores compatibles hacia atrás.
- **MINOR** (`0.1.0 → 0.2.0`) — funciones nuevas, aún compatibles hacia atrás.
- **MAJOR** (`0.1.0 → 1.0.0`) — cambios que rompen la API existente.

Para publicar una versión nueva, sube el número (en ambos sitios) y fusiónalo a
través del [flujo de pull requests](../github/workflow.md) habitual.

## Adónde ir después

- [Instalación y uso](installation-and-usage.md) — instala este paquete e
  impórtalo.
- [API](api.md) — diseña la interfaz pública que expondrá `__init__.py`.
