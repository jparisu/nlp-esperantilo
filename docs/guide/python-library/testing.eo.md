# Testado

La testoj estas kodo, kiu kontrolas vian kodon. Ili estas tio, kio permesas al vi
ŝanĝi bibliotekon kun memfido: se ŝanĝo rompas ion, testo kaptas ĝin tuj anstataŭ ke
uzanto ekscias poste. Ĉi tiu paĝo klarigas kial ili gravas, kiel estas organizita la
dosierujo `tests/`, kiel verki kaj ruli ilin per **pytest**, kaj kiel ili fariĝas
aŭtomata pordo ĉe ĉiu kunfanda peto.

## Kial unutestoj

**Unutesto** ekzercas unu malgrandan pecon de la biblioteko izolite kaj asertas ke ĝi
kondutas kiel atendite. Ilia vera valoro aperas kun la tempo:

- **Ili kaptas regresojn.** Kiam vi ŝanĝas la tokenizilon, la testoj diras al vi tuj
  ĉu vi rompis la lematizilon, kiu dependas de ĝi.
- **Ili igas la refaktorigon sekura.** Vi povas reskribi la internaĵojn de la
  [API](api.md) libere, ĉar sukcesa testaro pruvas, ke la publika konduto ne ŝanĝiĝis.
- **Ili dokumentas la konduton.** Testo estas rulebla ekzemplo de kiel funkcio estas
  destinita esti vokata kaj kion ĝi devus redoni.
- **Ili ebligas la kunlaboron.** En teamo, la testoj estas kiel vi fidas la kunfandan
  peton de kunlaboranto sen relegi ĝin tute — la kontroloj estas verdaj.

La kosto estas malgranda kaj pagata unufoje; la profito kumuliĝas ĉiufoje kiam la kodo
ŝanĝiĝas.

## La strukturo `tests/`

La testoj vivas en supranivela dosierujo `tests/`, tenata ekster la distribuata pako
(vidu [Organizado](organization.md)). La testaro **spegulas la fontkodon**: ĉiu parto
de la biblioteko havas respondan dosieron `test_*.py`, do estas evidente kie vivas
testo kaj kie unu mankas.

```text
tests/
├── test_package.py     # la pako importiĝas kaj eksponas sian publikan API-on
├── test_resources.py   # la datumdosieroj estas validaj
└── test_tokenizer.py   # la fraz-dividado kondutas kiel dokumentite
```

Notu la parigon: `test_tokenizer.py` akompanas
`src/esperantilo/nlp/tokenizer.py`, kies konduto estas priskribita en
[Biblioteko → Fraz-dividado](../../library/sentence-segmentation.md). Unu
fontmodulo, unu testmodulo: en tio konsistas la tuta konvencio.

Du nomkonvencioj lasas ke pytest **malkovru** la testojn aŭtomate, sen registrado:

- la test-*dosieroj* nomiĝas `test_*.py`,
- la test-*funkcioj* nomiĝas `test_*`.

La fumtesto de ĉi tiu projekto montras la formon — importu la aferon, poste asertu ion
pri ĝi:

```python
# tests/test_package.py
import esperantilo


def test_package_is_importable():
    assert esperantilo is not None


def test_version_is_exposed():
    assert isinstance(esperantilo.__version__, str)
    assert esperantilo.__version__
```

Ĉiu funkcio testas unu fakton, kaj ĝia nomo diras kiu estas tiu fakto — do raporto pri
malsukceso legiĝas kiel frazo: `test_version_is_exposed failed`.

## Verki kaj ruli testojn per `pytest`

