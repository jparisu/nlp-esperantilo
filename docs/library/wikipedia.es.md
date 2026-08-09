# Leer Wikipedia

Una biblioteca de NLP no sirve de nada sin texto sobre el que trabajar.
`esperantilo` obtiene ese texto de Wikipedia con
[`WikiPage`](api.md#esperantilo.wiki.WikiPage), ya limpio de marcado wiki.

```python
from esperantilo import WikiPage

page = WikiPage.look_up("Esperanto", language="eo")

page.title          # 'Esperanto'
page.qid            # 'Q143'
len(page)           # número de secciones
```

## Títulos, conceptos e idiomas

Un artículo existe una vez por idioma, y el mismo *concepto* es una página
distinta en cada uno: `Parsley`, `Perejil` y `Petroselo` son tres artículos
sobre una misma planta. Lo que los une es el **QID**, el identificador que
Wikidata da al concepto en sí: el perejil es `Q26980`, en todos los idiomas.

`look_up` se apoya en eso. Resuelve el título a un concepto y luego lee el
artículo correspondiente, así que el idioma en el que *buscas* y el idioma en el
que *lees* no tienen por qué coincidir:

```python
WikiPage.look_up("Perejil", language="eo").title
# 'Petroselo'
```

El título se busca primero en `language` y después en cada uno de
`fallback_languages`, siguiendo las redirecciones. El artículo llega en
`language` si esa wiki lo tiene, o en el primer idioma de reserva que lo tenga
—así que comprueba `page.language`, que puede no ser el código que pediste.

Si ningún idioma de la lista conoce el título, `any_language=True` (el valor por
defecto) recurre a buscar en Wikidata en todos los idiomas. Ese paso es una
*búsqueda*, no una consulta: encuentra algo para casi cualquier palabra
plausible, y lo que encuentra no es necesariamente lo que querías. Usa
`any_language=False` para obtener un `ValueError` en lugar de una conjetura.

## Secciones

El cuerpo es un diccionario de encabezado a texto, en el orden en que aparecen
en el artículo. Solo los encabezados de primer nivel abren una sección; los más
profundos quedan dentro del texto de la sección que los contiene. Wikipedia deja
la entradilla sin título, así que se guarda bajo el título del artículo.

```python
page.section_names          # ['Esperanto', 'Historio', 'Gramatiko', …]
page.section("historio")    # se compara ignorando mayúsculas
page["Historio"]            # lo mismo
"Historio" in page          # True
page.full_text()            # todas las secciones, con sus encabezados
```

## Qué puede fallar

| Situación | Qué ocurre |
| --- | --- |
| Ningún idioma de la lista conoce el título | `ValueError` |
| El concepto no tiene artículo en ninguno de ellos | `ValueError` |
| No hay ninguna sección con ese nombre | `KeyError` |
| Sin conexión, tiempo agotado, error de la API | `requests.RequestException` |

`ValueError` significa «la página no está ahí». Todo lo que tenga que ver con la
red aparece como una excepción de `requests`, de modo que se pueden capturar por
separado.

Cada consulta cuesta entre una y ocho peticiones HTTP, según cuántos idiomas
haya que probar. No hay caché: llamar dos veces a `look_up` con los mismos
argumentos lo descarga todo dos veces.

## Licencia

El texto de Wikipedia es **CC BY-SA**. Si republicas lo que obtengas, conserva
la atribución y la licencia; `page.url` es el enlace que hay que citar.

## Idiomas

Esta es una lista de algunos de los idiomas más utilizados, y sus códigos de Wikipedia:

| Idioma | Código |
| --- | --- |
| Esperanto | `eo` |
| Inglés | `en` |
| Español | `es` |
| Francés | `fr` |
| Alemán | `de` |
| ... | ... |

La lista completa de códigos está en [Wikipedia:Lista de códigos de idioma](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).


## Véase también

- [Referencia de la API](api.md#esperantilo.wiki.WikiPage) — la firma generada,
  los argumentos y los ejemplos.
- [`resources/notebooks/wikipedia.ipynb`](https://github.com/jparisu/nlp-esperantilo/blob/main/resources/notebooks/wikipedia.ipynb)
  — un notebook listo para ejecutar en Google Colab.
- [Segmentación en frases](sentence-segmentation.md) — el paso siguiente obvio
  para el texto que acabas de obtener.
