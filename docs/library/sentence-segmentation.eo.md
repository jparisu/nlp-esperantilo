# Fraz-dividado

Dividi tekston en frazojn estas la unua paŝo de preskaŭ ĉiu NLP-ĉeno.
`esperantilo` faras tion per
[`sentence_tokenizer`](api.md#esperantilo.nlp.sentence_tokenizer).

```python
from esperantilo import sentence_tokenizer

sentence_tokenizer("Mi lernas Esperanton. Ĉu vere? Jes!")
# ['Mi lernas Esperanton.', 'Ĉu vere?', 'Jes!']
```

## La nuna regulo

Ĉi tiu dividilo uzas la signojn donitajn kiel eniga argumento por dividi la
tekston en frazojn.
Defaŭlte ili estas `.`, `!` kaj `?`.

Ekzemplo kun specifaj signoj estus:

```python
sentence_tokenizer("Unua. Dua! Tria?", end_of_sentence=("!",))
# ['Unua. Dua!', 'Tria?']
```

## Plibonigoj

Ĉi tiu dividilo estas tre simpligita unua versio.
Kelkaj plibonigoj indaj je efektivigo estas:

1. Ne tranĉi ĉe mallongigoj kiel `D-ro` aŭ `S-ro`.
2. Ne tranĉi ĉe dekumaj nombroj kiel `3.14`, nek ĉe aliaj interpunkciaj kazoj
   kiel `...` aŭ `?!`.
3. Ne tranĉi ĉe URL-oj, retpoŝtadresoj kaj aliaj vortoj enhavantaj `.` aŭ `?`.
4. ktp.

## Vidu ankaŭ

- [API-referenco](api.md) — la generita signaturo, la argumentoj kaj la ekzemploj.
- [Gvidilo → Testado](../guide/python-library/testing.md) — kiel `pytest` fiksas
  la supran regulon.
