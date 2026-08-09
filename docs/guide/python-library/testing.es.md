# Pruebas

Las pruebas son código que comprueba tu código. Son lo que te permite cambiar una
biblioteca con confianza: si un cambio rompe algo, una prueba lo detecta al
instante en lugar de que un usuario se entere más tarde. Esta página explica por
qué importan, cómo se organiza la carpeta `tests/`, cómo escribirlas y ejecutarlas
con **pytest**, y cómo se convierten en una puerta automática en cada pull request.

## Por qué pruebas unitarias

Una **prueba unitaria** ejercita una pieza pequeña de la biblioteca de forma
aislada y afirma que se comporta como se espera. Su verdadero valor aflora con el
tiempo:

- **Detectan regresiones.** Cuando cambias el tokenizador, las pruebas te dicen al
  momento si rompiste el lematizador que depende de él.
- **Hacen segura la refactorización.** Puedes reescribir las entrañas de la
  [API](api.md) con libertad, porque una suite que pasa demuestra que el
  comportamiento público no ha cambiado.
- **Documentan el comportamiento.** Una prueba es un ejemplo ejecutable de cómo se
  supone que se llama a una función y qué debería devolver.
- **Habilitan la colaboración.** En un equipo, las pruebas son cómo confías en el
  pull request de un compañero sin releerlo entero — las comprobaciones están en
  verde.

El coste es pequeño y se paga una vez; el beneficio se acumula cada vez que el
código cambia.

## La estructura `tests/`

Las pruebas viven en una carpeta `tests/` de nivel superior, mantenida fuera del
paquete que se distribuye (véase [Organización](organization.md)). La suite
**refleja el código fuente**: cada parte de la biblioteca tiene su archivo
`test_*.py` correspondiente, de modo que es obvio dónde vive una prueba y dónde
falta.

```text
tests/
├── test_package.py     # el paquete se importa y expone su API pública
├── test_resources.py   # los archivos de datos son válidos
└── test_tokenizer.py   # la segmentación en frases se comporta como se documenta
```

Fíjate en el emparejamiento: `test_tokenizer.py` acompaña a
`src/esperantilo/nlp/tokenizer.py`, cuyo comportamiento se describe en
[Biblioteca → Segmentación en frases](../../library/sentence-segmentation.md).
Un módulo de código, un módulo de pruebas: en eso consiste toda la convención.

Dos convenciones de nombres permiten a pytest **descubrir** las pruebas
automáticamente, sin registro:

- los *archivos* de prueba se llaman `test_*.py`,
- las *funciones* de prueba se llaman `test_*`.

La prueba de humo de este proyecto muestra la forma — importa la cosa, luego afirma
algo sobre ella:

```python
# tests/test_package.py
import esperantilo


def test_package_is_importable():
    assert esperantilo is not None


def test_version_is_exposed():
    assert isinstance(esperantilo.__version__, str)
    assert esperantilo.__version__
```

Cada función prueba un hecho, y su nombre dice cuál es ese hecho — de modo que un
informe de fallo se lee como una frase: `test_version_is_exposed failed`.

## Escribir y ejecutar pruebas con `pytest`

[pytest](https://docs.pytest.org/) es el ejecutor de pruebas estándar de facto de
Python. Instálalo mediante el extra de pruebas y ejecuta toda la suite con una
palabra:

```bash
pip install -e ".[test]"
pytest
```

!!! tip "`pytest` funciona sin instalar nada"
    El paquete vive bajo `src/`, que Python no busca por defecto, así que un
    `pytest` a secas en un clon recién hecho fallaría con
    `No module named 'esperantilo'`. `pythonpath = ["src"]` en `pyproject.toml`
    lo pone en la ruta durante las pruebas, así que `pytest` funciona nada más
    hacer `git clone`.

```console
$ pytest
===================== test session starts =====================
configfile: pyproject.toml
testpaths: tests, src
collected 300 items

tests/test_package.py ........                            [  2%]
tests/test_resources.py ...........................       [ 18%]
tests/test_tokenizer.py .............xxx                  [ 97%]
src/esperantilo/nlp/tokenizer.py .                        [ 97%]
src/esperantilo/wiki/_wiki_api.py ..                      [ 98%]
src/esperantilo/wiki/wiki.py .....                        [100%]

=============== 297 passed, 3 xfailed in 0.13s ================
```

Las funciones del día a día que usarás:

- **Aserciones.** Simples sentencias `assert` — pytest las reescribe para mostrar
  los valores reales en caso de fallo, así que rara vez necesitas nada más.
- **Parametrización.** Ejecuta la misma prueba sobre muchas entradas con
  `@pytest.mark.parametrize`, en lugar de copiar y pegar. Este proyecto la usa para
  ejecutar las mismas comprobaciones sobre *cada* archivo de `resources/`:

    ```python
    @pytest.mark.parametrize("path", FILES, ids=lambda p: p.name)
    def test_mandatory_fields(path):
        data = json.loads(path.read_text(encoding="utf-8"))
        for field in ("id", "titolo", "vortoj"):
            assert field in data, f"missing '{field}'"
    ```

- **Fixtures.** Preparación reutilizable compartida entre pruebas (un documento de
  ejemplo, un archivo temporal), declarada una vez y solicitada por su nombre.
- **Ejecutar un subconjunto** mientras te centras en un área:

    ```bash
    pytest tests/test_package.py           # un archivo
    pytest -k version                      # pruebas cuyo nombre contiene "version"
    pytest -x                              # para en el primer fallo
    ```

!!! tip "Prueba el comportamiento, no la implementación"
    Afirma sobre lo que una función *devuelve o hace*, no sobre cómo lo hace. Así
    tus pruebas siguen pasando a través de refactorizaciones internas y solo fallan
    cuando el comportamiento realmente cambia — que es de lo que se trata.

## Pruebas en integración continua

Ejecutar las pruebas en local está bien; ejecutarlas **automáticamente en cada
cambio** es lo que las convierte en una verdadera red de seguridad. El
[workflow `tests.yml`](../github/actions.md#ejecutar-las-pruebas-de-python) ejecuta
`pytest` en cada push y pull request a `main`, de modo que un cambio roto se señala
en GitHub antes de que nadie lo fusione.

El paso final es hacer que esa comprobación sea **obligatoria**: con la
[protección de ramas](../github/repository-configuration.md#comprobaciones-de-estado-obligatorias),
un pull request no puede fusionarse mientras sus pruebas estén en rojo. El `pytest`
local, la CI y la protección de ramas forman entonces una cadena — detectas
problemas pronto, la CI detecta lo que se te escapó, y las reglas se aseguran de que
nada roto llegue a `main`.

## Adónde ir después

- [GitHub Actions](../github/actions.md) — el workflow que ejecuta estas pruebas.
- [Esperanto](../esperanto/index.md) — las reglas lingüísticas que codificará la
  biblioteca, y sus pruebas.
- [Biblioteca → Segmentación en frases](../../library/sentence-segmentation.md) —
  el comportamiento que fija
  [`tests/test_tokenizer.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py),
  y un ejemplo trabajado de las convenciones de esta página.
