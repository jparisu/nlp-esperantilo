# Segmentación en frases

Dividir un texto en frases es el primer paso de casi cualquier pipeline de NLP.
`esperantilo` lo hace con
[`sentence_tokenizer`](api.md#esperantilo.nlp.sentence_tokenizer).

```python
from esperantilo import sentence_tokenizer

sentence_tokenizer("Mi lernas Esperanton. Ĉu vere? Jes!")
# ['Mi lernas Esperanton.', 'Ĉu vere?', 'Jes!']
```

## La regla actual

Este tokenizador utiliza los carácteres dados como argumentos de entrada para dividir el texto en frases.
Por defecto, son `.`, `!` y `?`.

Un ejemplo utilizando carácteres específicos sería:

```python
sentence_tokenizer("Unua. Dua! Tria?", end_of_sentence=("!",))
# ['Unua. Dua!', 'Tria?']
```

## Mejoras

Este tokenizador es una primera versión muy simplificada.
Ciertas mejoras que convendría implementar son:

1. Evitar cortar en abreviaturas como `Dr.` o `S-ro`.
2. Evitar cortar en números decimales como `3.14` y otros casos de puntuación como `...` o `?!`.
3. Evitar cortar en URLs, direcciones de correo electrónico y otros tokens que contienen `.` o `?`.
4. etc.

## Véase también

- [Referencia de la API](api.md) — la firma generada, los argumentos y los
  ejemplos.
- [Guía → Pruebas](../guide/python-library/testing.md) — cómo `pytest` fija la
  regla de arriba.
