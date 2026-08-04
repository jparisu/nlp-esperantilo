# Instalado kaj uzo

Kiam biblioteko estas pakita ([Organizado](organization.md)), uzi ĝin estas je unu
`pip install` for. Ĉar la plej granda parto de la laboro en ĉi tiu kurso okazas en
**notlibroj (Google Colab)**, la ĉefa vojo estas instali rekte de GitHub — sen loka
agordo, sen mana klonado.

## Instali de GitHub

`pip` povas instali pakon rekte de Git-deponejo. Ĝi estas la plej rapida maniero
enmeti `esperantilo`-n en notlibron dum la biblioteko ankoraŭ moviĝas:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

Ĉi tio klonas la deponejon malantaŭ la kulisoj, konstruas la pakon el ĝia
`pyproject.toml`, kaj instalas ĝin — ekzakte kvazaŭ ĝi venus de la Python Package
Index.

Vi povas fiksi specifan **branĉon**, etikedon aŭ commit-on aldonante `@<ref>`:

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git@main
pip install git+https://github.com/jparisu/nlp-esperantilo.git@jparisu/v0.1
```

!!! tip "Kial instali de GitHub?"
    Dum biblioteko estas en aktiva disvolvado kaj ankoraŭ ne publikigita al PyPI,
    instali de GitHub signifas, ke ĉiuj ĉiam ricevas la plej lastan kodon de elektita
    branĉo, per unu sola komando kaj sen manaj paŝoj. Ĝi taŭgas nature por laborfluo
    bazita sur notlibroj.

## Uzi ĝin en notlibro

En Colab-notlibro, instalu en ĉelo (la komenca `!` rulas ŝelan komandon), poste
importu kaj uzu la bibliotekon:

```python
!pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

```python
import esperantilo

print(esperantilo.__version__)   # 0.1.0
```

Dum la biblioteko kreskas, la sama importo donas al vi ĝiajn publikajn objektojn —
ekzemple la tipojn `Doc` kaj `Token` dezajnitajn en [la API-paĝo](api.md):

```python
# Ilustra: la cela API, ankoraŭ ne realigita.
import esperantilo

doc = esperantilo.parse("La rapida vulpo saltas.")
for token in doc:
    print(token.text, token.lemma, token.pos)
```

!!! note "Restartigu la rultempon post la instalado"
    Se vi jam importis `esperantilo`-n en notlibro kaj poste instalas novan version,
    restartigu la rultempon (**Runtime → Restart**), por ke la nova kodo estu prenata.
    Python kaŝmemorigas la importitajn modulojn dum la tuta sesio.

## Instali loke

Por disvolvi la bibliotekon mem —anstataŭ nur uzi ĝin— instalu ĝin **loke** en
virtuala medio. Virtuala medio estas izolita Python-instalaĵo por unu projekto, por ke
ĝiaj dependecoj ne konfliktu kun io alia sur via maŝino:

```bash
python -m venv .venv          # kreu la medion
source .venv/bin/activate     # aktivigu ĝin (Windows: .venv\Scripts\activate)
pip install -e ".[test]"      # redaktebla instalo, kun la testa kromaĵo
```

Du opcioj igas ĉi tion *disvolva* instalo:

- **`-e` (redaktebla).** La pako estas instalita kiel ligilo al via fontkodo, do viaj
  redaktoj efikas tuj — sen reinstalado post ĉiu ŝanĝo.
- **`.[test]`** instalas la pakon *plus* ĝian kromaĵon `test` (`pytest`), por ke vi
  povu ruli la testaron tuj (vidu [Testado](testing.md)). Uzu `.[docs]` por labori pri
  la dokumentaro anstataŭe.

Ĉi tio estas ekzakte tio, kion faras la [`tests.yml`-laborfluo](../github/actions.md#ruli-la-python-testojn)
en CI, do verda loka rulo signifas verdan rulon en GitHub.

## Kien iri poste

- [API](api.md) — kiel devus aspekti pura publika interfaco por la biblioteko.
- [Testado](testing.md) — ruli kaj verki la testaron.
