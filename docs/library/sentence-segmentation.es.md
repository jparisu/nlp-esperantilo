# Segmentación en frases

Dividir un texto en frases es el primer paso de casi cualquier pipeline de PLN.
`esperantilo` lo hace con
[`sentence_tokenizer`](api.md#esperantilo.nlp.sentence_tokenizer).

```python
from esperantilo import sentence_tokenizer

sentence_tokenizer("Mi lernas Esperanton. Ĉu vere? Jes!")
# ['Mi lernas Esperanton.', 'Ĉu vere?', 'Jes!']
```

## La regla

Una frase termina en `.`, `!` o `?`. El carácter se queda con la frase que
cierra, y los espacios que la rodean se eliminan. Las frases vacías se
descartan, así que un texto de solo espacios devuelve `[]`.

Qué caracteres terminan una frase es un argumento:

```python
sentence_tokenizer("Unua. Dua! Tria?", end_of_sentence=["!"])
# ['Unua. Dua!', 'Tria?']
```

## Lo que no hace

El tokenizador es deliberadamente ingenuo: cada terminador corta, sea cual sea
su contexto:

| Entrada | Resultado |
| --- | --- |
| `"Pi estas 3.14."` | `['Pi estas 3.', '14.']` |
| `"Vidu esperanto.net."` | `['Vidu esperanto.', 'net.']` |
| `"Dr. Zamenhof venis."` | `['Dr.', 'Zamenhof venis.']` |

Son el `ToDo` anotado en el docstring de la función, y están
[fijados con pruebas `xfail`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py)
que se convierten en fallos el día en que se arreglen. Hacerlo es exactamente el
tipo de ejercicio para el que prepara la [Guía](../guide/index.md).

## Véase también

- [Referencia de la API](api.md) — la firma generada, los argumentos y los
  ejemplos.
- [Guía → Pruebas](../guide/python-library/testing.md) — cómo `pytest` fija la
  regla de arriba.
