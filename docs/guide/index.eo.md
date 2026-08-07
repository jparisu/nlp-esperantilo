# Gvidilo

Gvidilo por konstrui kaj eldoni Python-bibliotekon kiel ĉi tiu: la
versikontrolo, la kunlabora fluo, la pakado kaj testado, kaj la lingva scio, kiu
iras internen.

!!! info "Gvidilo, ne referenco"
    Ĉi tiuj paĝoj instruas la *kiel*. La sekcio
    [Biblioteko](../library/index.md) estas la alia duono de ĉi tiu paĝaro: la
    referenca manlibro de `esperantilo` mem — kion ĝi faras hodiaŭ kaj kion
    signifas ĉiu publika nomo. La gvidilo ligas al ĝi ĉiam, kiam reala ekzemplo
    klarigas ion pli bone ol prozo.

## Por kiu ĝi estas

Universitataj studentoj, kiuj devas konstrui sian propran Esperantan
NLP-bibliotekon. Oni atendas teknikan fonon, sed ne nepre sperton pri ĉi tiuj
specifaj iloj.

## La kvar sekcioj

<div class="grid cards" markdown>

- [**1. Git**](git/index.md) — versikontrolo: kiel ĝi funkcias, la bezonataj
  komandoj kaj kiel malfari ŝanĝojn.
- [**2. GitHub**](github/index.md) — la kunlabora fluo: kunfandaj petoj,
  Actions, protekto de la deponejo, Pages.
- [**3. Python-Biblioteko**](python-library/index.md) — pakado, strukturo,
  dezajno de la API, instalado kaj testado.
- [**4. Esperanto**](esperanto/index.md) — historio, gramatiko, vortprovizo kaj
  vortlistoj: la reguloj, kiujn la biblioteko enkodigas.

</div>

La sekcioj estas plejparte sendependaj. Legu ilin laŭorde, se vi komencas de
nulo; saltu rekte al [Python-Biblioteko](python-library/index.md) aŭ
[Esperanto](esperanto/index.md), se vi jam konas Git kaj GitHub-on.

## Kion ĝi *ne* kovras {#kion-gi-ne-kovras}

Du temoj estas intence lasitaj ekster ĉi tiu gvidilo, ĉar ili estas instruataj
en la kurslecionoj:

- **Retĉerpado kaj konsumo de API-oj** (`requests`, `beautifulsoup4`, la
  Vikipedia API kaj similaj).
- **Teksto-minado kaj klasifiko per maŝinlernado** (eltiro de trajtoj,
  vektorigo, trejnado kaj taksado de modeloj, metrikoj).

La fokuso ĉi tie estas la *ilaro de programa inĝenierado* necesa por labori kiel
profesia teamo, kaj la *faka scio pri Esperanto* necesa por verki regul-bazitan
NLP-bibliotekon.

La biblioteko ja *uzas* la unuan el tiuj du temoj — `esperantilo.wiki` vokas la
API-ojn de Vikipedio kaj Vikidatumoj per `requests` — sed kiel eldonitan kodon
por legi, ne kiel lecionon: vidu
[Biblioteko → Legi Vikipedion](../library/wikipedia.md).

## Ĉi tiu deponejo estas la ekzemplo

Kiam ajn la gvidilo montras dosieron, laborfluon aŭ enmetaĵon (*commit*), ĝi
estas reala, el ĉi tiu deponejo — ne elpensita fragmento. La sekcio
[Biblioteko](../library/index.md) dokumentas la rezulton.

| La gvidilo klarigas | Vi povas vidi ĝin funkcii en |
| --- | --- |
| [`pyproject.toml` kaj la `src/`-strukturo](python-library/organization.md) | [`pyproject.toml`](https://github.com/jparisu/nlp-esperantilo/blob/main/pyproject.toml) |
| [Dezajni publikan API-on](python-library/api.md) | [Biblioteko → API-referenco](../library/api.md) |
| [Verki testojn](python-library/testing.md) | [`tests/test_tokenizer.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py) |
| [GitHub Actions](github/actions.md) | [`.github/workflows/`](https://github.com/jparisu/nlp-esperantilo/tree/main/.github/workflows) |
| [GitHub Pages](github/pages.md) | ĉi tiu paĝaro |
