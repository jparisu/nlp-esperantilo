# NLP Esperantilo

Bonvenon al **NLP Esperantilo**, projekto konsistanta el du komplementaj partoj:

- **Python-biblioteko** por regul-bazita komputila lingvistiko (NLP) en Esperanto.
- **Ĉi tiu dokumentaro**, gvidilo kaj lernolibro por konstrui tiun bibliotekon kaj
  ĝiajn ilojn de nulo.

!!! warning "Laboro en progreso"
    Ĉi tiu paĝaro estas la skeleto de la dokumentaro. Ĉiu sekcio jam havas sian
    strukturon kaj sian planitan enhavon, sed la enhavo mem ankoraŭ estas verkata.
    La paĝoj sen Esperanta traduko montriĝas en la angla.

## Por kiu ĝi estas

Ĉi tiu gvidilo celas universitatajn studentojn, kiuj devas konstrui sian propran
Esperantan NLP-bibliotekon. Oni atendas, ke la leganto havas ian teknikan fonon,
sed ne nepre sperton pri la specifaj iloj kaj temoj ĉi tie klarigataj.

## Kion kovras ĉi tiu gvidilo

| Sekcio | Enhavo |
| --- | --- |
| [Git](git/index.md) | Versikontrolo: kiel Git funkcias, ĝiaj plej uzataj komandoj kaj kiel malfari ŝanĝojn. |
| [GitHub](github/index.md) | Kunlabora fluo, kunfandaj petoj (pull requests), GitHub Actions, protekto de la deponejo kaj GitHub Pages. |
| [Python-Biblioteko](python-library/index.md) | Pakado, strukturo de la projekto, dezajno de la API, instalado kaj testado. |
| [Esperanto](esperanto/index.md) | Historio, gramatiko, vortprovizo kaj lernorimedoj: la lingvaj reguloj, kiujn la biblioteko enkodigas. |

## Kion ĝi *ne* kovras

Du temoj estas intence lasitaj ekster ĉi tiu gvidilo, ĉar ili estas instruataj en
la kurslecionoj:

- **Retĉerpado kaj konsumo de API-oj** (`requests`, `beautifulsoup4`, la
  Vikipedia API kaj similaj).
- **Teksto-minado kaj klasifiko per maŝinlernado** (eltiro de trajtoj,
  vektorigo, trejnado kaj taksado de modeloj, metrikoj).

La fokuso ĉi tie estas la *ilaro de programa inĝenierado* necesa por labori kiel
profesia teamo, kaj la *faka scio pri Esperanto* necesa por verki regul-bazitan
NLP-bibliotekon.

## Kiel legi la dokumentaron

La gvidilon eblas legi de komenco ĝis fino, sed la kvar sekcioj estas plejparte
sendependaj. Kiu jam konas Git kaj GitHub-on, tiu povas salti rekte al
[Python-Biblioteko](python-library/index.md) aŭ [Esperanto](esperanto/index.md).

## Konstrui la dokumentaron loke

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

La paĝaro tiam disponeblas ĉe <http://127.0.0.1:8000>. Ĉiu push al `main`
rekonstruas ĝin kaj publikigas ĝin en GitHub Pages.
