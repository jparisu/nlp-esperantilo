# Organizado

Biblioteko estas pli ol sia fontkodo: ĝi bezonas manplenon da dosieroj, kiuj diras al
Python (kaj al `pip`) kiel konstrui, instali kaj priskribi ĝin. Ĉi tiu paĝo trairas
la strukturon, kiun uzas ĉi tiu deponejo, kaj la celon de ĉiu dosiero, por ke vi povu
reprodukti ĝin en via propra projekto.

## Rekomendita strukturo

Ĉi tiu projekto uzas la **`src/`-strukturon**, la nuna plej bona praktiko por
Python-pakoj:

```text
nlp-esperantilo/
├── pyproject.toml        # metadatenoj de la projekto kaj konstrua agordo
├── requirements.txt      # rultempaj dependecoj (neniuj, nuntempe)
├── README.md             # ĉefpaĝo
├── LICENSE               # licenca teksto
├── mkdocs.yml            # agordo de la dokumentaro
├── docs/                 # la dokumentaro, kiun vi legas
├── resources/            # datumdosieroj (vortlistoj) distribuataj kun la projekto
├── src/
│   └── esperantilo/      # la pako mem
│       └── __init__.py
└── tests/
    ├── test_package.py   # fumtestoj de la pako
    └── test_resources.py # validigo de la datumdosieroj
```

