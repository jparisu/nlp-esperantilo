# Malfari ŝanĝojn

Pli aŭ malpli frue vi volos **reiri**: forĵeti redakton, malprepari dosieron, aŭ
flankenmeti vian laboron por trakti ion urĝan. Git havas komandon por ĉiu kazo. Ĉi
tiu paĝo kovras la tri, kiujn vi vere bezonas — `restore`, `reset` kaj `stash` — kaj
gvidilon por elekti la ĝustan.

!!! warning "Kelkaj el ĉi tiuj forĵetas laboron"
    Forĵeti ŝanĝojn en la labordosierujo (`git restore <dosiero>`,
    `git reset --hard`) **definitive forigas** tiujn ŝanĝojn: ili neniam estis
    konfirmitaj, do Git ne povas revenigi ilin. Se vi dubas, preferu `git stash`,
    kiu flankenmetas la laboron sen detrui ĝin.

## `git restore` — forĵeti ŝanĝojn en la labordosierujo

Uzu `restore` por forĵeti redaktojn, kiujn vi **ne konfirmis**, kaj reiri al la
lasta konfirmita versio de dosiero.

```console
$ git status
Changes not staged for commit:
        modified:   README.md

$ git restore README.md
$ git status
On branch main
nothing to commit, working tree clean
```

`restore` ankaŭ **malpreparas** dosieron (elprenas ĝin el la prepara zono, sed
konservas viajn redaktojn) per la opcio `--staged`:

```console
$ git restore --staged README.md   # malpreparu, konservu la ŝanĝojn
```

- `git restore <dosiero>` → forĵeti nekonfirmitajn redaktojn de tiu dosiero.
- `git restore --staged <dosiero>` → malprepari, sed konservi la redaktojn.

## `git reset` — movi la montrilon de la branĉo

`reset` funkcias sur **commit-oj kaj preparado**, ne sur unuopaj redaktoj de
dosieroj. Ĝia plej ofta ĉiutaga uzo estas la mala direkto de `add`: malpreparado.

```console
$ git add README.md
$ git reset README.md      # malpreparas README.md (ekvivalentas al restore --staged)
```

Uzata kun commit, `reset` **movas la montrilon de la nuna branĉo** al pli frua
commit — forigante praktike de la branĉo la commit-ojn post ĝi. Kio okazas al la
ŝanĝoj en tiuj commit-oj dependas de la reĝimo:

| Reĝimo | Montrilo de branĉo | Prepara zono | Labordosierujo |
| --- | --- | --- | --- |
| `--soft` | retroiras | konserviĝas | konserviĝas |
| `--mixed` *(defaŭlta)* | retroiras | nuliĝas | konserviĝas |
| `--hard` | retroiras | nuliĝas | **forĵetiĝas** |

- `git reset --soft HEAD~1` — malfaras la **lastan commit-on** sed konservas ĝiajn
  ŝanĝojn preparitaj, pretaj por rekonfirmo (bonega por korekti mesaĝon de commit aŭ
  dividi commit-on).
- `git reset --mixed HEAD~1` — malfaras la lastan commit-on kaj malpreparas ĝiajn
  ŝanĝojn, sed konservas ilin en viaj dosieroj.
- `git reset --hard HEAD~1` — malfaras la lastan commit-on **kaj forĵetas ĝiajn
  ŝanĝojn**. Rapida, kaj neinversigebla.

Ĉi tie `HEAD~1` signifas "unu commit antaŭ la nuna".

!!! danger "`--hard` kaj kunhavigita historio"
    Neniam faru `reset` de commit-oj, kiujn vi jam **puŝis kaj kunhavigis** kun
    aliaj: vi reskribas historion, kiun ili jam havas, kaj ilia sekva `pull`
    konfliktos. Sur kunhavigitaj branĉoj, malfaru commit-on per `git revert` (kiu
    registras *novan* commit-on, kiu malfaras malnovan) anstataŭe.

## `git stash` — flankenmeti ŝanĝojn

Foje vi estas en la mezo de io, kiam vi bezonas puran labordosierujon tuj — por
fari pull, por ŝanĝi branĉon, aŭ por provi rapidan riparon. `stash` kaŝas viajn
nekonfirmitajn ŝanĝojn sekure kaj redonas al vi puran arbon.

```console
$ git stash
Saved working directory and index state WIP on main: 92c1041 Add project skeleton

$ git status
On branch main
nothing to commit, working tree clean
```

Viaj ŝanĝoj ne perdiĝas — ili estas sur stako. Revenigu ilin kiam vi estas preta:

```console
$ git stash pop      # reaplikas la plej lastan stash-on kaj forigas ĝin de la stako
```

- `git stash` → konservi la ŝanĝojn kaj purigi la labordosierujon.
- `git stash list` → vidi kion vi stash-is.
- `git stash pop` → reapliki la lastan stash-on kaj forigi ĝin.
- `git stash drop` → forĵeti stash-on sen apliki ĝin.

Male al `reset --hard`, `stash` estas **sekura**: nenio detruiĝas, do ĝi estas la
ĝusta unua reflekso kiam ajn vi nur bezonas parkumi vian laboron por momento.

## Kiun mi bezonas?

| Via situacio | Komando |
| --- | --- |
| Mi redaktis dosieron kaj volas forĵeti la redakton | `git restore <dosiero>` |
| Mi preparis dosieron erare | `git restore --staged <dosiero>` (aŭ `git reset <dosiero>`) |
| Mi volas refari mian lastan commit-on (mesaĝon, aŭ aldoni dosieron) | `git reset --soft HEAD~1` |
| Mi bezonas puran arbon *tuj* sed volas revenigi mian laboron poste | `git stash` → `git stash pop` |
| Mi volas malfari commit-on, kiun mi jam **puŝis** | `git revert <commit>` |

!!! tip "La ĝenerala regulo de sekureco antaŭ ĉio"
    Se la ŝanĝo estas **konfirmita**, vi preskaŭ ĉiam povas revenigi ĝin, do malfari
    estas sekure. Se ĝi estas **nekonfirmita**, Git ne havas kopion — do faru
    `stash` antaŭ ol fari ion detruan.

## Kien iri poste

- [Ekzemplo](example.md) — kompleta trairo, kiu kunigas commit-ojn, branĉojn kaj
  kunfandojn.
