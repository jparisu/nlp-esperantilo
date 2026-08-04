# Ekzemplo

Ĉi tiu paĝo kunigas la tutan sekcion **rekreante kiel ĉi tiu sama projekto,
`nlp-esperantilo`, estis ekigita** — de malplena dosierujo ĝis deponejo puŝita al
GitHub, kun branĉo kaj kunfanda konflikto survoje.

Vi povas sekvi en malplena dosierujo kaj reprodukti ĉiun paŝon. La komandoj estas la
linioj komenciĝantaj per `$`; ĉio alia estas eligo.

!!! info "Kion vi bezonas"
    Git instalita (`git --version` devus presi version) kaj, por la lasta paŝo,
    GitHub-konton. Agordu vian identecon unufoje, por ke viaj commit-oj estu
    atribuitaj al vi:

    ```console
    $ git config --global user.name "Via Nomo"
    $ git config --global user.email "vi@ekzemplo.com"
    ```

## 1. Krei la deponejon

Komencu en malplena dosierujo kaj igu ĝin Git-deponejo:

```console
$ mkdir nlp-esperantilo
$ cd nlp-esperantilo
$ git init
Initialized empty Git repository in /home/user/nlp-esperantilo/.git/
```

Antaŭ ol aldoni ion, kreu **`.gitignore`**, por ke generitaj dosieroj neniam eniru
la historion (vidu [Komandoj § .gitignore](commands.md#la-dosiero-gitignore)):

```console
$ printf '__pycache__/\n.venv/\nsite/\n' > .gitignore
```

## 2. Aldoni dosierojn kaj fari la unuan commit-on

Kreu unuan dosieron — la README de la projekto:

```console
$ printf '# NLP Esperantilo\n' > README.md
```

Kontrolu la staton. Git vidas du novajn dosierojn, kiujn ĝi ankoraŭ ne spuras:

```console
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md

nothing added to commit but untracked files present
```

Preparu ambaŭ dosierojn kaj registru la unuan commit-on:

```console
$ git add .
$ git commit -m "Initial commit"
[main (root-commit) 29434cf] Initial commit
 2 files changed, 4 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
```

Aldonu iom pli al la README kaj faru duan commit-on, por havi iom da historio:

```console
$ printf '\nA rule-based NLP library for Esperanto.\n' >> README.md
$ git add README.md
$ git commit -m "Add README"
[main 7b0978f] Add README
 1 file changed, 2 insertions(+)
```

## 3. Inspekti la staton

Tri komandoj respondas al "kie mi estas?":

```console
$ git log --oneline
7b0978f Add README
29434cf Initial commit

$ git status
On branch main
nothing to commit, working tree clean

$ git diff
```

`git log` montras la du commit-ojn, `git status` konfirmas ke nenio pendas, kaj
`git diff` presas nenion ĉar ne estas nekonfirmitaj ŝanĝoj. Ĉi tiu estas la pura
deirpunkto por nova laboro.

## 4. Krei branĉon kaj labori sur ĝi

Nova laboro iras sur sian propran **branĉon**, ne rekte sur `main`. Kreu unu kaj
ŝanĝu al ĝi:

```console
$ git checkout -b docs-design
Switched to a new branch 'docs-design'
```

Aldonu la dezajnan dokumenton por la dokumentaro kaj konfirmu ĝin:

```console
$ printf '# DOCS DESIGN\n\nStructure of the documentation.\n' > docs-design.md
$ git add docs-design.md
$ git commit -m "Add docs design"
[docs-design 5f46a63] Add docs design
 1 file changed, 3 insertions(+)
```

La branĉo `docs-design` nun estas unu commit-on antaŭ `main`. Nenio sur `main`
ŝanĝiĝis — vi povas ŝanĝi tien kaj reen por konfirmi:

```console
$ git checkout main
Switched to branch 'main'
$ ls
README.md          # docs-design.md ne estas ĉi tie; ĝi vivas sur la alia branĉo

$ git checkout docs-design
Switched to branch 'docs-design'
```

## 5. Kunfandi la branĉon reen kaj solvi konflikton

Por okazigi konflikton, ni lasu ambaŭ branĉojn ŝanĝi **la saman linion** de la
README.

Sur `main`, alĝustigu la priskriban linion:

```console
$ git checkout main
$ printf '# NLP Esperantilo\n\nAn NLP library for the Esperanto language.\n' > README.md
$ git commit -am "Reword README description"
[main a1b2c3d] Reword README description
```

Sur `docs-design`, ŝanĝu *la saman linion* alimaniere:

```console
$ git checkout docs-design
$ printf '# NLP Esperantilo\n\nA rule-based NLP toolkit for Esperanto.\n' > README.md
$ git commit -am "Reword README description"
[docs-design e4f5a6b] Reword README description
```

Nun kunfandu `docs-design` en `main`. Git ne povas decidi kiu vortumo venkas:

```console
$ git checkout main
$ git merge docs-design
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

Malfermu `README.md`. Git markis la konfliktan regionon:

```text
# NLP Esperantilo

<<<<<<< HEAD
An NLP library for the Esperanto language.
=======
A rule-based NLP toolkit for Esperanto.
>>>>>>> docs-design
```

- Ĉio inter `<<<<<<< HEAD` kaj `=======` estas **via** versio (`main`).
- Ĉio inter `=======` kaj `>>>>>>> docs-design` estas la **enveninta** versio.

**Solvu** ĝin redaktante la dosieron ĝis la fina teksto, kiun vi volas, kaj
forigante ĉiujn tri liniojn de markiloj:

```text
# NLP Esperantilo

A rule-based NLP library for the Esperanto language.
```

Poste preparu la solvitan dosieron kaj kompletigu la kunfandon:

```console
$ git add README.md
$ git commit -m "Merge docs-design into main"
[main 92c1041] Merge docs-design into main
```

La historio nun montras ambaŭ liniojn de laboro kunigitajn per **kunfanda commit**:

```console
$ git log --oneline --graph
*   92c1041 Merge docs-design into main
|\
| * e4f5a6b Reword README description
* | a1b2c3d Reword README description
|/
* 7b0978f Add README
* 29434cf Initial commit
```

La branĉo `docs-design` plenumis sian celon kaj povas esti forigita:

```console
$ git branch -d docs-design
Deleted branch docs-design (was e4f5a6b).
```

## 6. Konekti remoton kaj puŝi (push)

Ĝis nun ĉio vivas sur via maŝino. Por kunhavigi ĝin, kreu malplenan deponejon en
GitHub (vidu la [GitHub-sekcion](../github/first-steps.md)), poste konektu ĝin kiel
remoton **`origin`** kaj puŝu:

```console
$ git remote add origin https://github.com/jparisu/nlp-esperantilo.git
$ git push -u origin main
Enumerating objects: 12, done.
Writing objects: 100% (12/12), 1.24 KiB, done.
To https://github.com/jparisu/nlp-esperantilo.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

La opcio `-u` ligas vian lokan `main` al `origin/main`, do ekde nun simplaj
`git push` kaj `git pull` sufiĉas.

## Resumo

En unu mallonga sesio vi uzis ĉiun kernan ideon de ĉi tiu sekcio:

- **`init`** por krei deponejon kaj **`.gitignore`** por teni ĝin pura,
- **`add`** kaj **`commit`** por registri instantfotojn,
- **`status`**, **`log`** kaj **`diff`** por inspekti la staton,
- **`branch`** / **`checkout`** por labori izolite,
- **`merge`** —inkluzive de **solvado de konflikto**— por kunigi la laboron,
- **`remote`** kaj **`push`** por kunhavigi ĝin kun la mondo.

Ĉi tio estas ekzakte la ciklo, kiun vi ripetos, denove kaj denove, dum la resto de
la projekto. La sekva paŝo estas fari ĝin *kiel teamo*, pri kio temas la
[GitHub-sekcio](../github/index.md).
