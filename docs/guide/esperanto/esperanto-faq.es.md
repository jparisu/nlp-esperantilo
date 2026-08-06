# Preguntas frecuentes

Preguntas habituales sobre el Esperanto y sobre convertirlo en datos para la
biblioteca. Cada respuesta enlaza a la página donde el tema se trata en detalle.

??? question "¿Qué es el Esperanto, en una frase?"
    Una lengua auxiliar internacional construida, publicada por L. L. Zamenhof en
    1887, diseñada para ser **regular y fácil de aprender** — sin excepciones
    gramaticales. Véase [Historia](history.md).

??? question "¿Por qué construir una biblioteca de PLN para el Esperanto en concreto?"
    Porque su gramática es completamente regular, así que un tokenizador,
    lematizador y etiquetador morfosintáctico **basados en reglas** son realmente
    viables — las terminaciones y los afijos siguen reglas que nunca se rompen, a
    diferencia de las lenguas naturales. Véase
    [Historia § Por qué importa aquí](history.md#por-que-importa-aqui).

??? question "¿Cómo sé la categoría gramatical de una palabra?"
    Por su vocal final: `-o` es un sustantivo, `-a` un adjetivo, `-e` un adverbio,
    `-i` un verbo en infinitivo. Esta sola regla cubre la mayoría de las palabras
    con contenido. Véase
    [Gramática § Terminaciones de clase de palabra](grammar.md#terminaciones-de-clase-de-palabra).

??? question "¿Cómo funciona la lematización en Esperanto?"
    Pela las terminaciones gramaticales y los afijos de una palabra hasta llegar a
    su raíz, luego vuelve a añadir la vocal de clase. `malsanulejojn` → quita `-n`,
    `-j`, `-o`, luego `-ej-`, `-ul-`, `mal-` → raíz `san-`. Cada paso es una
    búsqueda en una tabla. Véase [Vocabulario § Afijos](vocabulary.md#afijos).

??? question "¿Qué son los correlativos?"
    Una rejilla regular de 5 × 9 con 45 palabras comunes (este/ese/cuál/algún/todo/
    ningún × cosa/persona/lugar/tiempo…), cada una un prefijo más una terminación.
    Aprende la rejilla y obtienes las 45. Véase
    [Gramática § Correlativos](grammar.md#correlativos).

??? question "¿Para qué sirve el acusativo `-n`?"
    Marca el **objeto directo** de un verbo (y la dirección del movimiento). Lo
    toman tanto los sustantivos como sus adjetivos, y se apila después del plural
    `-j`: `interesajn librojn`. Véase
    [Gramática § Flexiones gramaticales](grammar.md#flexiones-gramaticales).

??? question "¿Cómo debo manejar las letras especiales `ĉ ĝ ĥ ĵ ŝ ŭ` en el código?"
    Trátalas como letras Unicode corrientes y **normaliza** la entrada a una única
    forma canónica (NFC, diacríticos reales) antes de tokenizar, convirtiendo el
    sistema x (`cx`, `gx`, …) o el sistema h si están presentes. Véase
    [Gramática § Alfabeto](grammar.md#alfabeto).

??? question "¿Qué cuenta como palabra vacía en Esperanto?"
    El artículo `la`, los pronombres, los correlativos, y un conjunto fijo de
    preposiciones, conjunciones y adverbios comunes — en su mayoría clases cerradas,
    así que la lista es finita. Este proyecto distribuye 250 de ellas. Véase
    [Vocabulario § Palabras vacías](vocabulary.md#palabras-vacias).

??? question "¿De dónde saca la biblioteca sus listas de palabras?"
    De archivos JSON bajo `resources/`, que son la única fuente de verdad: la
    documentación los renderiza en tiempo de construcción y la biblioteca leerá
    esos mismos archivos en tiempo de ejecución, de modo que nunca pueden
    discrepar. Véase [Vocabulario § Formato](vocabulary.md#formato).

??? question "¿Dónde encuentro texto real en Esperanto para probar la biblioteca?"
    En corpus como el [Tekstaro de Esperanto](https://tekstaro.com), la Wikipedia
    en Esperanto, y libros de dominio público en Project Gutenberg — atento a la
    licencia de cada fuente. Véase [Recursos § Corpus](resources.md#corpus).

??? question "¿Es fiable el contenido gramatical de aquí?"
    Sigue *A Complete Grammar of Esperanto* de Ivy Kellerman Reed (1910), una
    referencia de dominio público incluida en el repositorio. Véase
    [Recursos § Libros](resources.md#libros).
