# API

La **API** (Application Programming Interface, interfaz de programación de
aplicaciones) de una biblioteca es su *cara pública*: los objetos, funciones
y métodos que los usuarios están destinados a tocar. Todo lo demás es un detalle de
implementación que eres libre de cambiar. Diseñar bien esa *cara* es lo que
separa una biblioteca que la gente disfruta usando de una con la que pelea.

El paquete `esperantilo` expone hasta ahora una clase y una función, así que la mayor
parte de esta página es un **objetivo de diseño**: muestra cómo es una interfaz
de NLP.

!!! tip "La parte que ya existe"
    Todo lo que viene a continuación está ilustrado por código real y publicado:
    [Biblioteca → Referencia de la API](../../library/api.md) es la superficie
    pública actual de `esperantilo`, generada desde sus docstrings. Lee esta
    página para saber *por qué* una API es como es, y aquella para saber *qué*
    ofrece la biblioteca hoy.

## Qué es aquí una API

Piensa en una biblioteca como si tuviera dos caras:

- la **API pública** — lo que los usuarios importan y llaman, y lo que prometes
  mantener estable entre versiones;
- las **entrañas** — funciones auxiliares, módulos privados y estructuras de datos
  que hacen que funcione, y que puedes reescribir en cualquier momento.

El valor de la distinción es la libertad: mientras la API pública mantenga su
forma, puedes refactorizar todo lo que hay detrás sin romperle nada a ningún
usuario. La primera tarea del diseño de una API es, por tanto, **decidir qué es
público** y hacer que esa frontera sea obvia.

En Python, la frontera se traza por convención y con `__all__`:

- Los nombres con un guion bajo por delante (`_helper`, `_Cache`) son **privados**
  — una señal de que los usuarios no deberían depender de ellos.
- La lista `__all__` de un módulo nombra sus objetos **públicos**. Documenta la
  superficie prevista y controla qué trae `from esperantilo import *`:

Así es como lo hace hoy `esperantilo`, con su API pública declarada explícitamente en `__init__.py`:

```python
# esperantilo/__init__.py
from esperantilo.nlp import sentence_tokenizer
from esperantilo.wiki import WikiPage

__version__ = "0.1.0"

__all__ = ["__version__", "WikiPage", "sentence_tokenizer"]   # la API pública, declarada explícitamente
```

Con esto, un usuario escribe `from esperantilo import WikiPage` y nunca tiene que
saber que la clase vive realmente en `esperantilo.wiki.wiki`, ni que esta se
apoya en un módulo privado `esperantilo.wiki._wiki_api` que puede cambiar sin
aviso.

La lista completa, generada desde el propio código, está en
[Biblioteca → Referencia de la API](../../library/api.md).

## Cómo diseñar una buena API

