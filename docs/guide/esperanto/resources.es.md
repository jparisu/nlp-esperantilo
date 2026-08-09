# Recursos

Una lista curada de sitios para aprender Esperanto, buscar palabras y encontrar
texto contra el que probar la biblioteca. Las entradas están agrupadas por
propósito; las marcadas como **en-repo** se distribuyen con este proyecto.

## Cursos

Para aprender la lengua desde cero:

- **[lernu.net](https://lernu.net)** — un sitio multilingüe gratuito con cursos
  estructurados, explicaciones de gramática y un diccionario. El punto de partida
  más habitual.
- **[Duolingo — Esperanto](https://www.duolingo.com/course/eo/en)** — un curso
  gratuito y gamificado, bueno para crear un hábito diario y vocabulario básico.
- **[Kurso de Esperanto](https://www.kurso.com.br)** — un clásico curso
  audiovisual descargable.

Como la gramática es tan regular, la mayoría de las personas que aprenden alcanzan
una fluidez lectora básica mucho más rápido que con una lengua natural — lo cual es
conveniente cuando tu objetivo es *verificar una biblioteca lingüística* más que
convertirte en poeta.

## Libros

Gramáticas de referencia y lecturas:

- **_A Complete Grammar of Esperanto_**, Ivy Kellerman Reed (1910) — **en-repo** en
  `resources/esperanto/books/esperanto_grammar.txt`. Una gramática sistemática de dominio
  público con ejercicios graduados; es la referencia que sigue la
  [página de Gramática](grammar.md) de esta sección. También disponible como
  [eBook #7787 de Project Gutenberg](https://www.gutenberg.org/ebooks/7787).
- **_Fundamento de Esperanto_**, L. L. Zamenhof (1905) — el fundamento oficial e
  inmutable de la lengua (las dieciséis reglas, el *Universala Vortaro* y ejercicios
  modelo). La autoridad última sobre qué es Esperanto correcto.
- **_Plena Manlibro de Esperanta Gramatiko_** (PMEG) — una gramática descriptiva
  moderna y exhaustiva en Esperanto, disponible gratis en
  [bertilow.com/pmeg](https://bertilow.com/pmeg/). La mejor referencia en
  profundidad una vez que lees Esperanto con comodidad.

## Diccionarios

Para buscar raíces, afijos y significados:

- **[Reta Vortaro (ReVo)](https://www.reta-vortaro.de/)** — un diccionario
  monolingüe gratuito y construido por la comunidad, con traducciones a muchas
  lenguas y descargable en formato legible por máquina.
- **_Plena Ilustrita Vortaro_** (PIV) — el gran diccionario monolingüe de
  referencia, publicado por SAT; el estándar para definiciones autorizadas.
- **[Vortaro.net](https://vortaro.net)** — una cómoda interfaz en línea para PIV.
- **[esperanto12.net](https://esperanto12.net/en/tabelvortoj/)** — una referencia
  compacta de las clases cerradas, y el recorrido más claro por la
  [tabla de correlativos](grammar.md#correlativos) — las 45 palabras que el léxico
  deliberadamente no guarda.

!!! tip "Lo que quieres es legible por máquina"
    Para alimentar la biblioteca, prefiere fuentes que ofrezcan una **exportación
    estructurada** (los archivos de datos de ReVo, listas de palabras) frente a los
    diccionarios en prosa. Pueden convertirse al formato JSON descrito en
    [`resources/README.md`](https://github.com/jparisu/nlp-esperantilo/blob/main/resources/README.md).

## Corpus

Cuerpos de texto real en Esperanto, útiles para medir frecuencias de palabras y
para probar el tokenizador y el lematizador con entradas genuinas:

- **[Tekstaro de Esperanto](https://tekstaro.com)** — un corpus consultable de
  textos en Esperanto (literatura, publicaciones periódicas, el *Fundamento*), la
  fuente estándar de datos de frecuencia.
- **[Wikipedia en Esperanto](https://eo.wikipedia.org)** — un cuerpo grande y de
  descarga libre de texto contemporáneo sobre muchos temas.
- **[Project Gutenberg — Esperanto](https://www.gutenberg.org/browse/languages/eo)**
  — libros de dominio público en Esperanto, incluida la gramática que se distribuye
  en este repositorio.

!!! warning "Comprueba la licencia antes de redistribuir texto"
    Un corpus se puede *analizar* sin problema, pero redistribuir su texto (por
    ejemplo, confirmándolo en el repositorio) solo es seguro cuando su licencia lo
    permite. Las fuentes de dominio público como Project Gutenberg y el
    *Fundamento* son la opción segura por defecto; el texto de Wikipedia es
    CC BY-SA y debe conservar su atribución.

## Comunidades

Donde la lengua se usa de verdad, si quieres verla en su hábitat:

- **[Universala Esperanto-Asocio (UEA)](https://uea.org)** — la principal
  organización internacional, con enlaces a asociaciones nacionales y eventos.
- **[Esperanto en Reddit](https://www.reddit.com/r/Esperanto/)** — una comunidad
  activa y amigable para principiantes, en inglés.
- **Pasporta Servo, clubes locales y el anual _Universala Kongreso_** — la
  comunidad presencial, para quienes quieran oírla hablada.

## Adónde ir después

- [Historia](history.md) — cómo surgieron la lengua y su comunidad.
- [Gramática](grammar.md) — las reglas que estos recursos describen, destiladas
  para la biblioteca.
