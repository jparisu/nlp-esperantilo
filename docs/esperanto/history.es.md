# Historia

El Esperanto es una **lengua auxiliar internacional construida**: una lengua
diseñada a propósito, en lugar de una que evolucionó de forma natural. Entender
*por qué* se construyó como se construyó explica su propiedad más importante para
este proyecto —su **regularidad**—, que es lo que hace viable, para empezar, una
biblioteca de PLN basada en reglas.

## Zamenhof y el *Unua Libro*

El Esperanto fue creado por **L. L. Zamenhof** (1859–1917), un oftalmólogo de
**Białystok**, una ciudad entonces en el Imperio ruso y hoy en Polonia. Białystok
albergaba varias comunidades —polacos, rusos, alemanes, judíos— que hablaban
lenguas distintas y a menudo desconfiaban unas de otras. Zamenhof llegó a creer que
una segunda lengua común y neutral podría reducir esa fricción.

Publicó su proyecto en **1887**, en un folleto cuyo título en ruso se traduce como
*"Lengua Internacional"*. Lo firmó con el seudónimo **Doktoro Esperanto** —"Doctor
El-que-espera"— y el apodo se convirtió en el nombre de la lengua. Ese primer
folleto se conoce como el **_Unua Libro_** ("Primer Libro"). Contenía toda la
lengua en un espacio minúsculo: un prefacio, dieciséis reglas gramaticales y un
pequeño diccionario de raíces.

!!! quote "La idea tras las dieciséis reglas"
    Toda la gramática cabía en unas pocas páginas precisamente porque **no tiene
    excepciones**. Todo sustantivo termina en `-o`, todo verbo en presente en
    `-as`, y esas reglas nunca se rompen. Eso es inusual para una lengua natural —y
    es exactamente la propiedad de la que depende un analizador basado en reglas.

## Motivación

El objetivo de Zamenhof era una lengua **fácil de aprender** y **neutral** —que no
perteneciera a ninguna nación—. Del objetivo se derivaron directamente tres
decisiones de diseño, y las tres nos importan:

- **Regularidad.** La gramática es completamente sistemática; no hay verbos
  irregulares, ni plurales irregulares, ni excepciones de género que memorizar.
- **Simplicidad.** Un pequeño conjunto de reglas se combina para expresar mucho.
  Hay un solo artículo determinado, un solo marcador de plural, un solo marcador de
  acusativo.
- **Formación de palabras productiva.** Un número modesto de raíces más un conjunto
  de prefijos y sufijos generan un vocabulario amplio por composición regular
  (véase [Gramática § Afijos](grammar.md#afijos)).

Para un lingüista computacional, esto es casi ideal: una lengua cuya morfología
puede describirse con reglas que de verdad se cumplen, en lugar de con largas
listas de excepciones.

## Evolución

Para mantener la lengua estable a medida que se extendía, Zamenhof publicó el
**_Fundamento de Esperanto_** en **1905**, en el primer Congreso Universal de
Esperanto, en Francia. El *Fundamento* fue declarado el fundamento intocable de la
lengua: su gramática y su vocabulario básico podían ampliarse pero no cambiarse. Por
eso el Esperanto se ha mantenido notablemente consistente durante más de un siglo —
un texto de 1905 sigue siendo perfectamente legible hoy.

Desde entonces la lengua ha desarrollado una comunidad viva de hablantes por todo
el mundo, su propia literatura (original y traducida), publicaciones periódicas,
música y, más recientemente, una fuerte presencia en línea. Las estimaciones del
número de hablantes varían mucho, pero el Esperanto es, con gran diferencia, la
lengua construida de mayor éxito jamás creada, y la única con una comunidad de
hablantes nativos que crecieron con ella en casa.

Para saber dónde aprenderla y leerla de verdad, véase [Recursos](resources.md).

## Por qué importa aquí

La historia no es solo trasfondo: es la razón por la que este proyecto puede ser
*basado en reglas* en absoluto. Una lengua deliberadamente diseñada para la
regularidad puede tokenizarse, lematizarse y etiquetarse morfosintácticamente con
reglas escritas a mano hasta un grado que sería imposible para, digamos, el inglés.
La página siguiente convierte esa regularidad en las reglas concretas que codifica
la biblioteca.

## Adónde ir después

- [Gramática](grammar.md) — las reglas regulares que implementa la biblioteca.
