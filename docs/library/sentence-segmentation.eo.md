# Fraz-dividado

Dividi tekston en frazojn estas la unua paŝo de preskaŭ ĉiu NLP-ĉeno.
`esperantilo` faras tion per
[`sentence_tokenizer`](api.md#esperantilo.tokenizer.sentence_tokenizer).

```python
from esperantilo import sentence_tokenizer

sentence_tokenizer("Mi lernas Esperanton. Ĉu vere? Jes!")
# ['Mi lernas Esperanton.', 'Ĉu vere?', 'Jes!']
```

## La regulo

Frazo finiĝas ĉe `.`, `!` aŭ `?`. La signo restas ĉe la frazo, kiun ĝi fermas,
kaj la ĉirkaŭaj spacoj estas forigitaj. Malplenaj frazoj estas forĵetataj, do
teksto el nuraj spacoj donas `[]`.

Kiuj signoj finas frazon estas argumento:

```python
sentence_tokenizer("Unua. Dua! Tria?", end_of_sentence=["!"])
# ['Unua. Dua!', 'Tria?']
```

## Kion ĝi ne faras

La dividilo estas intence naiva — ĉiu finigilo tranĉas, kio ajn ĝin ĉirkaŭas:

| Enigo | Rezulto |
| --- | --- |
| `"Pi estas 3.14."` | `['Pi estas 3.', '14.']` |
| `"Vidu esperanto.net."` | `['Vidu esperanto.', 'net.']` |
| `"Dr. Zamenhof venis."` | `['Dr.', 'Zamenhof venis.']` |

Tiuj estas la `ToDo` notita en la dokumentĉeno de la funkcio, kaj ili estas
[fiksitaj per `xfail`-testoj](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py),
kiuj fariĝas malsukcesoj en la tago, kiam ili estos riparitaj. Fari tion estas
ĝuste la speco de ekzerco, por kiu la [Gvidilo](../guide/index.md) preparas vin.

## Vidu ankaŭ

- [API-referenco](api.md) — la generita signaturo, la argumentoj kaj la ekzemploj.
- [Gvidilo → Testado](../guide/python-library/testing.md) — kiel `pytest` fiksas
  la supran regulon.
