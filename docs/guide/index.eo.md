# Gvidilo

Ĉi tiu gvidilo helpos vin konstrui kaj eldoni Python-bibliotekon kiel tiun de ĉi tiu deponejo.
Ĝi gvidos vin tra la bazoj de la versikontrolo, la kunlabora fluo, la pakado kaj
testado, kaj la lingva scio, kiu iras internen.

!!! info "Gvidilo, ne referenco"
    Ĉi tiuj paĝoj instruas la *kiel*. La sekcio
    [Biblioteko](../library/index.md) estas la alia duono de ĉi tiu paĝaro: la
    referenca manlibro de `esperantilo` mem — ĝia API kaj ĝia funkciaro.

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
