# Komandoj

Ĉi tiu paĝo estas praktika trairo de la komandoj, kiujn vi uzos ĉiutage. Por ĉiu:
kion ĝi faras, la du aŭ tri opcioj kiujn vi vere uzos, kaj eta ekzemplo kun la
eligo kiun vi povas atendi.

Vi ne bezonas parkerigi ilin — tenu ĉi tiun paĝon kiel referencon kaj la muskola
memoro venos. La paĝo [Ekzemplo](example.md) poste kunligas ilin en kompletan
laborfluon.

!!! info "Konvencioj uzataj sube"
    La linioj komenciĝantaj per `$` estas komandoj kiujn vi tajpas; ĉio alia estas
    eligo. La vojoj kaj haketaĵoj venas el eta ekzempla projekto.

## Ekigi deponejon

### `git init`

Igas la nunan dosierujon Git-deponejo. Ĝi kreas kaŝitan dosierujon `.git/`, kiu
enhavas la tutan historion; viaj dosieroj restas netuŝitaj.

```console
$ git init
Initialized empty Git repository in /home/user/my-project/.git/
```

Ĉi tion oni faras **unufoje**, ĉe la komenco de projekto.

### `git clone`

Kopias ekzistantan deponejon — inkluzive de ĝia tuta historio — al via maŝino. Tiel
vi komencas labori pri projekto, kiu jam ekzistas (ekzemple, unu gastigata en
GitHub).

```console
$ git clone https://github.com/jparisu/nlp-esperantilo.git
Cloning into 'nlp-esperantilo'...
remote: Enumerating objects: 120, done.
Receiving objects: 100% (120/120), 45.2 KiB, done.
```

Klonado ankaŭ agordas remoton nomatan **`origin`**, kiu montras al la fonto, tiel
ke vi povas fari `push` kaj `pull` sen plia agordo.

## Registri ŝanĝojn

### `git status`

Montras la nunan staton: kiuj dosieroj ŝanĝiĝis, kiuj estas preparitaj por la sekva
commit, kaj kiuj ankoraŭ ne estas spurataj. Ĉi tiu estas la komando, kiun vi plej
ofte plenumas — kiam ajn vi dubas, plenumu `git status`.

```console
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        notes.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

### `git add`

Movas ŝanĝojn al la prepara zono, por ke ili estu parto de la sekva commit.

```console
$ git add README.md        # preparas unu dosieron
$ git add .                # preparas ĉion en la nuna dosierujo
```

La preparado estas tio, kio ebligas al vi fari commit-on de *kelkaj* el viaj ŝanĝoj
kaj lasi la reston: nur tio, kion vi `add`-as, eniras la commit-on.

### `git commit`

Registras ĉion nun preparitan kiel novan commit-on, kun mesaĝo.

```console
$ git commit -m "Add stop-word list"
[main 9f3a1c2] Add stop-word list
 1 file changed, 42 insertions(+)
```

- `-m "…"` donas la mesaĝon enlinie. Sen ĝi, Git malfermas redaktilon.
- Verku la mesaĝojn en **imperativo** kaj tenu ilin signifoplenaj — vidu
  [Organizado § Historio](organization.md#historio).

!!! warning "`git commit -a`"
    `git commit -a` preparas **ĉiujn spuratajn dosierojn** kaj faras la commit-on
    en unu paŝo. Ĝi estas oportuna mallongigo, sed ĝi preterlasas la revizion kiun
    donas la preparado, kaj ĝi neniam inkluzivas novajn (nespuratajn) dosierojn.
    Preferu eksplicitan `git add` dum vi lernas.

## Inspekti

### `git log`

Legas la historion, la plej nova commit unue.

```console
$ git log --oneline
772a47a Only test in python 3.11
a1976d8 Add PR documentation previews and the stop-word list
92c1041 Add project skeleton, documentation scaffold and CI
5f46a63 Add docs design
7b0978f Add README
```

- `--oneline` densigas ĉiun commit-on al unu linio — la plej utila ĉiutaga vido.
- `--graph --oneline --all` desegnas la branĉan strukturon kiel ASCII-arton.
- `-p` montras la plenan diff-on de ĉiu commit.

### `git diff`

Montras la ŝanĝojn kiel [diff-on](organization.md#diff-oj). Sen argumentoj ĝi montras
tion, kion vi ŝanĝis sed **ankoraŭ ne preparis**:

```console
$ git diff
diff --git a/README.md b/README.md
index 3b1f2a1..a2c4d9e 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,2 @@
 # NLP Esperantilo
+A rule-based NLP library for Esperanto.
```

- `git diff --staged` montras tion, kio estas preparita (t.e. tion, kion registros
  la sekva commit).
- `git diff main feature` komparas du branĉojn.

## Branĉigi kaj kunfandi

### `git branch`

Listigas, kreas aŭ forigas branĉojn.

```console
$ git branch                 # listigas; la nuna estas markita per *
* main
$ git branch feature         # kreas branĉon nomatan "feature"
$ git branch -d feature      # forigas jam kunfanditan branĉon
```

Krei branĉon ne ŝanĝas vin al ĝi — por tio, uzu `checkout`.

### `git checkout`

Ŝanĝas inter branĉoj (kaj, pli ĝenerale, movas `HEAD`).

```console
$ git checkout feature       # ŝanĝu al ekzistanta branĉo
Switched to branch 'feature'
$ git checkout -b feature    # kreu KAJ ŝanĝu en unu paŝo
Switched to a new branch 'feature'
```

!!! note "`git switch` kaj `git restore`"
    La moderna Git dividis la du taskojn de `checkout` en pli klarajn komandojn:
    `git switch` por ŝanĝi branĉon kaj `git restore` por forĵeti ŝanĝojn de
    dosieroj. `checkout` ankoraŭ funkcias kaj estas tio, kion vi plej ofte vidos,
    do ĉi tiu gvidilo uzas ĝin; `restore` estas traktata en
    [Malfari ŝanĝojn](undoing-changes.md).

### `git merge`

Integras alian branĉon en la nunan.

```console
$ git checkout main
$ git merge feature
Updating 92c1041..9f3a1c2
Fast-forward
 docs/git/commands.md | 120 +++++++++++++++++++++++++++
 1 file changed, 120 insertions(+)
