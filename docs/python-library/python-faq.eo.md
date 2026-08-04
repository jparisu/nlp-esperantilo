# Oftaj demandoj

Kutimaj demandoj pri konstruado, instalado kaj testado de la Python-biblioteko. Ĉiu
respondo ligas al la paĝo, kie la temo estas traktata pli detale.

??? question "Kio estas la diferenco inter modulo, pako kaj biblioteko?"
    **Modulo** estas unuopa dosiero `.py`; **pako** estas dosierujo de moduloj kun
    `__init__.py`; **biblioteko** estas pako celita por esti reuzata de alia kodo.
    **Distribuaĵo** estas la instalebla pakaĵo, kiun `pip` alportas. Vidu
    [Kio estas biblioteko](library.md#modulo-pako-biblioteko-distribuajo).

??? question "Ĉu mi bezonas `setup.py`? Kio estas `pyproject.toml`?"
    Ne — `pyproject.toml` estas la moderna, normigita anstataŭaĵo de `setup.py`. Ĝi
    enhavas la metadatenojn de la projekto, la dependecojn kaj la konstruan agordon en
    unu sola dosiero. Vidu [Organizado § pyproject.toml](organization.md#pyprojecttoml).

??? question "Kial la kodo estas sub `src/` anstataŭ ĉe la radiko de la deponejo?"
    Por ke la pako ne estu importebla *hazarde* de la radiko de la projekto. La
    `src/`-strukturo devigas vin instali la pakon antaŭ ol importi ĝin, do viaj testoj
    ruliĝas kontraŭ la instalita biblioteko ekzakte kiel ricevus ĝin uzanto. Vidu
    [Organizado § src](organization.md#the-src-layout).

??? question "Kio estas la diferenco inter `requirements.txt` kaj `pyproject.toml`?"
    `pyproject.toml` deklaras kion la *biblioteko* bezonas kiel parton de sia identeco
    — la fonto de vero kiam iu instalas ĝin. `requirements.txt` estas oportuna listo
    por fiksi reprodukteblan *medion*. Ĉi tiu biblioteko estas regul-bazita, do ĝi ne
    havas rultempajn dependecojn kaj `requirements.txt` estas esence malplena. Vidu
    [Organizado § requirements.txt](organization.md#requirementstxt).

??? question "Kion faras `__init__.py`?"
    Ĝi markas dosierujon kiel **pakon** kaj difinas kion la pako eksponas ĉe la
    importo. Ĉi tie ĝi deklaras la version kaj, dum la biblioteko kreskas, estas kie
    reeksportiĝas la publikaj klasoj. Vidu
    [Organizado § __init__.py](organization.md#__init__py).

??? question "Kiel mi instalas la bibliotekon en notlibro de Google Colab?"
    Instalu ĝin rekte de GitHub en ĉelo, poste importu ĝin:

    ```python
    !pip install git+https://github.com/jparisu/nlp-esperantilo.git
    import esperantilo
    ```

    Vidu [Instalado kaj uzo](installation-and-usage.md#uzi-gin-en-notlibro).

??? question "Kion signifas `pip install -e \".[test]\"`?"
    `-e` instalas la pakon en **redaktebla** reĝimo (ligilo al via fontkodo, do la
    redaktoj efikas tuj), kaj `.[test]` ankaŭ instalas la kromaĵon `test` (`pytest`).
    Ĝi estas la norma aranĝo por *disvolvi* la bibliotekon. Vidu
    [Instalado kaj uzo § Instali loke](installation-and-usage.md#instali-loke).

??? question "Mi instalis novan version en notlibro sed nenio ŝanĝiĝis. Kial?"
    Python kaŝmemorigas la importitajn modulojn dum la sesio. Post instalado de nova
    versio, **restartigu la rultempon** (Runtime → Restart), por ke la nova kodo estu
    ŝargita. Vidu [Instalado kaj uzo](installation-and-usage.md#uzi-gin-en-notlibro).

??? question "Por kio estas `__all__`?"
    Ĝi nomas la **publikajn** objektojn de modulo: ĝi dokumentas la celitan API-on kaj
    regas kion alportas `from esperantilo import *`. La nomoj ekster ĝi (kaj tiuj
    komenciĝantaj per `_`) estas traktataj kiel privataj. Vidu
    [API § Kio estas API ĉi tie](api.md#kio-estas-api-ci-tie).

??? question "Kial modeli la API-on laŭ spaCy?"
    Ĉar la tipita dezajno `Doc` / `Token` de spaCy estas pruvita, agrabla maniero
    reprezenti analizitan tekston, kaj la regula gramatiko de Esperanto igas tiujn
    atributojn kalkuleblaj per reguloj. Ĝi donas konkretan celon por imiti. Vidu
    [API § API laŭ la stilo de spaCy](api.md#api-lau-la-stilo-de-spacy).

??? question "Kiel mi rulas la testojn?"
    Instalu la testan kromaĵon kaj rulu pytest:

    ```bash
    pip install -e ".[test]"
    pytest
    ```

    pytest aŭtomate malkovras la dosierojn nomatajn `test_*.py` kaj la funkciojn
    nomatajn `test_*`. Vidu
    [Testado](testing.md#verki-kaj-ruli-testojn-per-pytest).

??? question "Ĉu la testoj ruliĝas aŭtomate?"
    Jes. La `tests.yml`-laborfluo de GitHub Actions rulas `pytest` ĉe ĉiu push kaj
    kunfanda peto, kaj la branĉoprotekto povas igi la sukceson de la testoj **deviga**
    antaŭ kunfando. Vidu
    [Testado § Testoj en kontinua integrado](testing.md#testoj-en-kontinua-integrado).
