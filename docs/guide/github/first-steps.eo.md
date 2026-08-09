# Unuaj paŝoj

Ĉi tiu paĝo kondukas vin de *neniu konto* al *via propra deponejo en GitHub*, preta
por la [laborfluo](workflow.md) kiu sekvas. Se vi jam havas konton kaj deponejon, vi
povas trarigardi ĝin kaj salti antaŭen.

## Krei konton

Iru al [github.com](https://github.com) kaj registriĝu. Senpaga konto sufiĉas por
ĉio en ĉi tiu gvidilo, inkluzive de privataj deponejoj kaj GitHub Actions.

Du fruajn paŝojn indas fari bone:

- **Vian profilon.** Uzu rekoneblan uzantnomon kaj realan nomon — en teama
  projekto, viaj kunlaborantoj kaj instruistoj bezonas scii kiu estas kiu. Viaj
  commit-oj estas ligitaj al la retpoŝta adreso agordita en
  [`git config`](../git/example.md), do uzu ĉi tie la saman retpoŝton.
- **Aŭtentigon por puŝi.** Ensaluti al la retejo uzas pasvorton; puŝi de la
  komandolinio **ne**. Vi bezonas unu el ĉi tiuj:
    - **Personal Access Token (PAT)**, uzatan anstataŭ pasvorto per HTTPS, aŭ
    - **SSH-ŝlosilon**, ŝlosilparon, kies publikan duonon vi aldonas al GitHub.

!!! tip "Kiun mi uzu?"
    Por labori en kajeroj aŭ puŝi malofte, **PAT per HTTPS** estas la plej simpla:
    kreu ĝin en **Settings → Developer settings → Personal access tokens**, kaj
    algluu ĝin kiam Git petas pasvorton. Por ofta loka laboro, **SSH-ŝlosilo**
    (aldonita en **Settings → SSH and GPG keys**) evitas retajpi ion ajn. Ambaŭ
    taŭgas — elektu unu kaj daŭrigu.

### Agordi la aŭtentigon sur via maŝino

Elektu unu el la du langetoj por aŭtentigi vin. Vi ne bezonas ambaŭ.

=== "PAT per HTTPS"

    **1. Kreu la ĵetonon.** En GitHub, **Settings → Developer settings →
    Personal access tokens → Fine-grained tokens → Generate new token**. Donu al
    ĝi nomon, limdaton kaj, sub **Repository access**, elektu la deponejojn,
    kiujn ĝi atingas. Sub **Permissions → Repository permissions** vi bezonas
    almenaŭ **Contents: Read and write**.

    **2. Kopiu ĝin tuj.** La ĵetono montriĝas unufoje. Se vi perdas ĝin, necesas
    generi alian.

    **3. Klonu per HTTPS.** Git petos uzantnomon kaj pasvorton: algluu la
    ĵetonon kiel pasvorton, ne tiun de via konto.

    ```bash
    git clone https://github.com/<uzanto>/<deponejo>.git
    ```

    **4. Evitu ripeti ĝin ĉe ĉiu puŝo.** Konservu la akreditilojn per
    *credential helper*:

    ```bash
    # Windows: venas kun Git for Windows, ĉifrita
    git config --global credential.helper manager

    # macOS: konservas ilin en la sistema ŝlosilaro
    git config --global credential.helper osxkeychain

    # Linukso: en plata teksto, en ~/.git-credentials
    git config --global credential.helper store
    ```

    !!! warning "`store` konservas la ĵetonon neĉifritan"
        En Linukso, `store` lasas la ĵetonon legebla en `~/.git-credentials`.
        Tio taŭgas por persona maŝino; sur komuna komputilo uzu
        `credential.helper cache`, kiu tenas ĝin nur en memoro dum iom da tempo.

    Oficiala dokumentaro:
    [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

=== "SSH-ŝlosilo"

    **1. Generu la ŝlosilparon.** Akceptu la vojon, kiun ĝi proponas. La
    *pasfrazo* estas nedeviga, sed indas meti ĝin: ĝi protektas la ŝlosilon, se
    iu atingas vian diskon.

    ```bash
    ssh-keygen -t ed25519 -C "via-retadreso@ekzemplo.com"
    ```

    **2. Registru la ŝlosilon ĉe la agento**, por ne tajpi la pasfrazon ĉe ĉiu
    operacio:

    ```bash
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    ```

    **3. Kopiu la publikan ŝlosilon.** Ĝi estas tiu, kiu finiĝas per `.pub`; la
    alia neniam eliras vian maŝinon.

    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```

    **4. Aldonu ĝin al GitHub.** Sub **Settings → SSH and GPG keys → New SSH
    key**, algluu la enhavon, donu al ĝi nomon, kiu identigas la komputilon, kaj
    konservu.

    **5. Kontrolu kaj klonu per SSH.** La unua konekto petos konfirmi la
    fingrospuron de la servilo.

    ```bash
    ssh -T git@github.com
    git clone git@github.com:<uzanto>/<deponejo>.git
    ```

    Oficiala dokumentaro:
    [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    kaj
    [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

!!! tip "Ĉu vi jam klonis per la malĝusta metodo?"
    Ne necesas kloni denove. La aŭtentigan metodon decidas la URL de la remoto,
    kaj ĝi ŝanĝeblas:

    ```bash
    git remote -v                                          # vidi la nunan
    git remote set-url origin git@github.com:<uzanto>/<deponejo>.git
    ```

Kun ambaŭ, identigu vin al Git antaŭ la unua commit — la sama adreso, kiun vi
uzis en GitHub, por ke la commit-oj estu atribuitaj al vi:

```bash
git config --global user.name "Via Nomo"
git config --global user.email "via-retadreso@ekzemplo.com"
```

## Krei deponejon

Klaku **New** (la verda butono sur via paĝo de deponejoj) kaj plenigu:

- **Nomo** — mallonga kaj priskriba, ekz. `nlp-esperantilo`.
- **Videbleco** — **publika** (ĉiu povas vidi ĝin) aŭ **privata** (nur vi kaj
  invititaj kunlaborantoj). Vi povas ŝanĝi ĉi tion poste.
- **Ekigi kun** — GitHub povas aldoni por vi tri dosierojn en la momento de la kreo:
    - **README**, la ĉefpaĝon de la deponejo;
    - **`.gitignore`**, antaŭplenigitan por la lingvo kiun vi elektas (elektu
      *Python*);
    - **licencon**, kiu diras kiel aliaj povas uzi vian kodon.

!!! note "README, .gitignore kaj licenco"
    Lasi GitHub-on krei ĉi tiujn signifas, ke la deponejo komenciĝas jam kun unu
    commit ene. Se anstataŭe vi konstruis la deponejon loke (kiel en la
    [Git-ekzemplo](../git/example.md)), lasu ĉi tiujn markobutonojn nemarkitaj kaj
    puŝu vian propran historion.

## Agordi ĝin

Kelkajn agordojn indas ŝanĝi frue, el la langeto **Settings** de la deponejo kaj ĝia
ĉefpaĝo:

- **Priskribo kaj temoj (topics).** Unulinia priskribo kaj kelkaj temaj etikedoj
  igas la deponejon pli facile trovebla kaj komprenebla.
- **Kunlaborantoj.** En **Settings → Collaborators**, invitu viajn teamanojn por ke
  ili povu puŝi al branĉoj kaj revizii kunfandajn petojn.
- **Defaŭlta branĉo.** Konfirmu, ke ĝi nomiĝas `main`.

La agordo, kiu *altrudas* sanan teaman laborfluon — protekti `main`, postuli
reviziojn kaj sukcesajn kontrolojn — estas sufiĉe grava por havi sian propran paĝon:
[Agordo de la deponejo](repository-configuration.md). Agordu tion kiam la laborfluo
kaj la Actions estas surloke.

## Esplori

La plej grandan parton de via tempo en GitHub vi pasigas legante deponejojn *de
aliaj personoj*. Ĉiu deponejo havas la samajn langetojn, kaj koni ilin igas legebla
ajnan projekton:

| Langeto |  |
| --- | --- |
| **Code** | La dosierojn, la README, la branĉan elektilon kaj la historion de commit-oj. |
| **Issues** | Raportitajn cimojn, taskojn kaj funkcio-petojn, malfermitajn kaj fermitajn. |
| **Pull requests** | Proponitajn ŝanĝojn en revizio, kaj la jam kunfanditajn. |
| **Actions** | La aŭtomatajn rulojn (testojn, konstruojn) kaj ĉu ili sukcesis. |
| **Insights** | La kontribuan agadon, kaj bildon pri kiel la projekto moviĝas. |

Trarigardi bone administratan projekton — legi kiel estas priskribitaj ĝiaj kunfandaj
petoj kaj kiel estas diskutataj ĝiaj problemoj — estas unu el la plej bonaj manieroj
lerni la konvenciojn de la programara kunlaboro.

## Problemoj kaj kunfandaj petoj

Ĉi tiuj du estas la spino de la kunlaboro en GitHub, kaj ili ludas malsamajn rolojn:

- **Problemo (issue)** priskribas *ion farendan aŭ riparendan*: cimon, taskon,
  demandon. Ĝi estas konversacio, ne kodo. La problemoj estas numeritaj (`#12`) kaj
  povas esti etikeditaj kaj asignitaj.
- **Kunfanda peto (pull request, PR)** proponas *realan ŝanĝon al la kodo*: "jen
  branĉo kun commit-oj, bonvolu revizii kaj kunfandi ĝin". Ĝi ankaŭ estas numerita
  kaj diskutata, sed ĝi portas diff-on.

La du referencas unu la alian. Kunfanda peto povas diri *"Closes #12"* en sia
priskribo, kaj kiam ĝi kunfandiĝas, GitHub aŭtomate fermas la problemon #12 kaj
kunligas la du. Ĉi tio ligas la *planon* (problemoj) al la *laboro* (kunfandaj
petoj) en spurebla historio.

```mermaid
flowchart LR
    I["Issue: Add stop-word list"] -.-> PR["Pull request: Closes the issue"]
    PR -->|merged| M[main]
    PR -.->|auto-closes| I
```

La kunfanda peto mem — kiel malfermi, priskribi, revizii kaj kunfandi ĝin — estas la
temo de la sekva paĝo.

## Kien iri poste

- [Laborfluo](workflow.md) — la kompleta ciklo branĉo → commit → kunfanda peto →
  kunfando.