```

Se ambaŭ branĉoj ŝanĝis la samajn liniojn, la kunfando haltas kun **konflikto** por
ke vi solvu ĝin — vidu la [Ekzemplon](example.md).

## Sinkronigi kun remoto

### `git push`

Sendas viajn lokajn commit-ojn al la remoto (ekz. GitHub).

```console
$ git push origin main
Enumerating objects: 5, done.
To https://github.com/jparisu/nlp-esperantilo.git
   92c1041..9f3a1c2  main -> main
```

La unuan fojon kiam vi puŝas novan branĉon, uzu `git push -u origin <branĉo>`; la
`-u` memoras la ligon, do poste sufiĉas tajpi `git push`.

### `git pull`

Alportas commit-ojn de la remoto al via nuna branĉo. Ĝi fakte estas du paŝoj en unu:
**fetch** de la novaj commit-oj, poste **merge** de ili en vian branĉon.

```console
$ git pull
Updating 9f3a1c2..b7d0e11
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Akiru la kutimon fari pull **antaŭ** ol vi komencas labori, por konstrui sur la plej
lastaj ŝanĝoj de viaj kunlaborantoj anstataŭ sur malaktuala kopio.

## Rapida referenco

| Komando | Por kio |
| --- | --- |
| `git init` | Krei deponejon en la nuna dosierujo. |
| `git clone <url>` | Kopii ekzistantan deponejon, kun ĝia tuta historio. |
| `git status` | Vidi kio ŝanĝiĝis kaj kio estas preparita. |
| `git add <vojo>` | Prepari ŝanĝojn por la sekva commit. |
| `git commit -m "…"` | Registri la preparitajn ŝanĝojn kun mesaĝo. |
| `git log --oneline` | Legi la historion. |
| `git diff` | Inspekti ankoraŭ nepreparitajn ŝanĝojn. |
| `git branch` | Listigi, krei aŭ forigi branĉojn. |
| `git checkout <branĉo>` | Ŝanĝi branĉon (`-b` por krei). |
| `git merge <branĉo>` | Integri branĉon en la nunan. |
| `git push` | Sendi commit-ojn al la remoto. |
| `git pull` | Alporti commit-ojn de la remoto al la nuna branĉo. |

## Aliaj utilaj komandoj

- `git rebase <branch>` — reorganizi commit-ojn por igi la historion pli lineara.
- `git fetch` — alporti commit-ojn de la remoto sen kunfandi ilin.
- `git cherry-pick <hash>` — apliki unu specifan commit-on el alia branĉo.

Aliaj komandoj por malfari ŝanĝojn estas traktataj en
[Malfari ŝanĝojn](undoing-changes.md): `git restore`, `git reset`, `git stash`.

## La dosiero `.gitignore`

Ne ĉiu dosiero apartenas al la deponejo. Kompilitaj artefaktoj, virtualaj medioj,
kaŝmemoroj kaj redaktilaj agordoj generiĝas loke kaj nur malordigus la historion
(kaj kaŭzus konfliktojn), se ilin oni konfirmus.

Dosiero **`.gitignore`**, metita ĉe la radiko de la deponejo, listigas ŝablonojn de
dosieroj, kiujn Git devas **ignori**: ili neniam aperas en `git status` kaj ne povas
esti aldonitaj hazarde. Ĉiu linio estas ŝablono; `#` komencas komenton.

Jen la `.gitignore`, kiun uzas ĉi tiu sama projekto — bona deirpunkto por ajna
Python-projekto:

```gitignore
# Byte-compiled / optimized files
__pycache__/
*.py[cod]

# Packaging and build artifacts
build/
dist/
*.egg-info/

# Virtual environments
.venv/
venv/
env/

# Testing and coverage
.pytest_cache/
.coverage

# Notebooks
.ipynb_checkpoints/

# MkDocs output
site/

# Editors and OS
.idea/
.vscode/
.DS_Store
```

!!! tip
    Aldonu la `.gitignore` **antaŭ** via unua commit, por ke la bruo neniam eniru la
    historion unuavice. Se dosiero jam estas spurata, aldoni ĝin al `.gitignore` ne
    forigas ĝin — vi devas fari `git rm --cached <dosiero>` unufoje.

!!! note "Etikedoj kaj eldonoj (tags kaj releases)"
    Etikedi specifajn commit-ojn kiel versiitajn eldonojn estas reala funkcio de
    Git, sed ĝi estas intence lasita ekster ĉi tiu gvidilo: por ĉi tiu projekto,
    kompreni `main` kaj branĉojn sufiĉas.

## Kien iri poste

- [Malfari ŝanĝojn](undoing-changes.md) — kiam komando misfunkciis, aŭ vi
  ŝanĝis vian opinion.
- [Ekzemplo](example.md) — ĉi tiuj komandoj, aplikitaj de komenco ĝis fino.