[pytest](https://docs.pytest.org/) estas la fakta norma testrulilo por Python.
Instalu ĝin per la testa kromaĵo kaj rulu la tutan testaron per unu vorto:

```bash
pip install -e ".[test]"
pytest
```

!!! tip "`pytest` funkcias sen instali ion ajn"
    La pako vivas sub `src/`, kiun Python ne serĉas defaŭlte, do nura `pytest`
    en freŝa klono malsukcesus kun `No module named 'esperantilo'`.
    `pythonpath = ["src"]` en `pyproject.toml` metas ĝin sur la vojon dum la
    testado, do `pytest` funkcias tuj post `git clone`.

```console
$ pytest
===================== test session starts =====================
configfile: pyproject.toml
testpaths: tests, src
collected 300 items

tests/test_package.py ........                            [  2%]
tests/test_resources.py ...........................       [ 18%]
tests/test_tokenizer.py .............xxx                  [ 97%]
src/esperantilo/nlp/tokenizer.py .                        [ 97%]
src/esperantilo/wiki/_wiki_api.py ..                      [ 98%]
src/esperantilo/wiki/wiki.py .....                        [100%]

=============== 297 passed, 3 xfailed in 0.13s ================
```

La ĉiutagaj funkcioj, kiujn vi uzos:

- **Asertoj.** Simplaj `assert`-frazoj — pytest reskribas ilin por montri la realajn
  valorojn ĉe malsukceso, do vi malofte bezonas ion alian.
- **Parametrigo.** Rulu la saman teston super multaj enigoj per
  `@pytest.mark.parametrize`, anstataŭ kopii-kaj-alglui. Ĉi tiu projekto uzas ĝin por
  ruli la samajn kontrolojn super *ĉiu* dosiero en `resources/`:

    ```python
    @pytest.mark.parametrize("path", FILES, ids=lambda p: p.name)
    def test_mandatory_fields(path):
        data = json.loads(path.read_text(encoding="utf-8"))
        for field in ("id", "titolo", "vortoj"):
            assert field in data, f"missing '{field}'"
    ```

- **Fikstaĵoj (fixtures).** Reuzebla preparo kunhavigita inter testoj (ekzempla
  dokumento, provizora dosiero), deklarita unufoje kaj petata per nomo.
- **Ruli subaron** dum vi fokusiĝas sur unu areo:

    ```bash
    pytest tests/test_package.py           # unu dosiero
    pytest -k version                      # testoj, kies nomo enhavas "version"
    pytest -x                              # haltu ĉe la unua malsukceso
    ```

!!! tip "Testu la konduton, ne la efektivigon"
    Asertu pri tio, kion funkcio *redonas aŭ faras*, ne pri kiel ĝi faras ĝin. Tiel
    viaj testoj plu sukcesas tra internaj refaktorigoj kaj malsukcesas nur kiam la
    konduto vere ŝanĝiĝas — kio estas la tuta celo.

## Dokumentteestoj: dokumentado, kiu ruliĝas {#doctests}

`Examples:`-bloko verkita kiel interaga seanco estas samtempe dokumentado kaj
testo. `--doctest-modules` igas pytest ruli tiujn ekzemplojn kaj kompari la
realan eligon kun la skribita; ĉi tiu projekto ŝaltas ĝin por `src/` en
`pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests", "src"]
addopts = "-ra --doctest-modules"
```

Tiuj ekzemploj estas tiuj publikigitaj sur la paĝo
[API-referenco](../../library/api.md), do ruli ilin estas tio, kio malhelpas la
dokumentaron silente malaktualiĝi. Tenu ilin mallongaj kaj ilustraj — randkazoj
apartenas al `tests/`.

## Testoj en kontinua integrado

Ruli la testojn loke estas bone; ruli ilin **aŭtomate ĉe ĉiu ŝanĝo** estas tio, kio
igas ilin vera sekureca reto. La [`tests.yml`-laborfluo](../github/actions.md#ruli-la-python-testojn)
rulas `pytest` ĉe ĉiu push kaj kunfanda peto al `main`, do rompita ŝanĝo estas
signalita en GitHub antaŭ ol iu kunfandas ĝin.

La lasta paŝo estas igi tiun kontrolon **deviga**: kun la
[branĉoprotekto](../github/repository-configuration.md#devigaj-statuskontroloj),
kunfanda peto ne povas kunfandiĝi dum ĝiaj testoj estas ruĝaj. La loka `pytest`, la CI
kaj la branĉoprotekto tiam formas ĉenon — vi kaptas problemojn frue, la CI kaptas kion
vi preterlasis, kaj la reguloj certigas ke nenio rompita atingas `main`.

## Kien iri poste

- [GitHub Actions](../github/actions.md) — la laborfluo, kiu rulas ĉi tiujn testojn.
- [Esperanto](../esperanto/index.md) — la lingvajn regulojn, kiujn enkodigos la
  biblioteko, kaj ĝiaj testoj.
- [Biblioteko → Fraz-dividado](../../library/sentence-segmentation.md) — la
  konduto, kiun fiksas
  [`tests/test_tokenizer.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_tokenizer.py),
  kaj prilaborita ekzemplo de la konvencioj de ĉi tiu paĝo.
