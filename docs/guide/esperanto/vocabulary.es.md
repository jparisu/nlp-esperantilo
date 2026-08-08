# Vocabulario

Donde [Gramática](grammar.md) da las *reglas*, esta página da las **listas** — los
datos concretos que cargará la biblioteca: las palabras vacías, el inventario
completo de afijos, y un conjunto inicial de raíces comunes. Las listas de aquí
están pensadas para copiarse directamente a los recursos de la biblioteca.

## Palabras vacías

Las **palabras vacías** (*stop-words*) son palabras de alta frecuencia que, por sí
solas, aportan poco significado — el artículo, las preposiciones, las
conjunciones, los pronombres, los correlativos y los adverbios comunes. Una tubería
de PLN suele filtrarlas antes del análisis, para que `la`, `de`, `kaj` y `mi` no
ahoguen a las palabras con contenido.

Las palabras vacías del Esperanto son fáciles de enumerar porque la mayoría
pertenecen a las clases pequeñas y cerradas descritas en [Gramática](grammar.md):
el único artículo `la`, los pronombres personales, los 45 correlativos, y un
conjunto fijo de preposiciones y conjunciones.

!!! abstract "La lista completa ya existe como datos"
    Este proyecto distribuye la lista completa como un archivo legible por máquina,
    renderizado aquí automáticamente:

    **[Palabras vacías →](word-lists/ignorindaj-vortoj.md)** — 122 entradas, cada
    una con su traducción al inglés, su categoría gramatical y su procedencia. Se
    genera a partir de `resources/esperanto/vortoj.json`, el mismo archivo que
    leerá la biblioteca en tiempo de ejecución, de modo que la documentación y los
    datos nunca pueden discrepar.

### Solo raíces

122 entradas es una lista corta, y a propósito. El Esperanto construye palabras
añadiendo morfemas a una raíz, así que una lista escrita palabra por palabra se
repite: `mi`, `mia`, `min` y `mian` son un pronombre y tres terminaciones;
`esti`, `estas`, `estis`, `estos`, `estus` y `estu` son un verbo y cinco.

Por eso el léxico guarda **raíces, no formas**. Una entrada se gana su sitio solo
si *no* puede construirse a partir de otra entrada más una regla escrita en este
sitio. Con ese criterio se eliminaron 131 de las 252 entradas originales:

