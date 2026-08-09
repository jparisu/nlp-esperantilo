# Gramática

Esta es la página de referencia central de la sección de Esperanto. Reúne las
reglas que necesita una tubería (*pipeline*) basada en reglas — para el
tokenizador, el lematizador, el etiquetador morfosintáctico y el manejo de
palabras vacías. Como la morfología del Esperanto no tiene excepciones, cada regla
de abajo puede convertirse casi directamente en código.

La idea rectora: una palabra en Esperanto se construye a partir de una **raíz** más
**terminaciones gramaticales** y **afijos** opcionales. Quita las terminaciones y
los afijos y tienes el lema; lee las terminaciones y tienes la categoría gramatical
y la flexión.

!!! note "Qué deja fuera esta página"
    Los **participios** (`-ant-`, `-int-`, `-ont-` activos; `-at-`, `-it-`, `-ot-`
    pasivos), los tiempos compuestos que se forman con ellos y `esti`, y la voz
    pasiva son igual de regulares, pero aquí no se cubren. Una tubería que
    implemente solo las reglas de abajo analizará mal formas como `leganta`,
    `legita` o `estas legata`.

!!! quote "Referencia"
    Las reglas y los ejemplos de esta página siguen la clásica **_A Complete
    Grammar of Esperanto_** de Ivy Kellerman Reed (1910), una obra de dominio
    público incluida en el repositorio en `resources/esperanto/books/esperanto_grammar.txt`.
    Véase [Recursos § Libros](resources.md#libros) para la cita completa.

## Alfabeto

El Esperanto usa un alfabeto latino de **28 letras**. Es estrictamente
**fonético**: cada letra se pronuncia siempre igual, y cada sonido se escribe con
exactamente una letra. Seis letras llevan diacríticos: las cinco consonantes con
circunflejo no las usa ninguna otra lengua, y `ŭ` aparece también en el alfabeto
latino del bielorruso.

| Letra | Nombre | Sonido (aprox.) |
| --- | --- | --- |
| `ĉ` | ĉo | *ch* de "chico" |
| `ĝ` | ĝo | *j* inglesa de "jam" (sonora) |
| `ĥ` | ĥo | *j* fuerte de "jamón" |
| `ĵ` | ĵo | *j* francesa de "jour" |
| `ŝ` | ŝo | *sh* inglesa de "show" |
| `ŭ` | ŭo | *u* breve en diptongos, como en "auto" |

Las letras `q`, `w`, `x`, `y` **no** forman parte del alfabeto.

!!! warning "La codificación importa para la tokenización"
    Los diacríticos son letras Unicode reales (`ĉ` es U+0109), no una `c` más una
    marca combinante — pero el texto que se encuentra por ahí puede usar cualquiera
    de las dos formas. También existen dos alternativas en ASCII para teclados que
    no pueden escribir los diacríticos:

    - el **sistema x**: `cx gx hx jx sx ux` para `ĉ ĝ ĥ ĵ ŝ ŭ`;
    - el **sistema h** (del *Fundamento*): `ch gh hh jh sh u`.

    Un tokenizador robusto debería **normalizar** la entrada a una única forma
    canónica (Unicode NFC, diacríticos reales) antes de aplicar cualquier otra
    regla. Los archivos de datos de este proyecto conservan los diacríticos reales
    y nunca el sistema x (véase [`resources/README.md`](https://github.com/jparisu/nlp-esperantilo/blob/main/resources/README.md)).

## Terminaciones de clase de palabra

Esta es la regla más útil de todas para el etiquetado morfosintáctico y la
lematización: la **vocal final de una palabra completa marca su categoría
gramatical**.

| Terminación | Clase de palabra | Ejemplo | Raíz | Significado |
| --- | --- | --- | --- | --- |
| `-o` | sustantivo | `libro` | `libr-` | libro |
| `-a` | adjetivo | `bona` | `bon-` | bueno |
| `-e` | adverbio (derivado) | `rapide` | `rapid-` | rápidamente |
| `-i` | verbo (infinitivo) | `kanti` | `kant-` | cantar |

De una sola raíz obtienes toda la familia: `muziko` (música), `muzika` (musical),
`muzike` (musicalmente).

## Flexiones gramaticales

Los sustantivos y los adjetivos toman dos terminaciones opcionales, siempre
**después** de la vocal de clase:

| Terminación | Significado | Ejemplo |
| --- | --- | --- |
| `-j` | plural | `libroj` (libros), `bonaj` (buenos) |
| `-n` | acusativo (objeto directo) | `libron`, `bonan` |
| `-jn` | plural **y** acusativo | `bonajn librojn` |

Dos reglas las hacen completamente regulares:

- **Los adjetivos concuerdan** con su sustantivo en número y caso: *"la bonaj
  libroj"*, *"mi legas interesajn librojn"*.
- El orden es fijo: raíz → vocal de clase → `-j` → `-n`. Así, el análisis de
  `librojn` es `libr-` + `-o` (sustantivo) + `-j` (plural) + `-n` (acusativo).

El acusativo también marca la dirección del movimiento, pero para el análisis
morfológico lo que importa es el sufijo `-n`.

## Sistema verbal

Los verbos **no** se conjugan por persona ni número — solo por tiempo y modo, con
una sola terminación cada uno. La misma raíz toma cualquiera de estas:

| Terminación | Tiempo / modo | Ejemplo (`kant-`, cantar) |
| --- | --- | --- |
| `-as` | presente | `kantas` (canto / canta) |
| `-is` | pasado | `kantis` (cantó) |
| `-os` | futuro | `kantos` (cantará) |
| `-us` | condicional | `kantus` (cantaría) |
| `-u` | imperativo / volitivo | `kantu!` (¡canta!) |
| `-i` | infinitivo | `kanti` (cantar) |

`mi kantas`, `vi kantas`, `ili kantas` — el verbo nunca cambia según el sujeto.
Para lematizar un verbo, sustituye su terminación de tiempo/modo por `-i`
(`kantis → kanti`).

## El artículo

Hay **un** artículo, el determinado `la` ("el/la/los/las"). Es **invariable** —
sin plural, sin género, sin caso:

- `la libro` (el libro), `la libroj` (los libros), `la bona libro` (el buen libro).

**No hay artículo indeterminado**: `libro` significa tanto "un libro" como
simplemente "libro". `la` es una palabra vacía natural (véase
[Palabras vacías](word-lists/ignorindaj-vortoj.md)).

## Pronombres personales

Los pronombres son un conjunto pequeño y cerrado — ideal para codificar a mano:

| Pronombre | Significado | Posesivo (`+ -a`) |
| --- | --- | --- |
| `mi` | yo | `mia` |
| `vi` | tú / usted / vosotros | `via` |
| `li` | él | `lia` |
| `ŝi` | ella | `ŝia` |
| `ĝi` | ello (neutro) | `ĝia` |
| `ni` | nosotros | `nia` |
| `ili` | ellos/ellas | `ilia` |
| `oni` | uno / se (impersonal) | `onia` |
| `si` | reflexivo (sí mismo/a, se) | `sia` |

El **acusativo** de un pronombre añade `-n`: `min` (me), `vin`, `lin`, `ŝin`,
`nin`, `ilin`. Los posesivos son adjetivos corrientes, así que también flexionan:
`miajn librojn` (mis libros, acus. pl.).

## Correlativos

Los **correlativos** son una rejilla asombrosamente regular de 5 × 9 con 45
palabras comunes (este/ese/cuál/algún/todo/ningún + cosa/persona/lugar/tiempo/
razón…). Cada uno es un **prefijo** (la categoría de significado) más una
**terminación** (el tipo). Aprende la rejilla y obtienes las 45 gratis.

Los cinco prefijos:

| Prefijo | Significado |
| --- | --- |
| `ki-` | interrogativo / relativo ("qué", "cuál") |
| `ti-` | demostrativo ("ese") |
| `i-` | indefinido ("algún") |
| `ĉi-` | universal ("todo", "cada") |
| `neni-` | negativo ("ningún", "nada") |

Las nueve terminaciones y la tabla completa:

| Terminación → tipo | `ki-` | `ti-` | `i-` | `ĉi-` | `neni-` |
| --- | --- | --- | --- | --- | --- |
| `-o` cosa | kio | tio | io | ĉio | nenio |
| `-u` individuo | kiu | tiu | iu | ĉiu | neniu |
| `-a` clase | kia | tia | ia | ĉia | nenia |
| `-es` posesión | kies | ties | ies | ĉies | nenies |
| `-e` lugar | kie | tie | ie | ĉie | nenie |
| `-am` tiempo | kiam | tiam | iam | ĉiam | neniam |
| `-al` razón | kial | tial | ial | ĉial | nenial |
| `-el` manera | kiel | tiel | iel | ĉiel | neniel |
| `-om` cantidad | kiom | tiom | iom | ĉiom | neniom |

Los correlativos en `-u` y `-a` toman tanto `-j` como `-n` (`tiujn`, `kiuj`), como
los sustantivos y adjetivos a los que se parecen. Los de `-o` toman `-n` pero
**nunca** `-j` (`kion`, `tion` — no existe *tioj*), y los de `-e` toman `-n` para
marcar dirección (`tien`, `kien`). Las otras cinco terminaciones son invariables.

Los 45 son palabras vacías, y esta tabla es el único sitio donde el proyecto los
guarda: `resources/esperanto/vortoj.json` contiene raíces, no formas, así que se
espera que un lematizador genere la rejilla a partir de los dos ejes de arriba en
lugar de buscar las palabras. Véase
[`resources/README.md` § Roots, not forms](https://github.com/jparisu/nlp-esperantilo/blob/main/resources/README.md#roots-not-forms).

## Afijos

Los afijos son lo que hace **composicional** el vocabulario del Esperanto — y son
el corazón de la lematización, porque una palabra larga suele ser una raíz envuelta
en afijos. Se colocan *entre* la raíz y la terminación gramatical.

### Prefijos

| Prefijo | Significado | Ejemplo |
| --- | --- | --- |
| `mal-` | opuesto directo | `bona` → `malbona` (bueno → malo) |
| `ge-` | ambos sexos juntos | `patro` → `gepatroj` (padre → padres/progenitores) |
| `ek-` | inicio súbito / acción breve | `iri` → `ekiri` (ir → ponerse en marcha) |
| `re-` | de nuevo / de vuelta | `veni` → `reveni` (venir → volver) |
| `dis-` | separación, dispersión | `doni` → `disdoni` (dar → repartir) |
| `mis-` | erróneamente | `kompreni` → `miskompreni` (entender mal) |
| `bo-` | parentesco político | `patro` → `bopatro` (suegro) |
| `pra-` | primordial / bis- (parentesco) | `avo` → `praavo` (bisabuelo) |

### Sufijos

| Sufijo | Significado | Ejemplo |
| --- | --- | --- |
| `-in-` | femenino | `patro` → `patrino` (padre → madre) |
| `-ist-` | profesional / adepto | `instrui` → `instruisto` (profesor/a) |
| `-ej-` | lugar para | `lerni` → `lernejo` (aprender → escuela) |
| `-il-` | herramienta / instrumento | `tranĉi` → `tranĉilo` (cortar → cuchillo) |
| `-ar-` | colección / conjunto | `arbo` → `arbaro` (árbol → bosque) |
| `-et-` | diminutivo (más pequeño) | `domo` → `dometo` (casa → casita) |
| `-eg-` | aumentativo (más grande) | `domo` → `domego` (casa → casona) |
| `-ul-` | persona caracterizada por | `juna` → `junulo` (joven → un/a joven) |
| `-an-` | miembro / habitante | `urbo` → `urbano` (ciudad → ciudadano/a) |
| `-ec-` | cualidad abstracta | `bona` → `boneco` (bueno → bondad) |
| `-ig-` | hacer / causar | `granda` → `grandigi` (grande → agrandar) |
| `-iĝ-` | volverse / llegar a ser | `ruĝa` → `ruĝiĝi` (rojo → enrojecer) |
| `-ind-` | digno de | `ami` → `aminda` (amar → digno de amor) |
| `-em-` | inclinado a | `labori` → `laborema` (trabajar → trabajador) |
| `-aĉ-` | peyorativo (mala calidad) | `domo` → `domaĉo` (casa → casucha) |

Los afijos se apilan. `mal-san-ul-ej-o` = `mal-` (opuesto) + `san-` (salud) +
`-ul-` (persona) + `-ej-` (lugar) + `-o` (sustantivo) = **hospital** (literalmente
"lugar para personas no sanas"). Un lematizador que conozca esta tabla de afijos
puede descomponer tales palabras por reglas.

## Números y composición

Los números cardinales se construyen a partir de un puñado de raíces:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 100 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `nul` | `unu` | `du` | `tri` | `kvar` | `kvin` | `ses` | `sep` | `ok` | `naŭ` | `dek` | `cent` | `mil` |

Los números mayores se **componen** por yuxtaposición: `dek du` (12), `dudek`
(20), `dudek unu` (21), `cent tridek kvin` (135). Añadir terminaciones deriva
palabras relacionadas:

- ordinales con `-a`: `unua` (primero), `dua` (segundo);
- múltiplos con `-obl-`: `duobla` (doble);
- fracciones con `-on-`: `duono` (una mitad), `kvarono` (un cuarto);
- colectivos con `-op-`: `duope` (de dos en dos).

De forma más general, **dos raíces cualesquiera pueden componerse** en una sola
palabra, con la última raíz como núcleo: `vapor-ŝipo` (barco de vapor),
`dorm-o-ĉambro` (dormitorio, con una `-o-` de enlace para facilitar la
pronunciación). La clase de palabra del compuesto viene de su terminación final,
exactamente igual que en una raíz simple.

## Ejemplos resueltos

Juntando las reglas, aquí hay una frase analizada palabra por palabra:

> **La juna instruistino legas interesan libron.**
> *"La joven profesora está leyendo un libro interesante."*

| Palabra | Descomposición | Análisis |
| --- | --- | --- |
| `La` | `la` | artículo (palabra vacía) |
| `juna` | `jun-` + `-a` | adjetivo — "joven" |
| `instruistino` | `instru-` + `-ist-` + `-in-` + `-o` | sustantivo — "profesora" |
| `legas` | `leg-` + `-as` | verbo, presente — "lee" (lema `legi`) |
| `interesan` | `interes-` + `-a` + `-n` | adjetivo, acusativo — "interesante" |
| `libron` | `libr-` + `-o` + `-n` | sustantivo, acusativo — "libro" (lema `libro`) |

Un segundo ejemplo muestra el plural, la concordancia de acusativo y un
correlativo:

> **Ĉiuj miaj amikoj legas tiujn librojn.**
> *"Todos mis amigos están leyendo esos libros."*

`Ĉiuj` (correlativo `ĉiu` + `-j`), `miaj` (posesivo `mia` + `-j`), `amikoj`
(`amik-o-j`) — el sujeto es plural, así que nada toma `-n`; `tiujn librojn`
(`tiu-j-n`, `libr-o-j-n`) es el objeto en acusativo plural, y el demostrativo
concuerda con su sustantivo. Esta concordancia regular es precisamente lo que un
etiquetador basado en reglas puede verificar y aprovechar.

## Adónde ir después

- [Listas de palabras](word-lists/index.md) — la lista de palabras vacías completa,
  generada desde los datos que lee la biblioteca.
- [Biblioteca Python § API](../python-library/api.md) — cómo estas reglas se
  convierten en una interfaz `Doc` / `Token`.