Un puñado de principios hacen que una interfaz sea predecible y agradable. Son los
mismos que hacen que [scikit-learn y spaCy](library.md#un-ejemplo-concreto) sean
fáciles de aprender:

- **Consistencia.** Las cosas similares deberían parecerse. Si un `Doc` es
  iterable y produce `Token`s, entonces cualquier colección de la biblioteca
  debería ser iterable de la misma forma.
- **Firmas pequeñas y predecibles.** Pocos parámetros, valores por defecto
  sensatos y sin sorpresas. `parse(text)` debería funcionar sin más; las opciones
  son extras, no obligaciones.
- **Nombres con sentido.** `lemma`, `pos`, `is_stop` dicen lo que son. Evita
  abreviaturas que solo entienda quien las escribió.
- **Anotaciones de tipo (type hints).** Anota los parámetros y los tipos de
  retorno. Documentan la interfaz, habilitan el autocompletado del editor y
  permiten que las herramientas detecten errores antes de la ejecución.
- **Docstrings.** Cada objeto público lleva un docstring breve que dice qué hace,
  qué recibe y qué devuelve.

```python
def parse(text: str) -> "Doc":
    """Analyse Esperanto ``text`` and return a :class:`Doc`.

    Args:
        text: the raw Esperanto text to analyse.

    Returns:
        A ``Doc`` holding the analysed tokens.
    """
    ...
```

Los type hints (`text: str`, `-> "Doc"`) y el docstring, juntos, le dicen al
usuario todo lo que necesita para llamar a `parse` correctamente, sin leer su
cuerpo.

## Una API al estilo de spaCy

[spaCy](https://spacy.io) es el modelo de referencia para este proyecto. Vale la
pena copiar su diseño porque convierte el desordenado procesamiento de texto en un
pequeño conjunto de objetos tipados y predecibles. La idea central: **analizar
texto devuelve un `Doc`, y un `Doc` es una secuencia de `Token`s**, cada uno con
sus atributos lingüísticos.

Esta es la forma de spaCy, que la biblioteca de Esperanto aspira a reflejar:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The quick brown fox jumps.")   # -> un Doc

for token in doc:                          # un Doc es iterable sobre Tokens
    print(token.text, token.lemma_, token.pos_, token.is_stop)
```

```text
The    the    DET    True
quick  quick  ADJ    False
brown  brown  ADJ    False
fox    fox    NOUN   False
jumps  jump   VERB   False
.      .      PUNCT  False
```

Dos objetos tipados sostienen todo el modelo:

| Objeto | Qué representa | Atributos típicos |
| --- | --- | --- |
| **`Doc`** | Un fragmento de texto analizado | iterable de `Token`, `text`, `sents` |
| **`Token`** | Una sola palabra/unidad | `text`, `lemma`, `pos`, `is_stop` |

Aplicado al Esperanto —donde la [gramática regular](../esperanto/grammar.md) hace
que estos atributos sean calculables por reglas— la interfaz objetivo tiene este
aspecto:

```python
# API objetivo ilustrativa para esperantilo.
import esperantilo

doc = esperantilo.parse("La rapida vulpo saltas.")

for token in doc:
    print(token.text, token.lemma, token.pos, token.is_stop)
```

```text
La      la      DET     True
rapida  rapida  ADJ     False
vulpo   vulpo   NOUN    False
saltas  salti   VERB    False
.       .       PUNCT   False
```

Fíjate en cómo las terminaciones del Esperanto se corresponden limpiamente con los
atributos — `-a` → adjetivo, `-o` → sustantivo, `-as` → verbo en presente (con
lema `salti`), y `la` es una palabra vacía (stop-word). Esa regularidad, descrita
en la [sección de Esperanto](../esperanto/grammar.md), es exactamente lo que hace
viable una implementación de `Doc` / `Token` basada en reglas.

Para la referencia completa a imitar —nombres de métodos, nombres de atributos y
relaciones entre objetos— véase la
[documentación de la API de spaCy](https://spacy.io/api).

## Documentar la API automáticamente

Una referencia de API escrita a mano se queda obsoleta rápidamente:
alguien renombra un parámetro y la página sigue mostrando el antiguo.
La solución es generar la página **desde los docstrings**, de forma que solo haya una copia de la verdad.

[mkdocstrings](https://mkdocstrings.github.io/) hace eso en MkDocs. Una página
que no contiene más que una directiva:

```markdown
::: esperantilo.nlp
    options:
      members:
        - sentence_tokenizer
```

renderiza la firma, las anotaciones de tipo, la tabla de argumentos y los
ejemplos de cada objeto listado, cada uno con un enlace a las líneas de código de
las que salió. Así es exactamente como se construye
[Biblioteca → Referencia de la API](../../library/api.md); el fuente de esa
página son [cuatro directivas y un párrafo](https://github.com/jparisu/nlp-esperantilo/blob/main/docs/library/api.md).

Dos hábitos hacen que la página generada merezca la pena:

- **Escribe los docstrings en un estilo consistente.** Este proyecto usa el
  estilo Google mostrado arriba (`Args:`, `Returns:`, `Examples:`), declarado una
  sola vez en `mkdocs.yml`.
- **Pon los ejemplos en bloques `Examples:`.** Escritos como sesiones `>>>` son a
  la vez documentación y [doctests](testing.md) — la CI los ejecuta, así
  que no pueden quedarse desfasados en silencio.

## Adónde ir después

- [Biblioteca → Referencia de la API](../../library/api.md) — las mismas ideas,
  aplicadas: la superficie pública real de `esperantilo`, generada desde su
  código.
- [Pruebas](testing.md) — cómo verificar que la API se comporta según su diseño.
- [Esperanto § Gramática](../esperanto/grammar.md) — las reglas que codificará la
  API.