| Eliminado | Se construye desde | Regla |
| --- | --- | --- |
| `mia`, `min`, `mian`, `nia`, `ĝin`, … | el pronombre `mi`, `ni`, `ĝi`, … | [Gramática § Pronombres personales](grammar.md#pronombres-personales) |
| `unua`, `dua`, `deka`, … | el cardinal `unu`, `du`, `dek`, … | [Gramática § Números](grammar.md#numeros-y-composicion) |
| `estas`, `havis`, `povus`, … | el infinitivo `esti`, `havi`, `povi` | [Gramática § Sistema verbal](grammar.md#sistema-verbal) |
| las 59 entradas de correlativos | cinco prefijos × nueve terminaciones | [Gramática § Correlativos](grammar.md#correlativos) |
| `malantaŭ`, `sinjorino`, `supren` | `antaŭ`, `sinjoro`, `supre` | [§ Afijos](#afijos), más abajo |
| `bv`, `s-ro`, `d-ro`, `k`, … | nada — véase [§ Abreviaturas](#abreviaturas) | — |

A cambio se *añadieron* cinco raíces, porque había formas cuya raíz faltaba:
`bona`, `feliĉa`, `bonvoli`, `fraŭlo` y `supre`.

!!! warning "La lista y el lematizador van juntos"
    Una lista de solo raíces es más pequeña *y* más débil por sí sola: `token in
    stop_words` ya no atrapa `estas` ni `min`. Solo es correcta para una tubería
    que normaliza primero — quitar las terminaciones y después buscar. Filtrar
    tokens en bruto contra esta lista dejará pasar las palabras vacías flexionadas.

Una muestra representativa, por categoría:

| Categoría | Ejemplos |
| --- | --- |
| Artículo | `la` |
| Preposiciones | `al`, `de`, `en`, `kun`, `por`, `pri`, `sur`, `sub`, `tra` |
| Conjunciones | `kaj`, `aŭ`, `sed`, `ke`, `ĉar`, `se`, `nek` |
| Pronombres | `mi`, `vi`, `li`, `ŝi`, `ĝi`, `ni`, `ili`, `oni`, `si` |
| Adverbios comunes | `ankaŭ`, `ankoraŭ`, `jam`, `nur`, `tre`, `tro`, `plu` |
| Verbos | `esti`, `havi`, `povi` — solo infinitivos |

Los correlativos también son palabras vacías, los 45, pero no están en el archivo:
los genera la [tabla](grammar.md#correlativos).

El resto — *por qué* califica cada palabra y de dónde vienen las entradas— vive con
la [lista generada](word-lists/ignorindaj-vortoj.md); esta página solo resume.

## Afijos

Los afijos son los datos de vocabulario más importantes para un **lematizador**: le
permiten descomponer una palabra derivada de vuelta a su raíz. Abajo está el
inventario completo presentado en [Gramática § Afijos](grammar.md#afijos), agrupado
por función y listo para codificar.

### Terminaciones gramaticales (flexivas)

Estas se quitan primero, en orden inverso, para llegar a la base:

| Grupo | Terminaciones |
| --- | --- |
| Clase de palabra | `-o` (sustantivo), `-a` (adjetivo), `-e` (adverbio), `-i` (verbo inf.) |
| Número / caso | `-j` (plural), `-n` (acusativo), `-jn` (ambos) |
| Tiempo / modo verbal | `-as`, `-is`, `-os`, `-us`, `-u`, `-i` |

### Prefijos derivativos

| Prefijo | Función | Ejemplo |
| --- | --- | --- |
| `mal-` | opuesto | `malbona` (malo) |
| `ge-` | ambos sexos | `gepatroj` (padres) |
| `ek-` | súbito / incoativo | `ekiri` (ponerse en marcha) |
| `re-` | de nuevo / de vuelta | `reveni` (volver) |
| `dis-` | dispersión | `disdoni` (repartir) |
| `mis-` | erróneamente | `miskompreni` (entender mal) |
| `bo-` | parentesco político | `bopatro` (suegro) |
| `pra-` | primordial / bis- | `praavo` (bisabuelo) |

### Sufijos derivativos

| Sufijo | Función | Ejemplo |
| --- | --- | --- |
| `-in-` | femenino | `patrino` (madre) |
| `-ist-` | profesional | `instruisto` (profesor/a) |
| `-ej-` | lugar | `lernejo` (escuela) |
| `-il-` | herramienta | `tranĉilo` (cuchillo) |
| `-ar-` | colección | `arbaro` (bosque) |
| `-et-` | diminutivo | `dometo` (casita) |
| `-eg-` | aumentativo | `domego` (casona) |
| `-ul-` | persona | `junulo` (un/a joven) |
| `-an-` | miembro | `urbano` (ciudadano/a) |
| `-ec-` | cualidad abstracta | `boneco` (bondad) |
| `-ig-` | hacer / causar | `grandigi` (agrandar) |
| `-iĝ-` | volverse | `ruĝiĝi` (enrojecer) |
| `-ind-` | digno de | `aminda` (digno de amor) |
| `-em-` | inclinado a | `laborema` (trabajador) |
| `-aĉ-` | peyorativo | `domaĉo` (casucha) |

!!! tip "Orden de pelado para la lematización"
    Para recuperar la raíz de una palabra como `malsanulejojn`, pela de fuera hacia
    dentro: `-n` → `-j` → `-o` (terminaciones), luego `-ej-`, `-ul-` (sufijos), y
    luego el prefijo `mal-`, dejando `san-` ("salud"). Cada paso es una búsqueda en
    una tabla.

## Abreviaturas

Las abreviaturas son el único grupo que la regla de solo raíces no puede
regenerar. `s-ro` no es `sinjoro` más una terminación — ningún recorte lo produce
—, así que sacarlo del léxico obliga a escribirlo aquí. Una tubería que quiera
expandirlas necesita esta tabla como datos:

| Abreviatura | Expansión | Significado |
| --- | --- | --- |
| `bv` | `bonvolu` | por favor |
| `d-ro` | `doktoro` | Dr. |
| `ekz` | `ekzemple` | p. ej., por ejemplo |
| `f-no` | `fraŭlino` | Srta. |
| `k` | `kaj` | y |
| `s-no` | `sinjorino` | Sra. |
| `s-ro` | `sinjoro` | Sr. |

El patrón detrás de casi todas es *primera letra, guion, última sílaba*: `s-ro` ←
`s(injo)ro`. Es una convención, no una regla, y las variantes son reales — `s-ino`
es tan común como `s-no`. Trata la tabla como cerrada y amplíala a mano.

## Raíces más comunes

Un lematizador también se beneficia de una lista de **raíces** conocidas, tanto
para validar una descomposición como para captar las palabras frecuentes que
aparecen por todas partes. Un conjunto inicial de raíces muy comunes, por clase:

=== "Verbos"

    | Raíz | Significado | | Raíz | Significado |
    | --- | --- | --- | --- | --- |
    | `est-` | ser/estar | | `pov-` | poder |
    | `hav-` | tener | | `vol-` | querer |
    | `far-` | hacer | | `dev-` | deber |
    | `ir-` | ir | | `sci-` | saber (hechos) |
    | `ven-` | venir | | `pens-` | pensar |
    | `vid-` | ver | | `dir-` | decir |
    | `don-` | dar | | `pren-` | tomar |
    | `leg-` | leer | | `skrib-` | escribir |
    | `manĝ-` | comer | | `labor-` | trabajar |
    | `am-` | amar | | `help-` | ayudar |

=== "Sustantivos"

    | Raíz | Significado | | Raíz | Significado |
    | --- | --- | --- | --- | --- |
    | `hom-` | ser humano | | `mond-` | mundo |
    | `vir-` | hombre | | `temp-` | tiempo |
    | `infan-` | niño/a | | `tag-` | día |
    | `dom-` | casa | | `jar-` | año |
    | `urb-` | ciudad | | `akv-` | agua |
    | `land-` | país | | `lum-` | luz |

=== "Adjetivos"

    | Raíz | Significado | | Raíz | Significado |
    | --- | --- | --- | --- | --- |
    | `bon-` | bueno | | `bel-` | bello |
    | `grand-` | grande | | `long-` | largo |
    | `nov-` | nuevo | | `alt-` | alto |

Esto es solo una semilla. Una lista de producción se deriva mejor por frecuencia a
partir de un [corpus](resources.md#corpus); la idea aquí es que las raíces, como
todo lo demás en Esperanto, son una lista finita que la biblioteca puede guardar en
un archivo.

## Formato

Todas estas listas se almacenan de la misma forma, como **archivos JSON bajo
`resources/`**, para que una única fuente de verdad pueda alimentar tanto el
código (en tiempo de ejecución) como la documentación (en tiempo de construcción,
mediante
[`docs/hooks/word_lists.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/docs/hooks/word_lists.py)).
Los nombres de los campos están en Esperanto, coincidiendo con los nombres de
archivo; los campos traducibles son objetos indexados por locale:

```jsonc
{
  "id": "ignorindaj-vortoj",          // también la URL de la página generada
  "titolo": { "eo": "Ignorindaj vortoj", "en": "Stop-words" },
  "lingvo": "eo",
  "tradukoj": ["en"],                 // locales presentes en "traduko"
  "kategorioj": {                     // categorías gramaticales usadas abajo
    "prepozicio": { "en": "Preposition" }
  },
  "vortoj": [
    {
      "vorto": "kun",                 // la palabra, en minúsculas
      "kategorio": "prepozicio",      // una clave de "kategorioj"
      "traduko": { "en": ["with"] },
      "fontoj": ["stopwords-iso"]     // procedencia, opcional
    }
  ]
}
```

La construcción de la documentación solo exige `id`, `titolo` y `vortoj`, pero
[`tests/test_resources.py`](../python-library/testing.md#la-estructura-tests) es
más estricto: `id` debe coincidir con el nombre del archivo, y cada `vorto` debe
estar en minúsculas, ser única, llevar un `traduko` y usar una `kategorio`
declarada en `kategorioj`. Los archivos son UTF-8 y conservan los diacríticos
reales (`ĉ ĝ ĥ ĵ ŝ ŭ`), nunca el sistema x. Así, una edición mal formada falla en
CI en lugar de en una construcción de la documentación. El esquema completo está
documentado en `resources/README.md`.

Usar una lista desde la biblioteca es entonces cosa de dos líneas:

```python
import json
from pathlib import Path

data = json.loads(Path("resources/esperanto/vortoj.json").read_text(encoding="utf-8"))
stop_words = {entry["vorto"] for entry in data["vortoj"]}
```

## Adónde ir después

- [Listas de palabras](word-lists/index.md) — las páginas de datos generadas.
- [Recursos](resources.md) — diccionarios y corpus para ampliar estas listas.