La distinga trajto estas, ke la importebla pako vivas sub `src/`, ne ĉe la radiko de
la deponejo. La kialo estas subtila sed grava — vidu
[La `src/`-strukturo](#the-src-layout) sube.

## La dosieroj, kiuj gravas

### `pyproject.toml`

Ĉi tiu sola dosiero priskribas la tutan projekton: ĝiajn **metadatenojn** (nomo,
versio, priskribo), ĝiajn **dependecojn**, kaj kiel ĝi estas **konstruata**. Ĝi estas
la moderna, normigita anstataŭaĵo de la pli malnova `setup.py`. Jen la ŝlosilaj partoj
de la dosiero de ĉi tiu projekto:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "esperantilo"
version = "0.1.0"
description = "A rule-based Natural Language Processing library for Esperanto"
requires-python = ">=3.9"
dependencies = []                      # regul-bazita: neniuj rultempaj eksteraj dep.

[project.optional-dependencies]
test = ["pytest>=7.0"]                 # instalata per .[test]
docs = ["mkdocs>=1.6", "mkdocs-material>=9.5", "mkdocs-static-i18n>=1.2"]

[tool.setuptools.packages.find]
where = ["src"]                        # trovu la pakon sub src/

[tool.pytest.ini_options]
testpaths = ["tests"]
```

Tri partojn indas kompreni:

- **`[project]`** — la identeco de la biblioteko. `name` estas tio, kion oni
  `pip install`-as; `version` estas tio, kion oni fiksas; `dependencies` estas tio,
  kio instaliĝas *kun* ĝi (malplena ĉi tie, ĉar la biblioteko estas regul-bazita).
- **`[project.optional-dependencies]`** — *kromaĵoj*, instalataj laŭbezone. `.[test]`
  aldonas `pytest`, `.[docs]` aldonas la MkDocs-ilojn. La uzantoj de la biblioteko
  bezonas neniun; la programistoj jes.
- **`[tool.*]`** — agordo por aliaj iloj tenata en unu loko. Ĉi tie
  `[tool.setuptools.packages.find]` diras al la konstruo kie estas la pako, kaj
  `[tool.pytest.ini_options]` agordas la testrulilon.

### `requirements.txt`

Simpla listo de dependecoj, unu por linio, tradicie uzata kun
`pip install -r requirements.txt`. Ĝi interkovras kun `pyproject.toml`, do kion faras
ĉiu?

- **`pyproject.toml`** deklaras kion la *biblioteko* bezonas por funkcii, kiel parton
  de sia identeco. Ĝi estas la fonto de vero, kiam iu instalas `esperantilo`.
- **`requirements.txt`** estas oportuna listo, ofte uzata por fiksi precizajn versiojn
  por reproduktebla *medio*.

En ĉi tiu projekto la biblioteko havas **neniujn rultempajn dependecojn** (ĝi estas
regul-bazita), do
[`requirements.txt`](https://github.com/jparisu/nlp-esperantilo/blob/main/requirements.txt)
estas esence malplena — ĝi nur dokumentas kie vivas la disvolvaj kromaĵoj. La proprajn
dependecojn de la dokumentaro oni fiksas aparte en `docs/requirements.txt`, kiu estas
la dosiero, kiun uzas la [CI-laborfluoj](../github/actions.md).

### `__init__.py`

Dosiero `__init__.py` estas tio, kio igas dosierujon **pako**: sen ĝi, Python ne
traktas la dosierujon kiel importeblan. Ĝi ruliĝas kiam la pako unue importiĝas, kaj
ĝi difinas la **publikan surfacon** de la pako. Tiu de ĉi tiu projekto estas intence
minimuma:

```python
"""Esperantilo: a rule-based NLP library for Esperanto."""

__version__ = "0.1.0"

__all__ = ["__version__"]
```

Nuntempe ĝi eksponas nur la version. Dum la biblioteko kreskas, ĉi tie vi importus kaj
reeksportus la publikajn klasojn kaj funkciojn (la objektojn `Doc` kaj `Token`
dezajnitajn en [la API-paĝo](api.md)), por ke la uzantoj povu skribi
`from esperantilo import Doc` anstataŭ fosi en internaj moduloj. La listo `__all__`
ankaŭ estas klarigita tie.

### `src/` — kial la kodo ne estas ĉe la radiko {#the-src-layout}

Meti la pakon sub `src/` malhelpas klasikan kaj konfuzan cimon. Se la pako sidus ĉe la
radiko de la deponejo, tiam ruli Python *el* la radiko importus la lokan dosierujon
rekte — eĉ se la biblioteko neniam estis instalita. La testoj sukcesus kontraŭ la
kruda fontkodo dum la instalita kopio de reala uzanto kondutas alie.

Kun la `src/`-strukturo, la radiko *ne* estas importebla, do vi estas devigata
**instali la pakon** (`pip install -e .`) antaŭ ol importi ĝin. Viaj testoj tiam
ruliĝas kontraŭ la biblioteko ekzakte kiel ricevus ĝin uzanto. Ĝi estas unu kroma
paŝo, kiu forigas tutan kategorion da problemoj de la speco "sur mia maŝino ĝi
funkcias".

### `tests/` — spegulante la fontkodon

La dosierujo `tests/` enhavas la testaron, tenata aparte de la distribuata kodo, por
ke la testoj ne estu instalataj al finuzantoj. Ĝi spegulas tion, kion ĝi testas:
[`test_package.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_package.py)
kontrolas ke la pako importiĝas kaj eksponas sian version, kaj
[`test_resources.py`](https://github.com/jparisu/nlp-esperantilo/blob/main/tests/test_resources.py)
validigas la datumdosierojn sub `resources/`. La testado havas sian propran paĝon:
[Testado](testing.md).

## Versiado

La versio de la biblioteko vivas en **unu loko**, `version` en `pyproject.toml`, kaj
estas spegulata de `__version__` en `__init__.py`, por ke ĝi estu legebla rultempe:

```python
>>> import esperantilo
>>> esperantilo.__version__
'0.1.0'
```

La numeroj sekvas la **semantikan versiadon**, `MAJOR.MINOR.PATCH`:

- **PATCH** (`0.1.0 → 0.1.1`) — malantaŭen-kongruaj cimriparoj.
- **MINOR** (`0.1.0 → 0.2.0`) — novaj funkcioj, ankoraŭ malantaŭen-kongruaj.
- **MAJOR** (`0.1.0 → 1.0.0`) — ŝanĝoj, kiuj rompas la ekzistantan API-on.

Por eldoni novan version, altigu la numeron (en ambaŭ lokoj) kaj kunfandu ĝin per la
kutima [kunfandpeta laborfluo](../github/workflow.md).

## Kien iri poste

- [Instalado kaj uzo](installation-and-usage.md) — instalu ĉi tiun pakon kaj importu
  ĝin.
- [API](api.md) — dezajnu la publikan interfacon, kiun eksponos `__init__.py`.
