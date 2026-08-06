# Oftaj demandoj

Kutimaj demandoj kaj duboj pri Git. Ĉiu respondo ligas al la paĝo, kie la temo estas
traktata pli detale.

??? question "Kio estas la diferenco inter Git kaj GitHub?"
    **Git** estas la versikontrola ilo, kiu funkcias sur via komputilo kaj registras
    la historion de viaj dosieroj. **GitHub** estas retejo, kiu gastigas
    Git-deponejojn interrete por ke oni kunhavigu kaj kunlaboru. Vi povas uzi Git
    tute sen GitHub; GitHub ĉiam uzas Git sube. Vidu [Kio estas Git](git.md) kaj la
    [GitHub-sekcion](../github/index.md).

??? question "Ĉu mi bezonas retkonekton por uzi Git?"
    Ne. Git estas [distribuita](git.md#iom-da-historio): via klono enhavas la tutan
    historion, do vi povas fari commit-ojn, krei branĉojn, inspekti la protokolon kaj
    reiri en la tempo tute senrete. Vi bezonas konekton nur por interŝanĝi commit-ojn kun
    remoto (`clone`, `fetch`, `push`, `pull`).

??? question "Kio estas la diferenco inter `add` kaj `commit`?"
    `git add` movas ŝanĝojn al la **prepara zono** — malneto de via sekva commit.
    `git commit` registras ĉion preparitan kiel konstantan punkton en la historio.
    Prepari unue ebligas al vi elekti ekzakte kio eniras ĉiun commit-on. Vidu
    [La tri zonoj](git.md#la-tri-zonoj).

??? question "Mi plenumis `git commit` kaj malfermiĝis redaktilo plena de teksto. Kio okazis?"
    Vi faris commit-on sen mesaĝo (`-m`), do Git malfermis vian defaŭltan redaktilon
    por verki unu. Tajpu mallongan mesaĝon en la unua linio, konservu kaj fermu la
    redaktilon. Se ĝi estas **Vim** kaj vi blokiĝis, premu `Esc`, poste tajpu `:wq`
    kaj premu Enter por konservi kaj eliri. Por eviti ĉi tion, ĉiam faru la commit-on
    per `git commit -m "via mesaĝo"`.

??? question "Kiel mi verku bonan mesaĝon de commit?"
    Tenu ĝin mallonga, en imperativo, kaj priskribu *kion* faras la commit:
    `Add stop-word list`, ne `stuff` aŭ `fixed things`. Unu kohera ŝanĝo por ĉiu
    commit. La konvencioj de mesaĝoj estas traktataj kiel temo de laborfluo en
    [GitHub § Laborfluo](../github/workflow.md).

??? question "Mi eraris en mia lasta commit. Ĉu mi povas malfari ĝin?"
    Jes, se vi **ankoraŭ ne puŝis** ĝin. Uzu `git reset --soft HEAD~1` por malfari la
    commit-on konservante ĝiajn ŝanĝojn preparitaj, korektu, kaj konfirmu denove. Se
    vi jam puŝis kaj kunhavigis ĝin, uzu `git revert` anstataŭe. Vidu
    [Malfari ŝanĝojn](undoing-changes.md).

??? question "Mi ŝanĝis dosieron kaj volas revenigi la originalon. Kiel?"
    Se la ŝanĝo ne estas konfirmita, `git restore <dosiero>` forĵetas ĝin kaj
    restarigas la lastan konfirmitan version. Atentu: nekonfirmitaj ŝanĝoj forĵetitaj
    tiel perdiĝas por ĉiam. Vidu
    [Malfari ŝanĝojn](undoing-changes.md#git-restore-forjeti-sangojn-en-la-labordosierujo).

??? question "Kio estas kunfanda konflikto kaj ĉu mi rompis ion?"
    Nenio estas rompita. Konflikto okazas, kiam du branĉoj ŝanĝis la **samajn liniojn**
    de dosiero kaj Git ne povas decidi kiun version konservi, do ĝi demandas vin.
    Redaktu la dosieron, forigu la markilojn `<<<<<<<`, `=======`, `>>>>>>>`, lasu la
    tekston kiun vi volas, poste faru `git add` kaj commit. La
    [Ekzemplo](example.md#5-kunfandi-la-brancon-reen-kaj-solvi-konflikton) trairas
    unu paŝon post paŝo.

??? question "Kio estas la diferenco inter `git pull` kaj `git fetch`?"
    `git fetch` elŝutas novajn commit-ojn de la remoto sed **ne** ŝanĝas viajn
    laborajn dosierojn. `git pull` faras fetch **kaj** kunfandas tiujn commit-ojn en
    vian nunan branĉon en unu paŝo. Vidu [Komandoj § git pull](commands.md#git-pull).

??? question "Ĉu mi konfirmu mian virtualan medion aŭ `__pycache__`?"
    Ne. Tiuj generiĝas loke kaj ne apartenas al la historio. Listigu ilin en dosiero
    [`.gitignore`](commands.md#la-dosiero-gitignore) por ke Git ilin ignoru. La
    `.gitignore` de ĉi tiu projekto estas bona ŝablono.

??? question "Mi hazarde konfirmis dosieron, kiu devus esti ignorata. Kaj nun?"
    Aldonu ĝin al `.gitignore`, poste ĉesu spuri ĝin per `git rm --cached <dosiero>`
    kaj faru commit. La dosiero restas sur via disko sed forlasas la deponejon. Vidu
    [Komandoj § .gitignore](commands.md#la-dosiero-gitignore).

??? question "Kion signifas `HEAD`?"
    `HEAD` estas montrilo al *kie vi estas nun* en la historio — normale la lasta
    commit de la branĉo sur kiu vi estas. Notacioj kiel `HEAD~1` signifas "unu commit
    antaŭ `HEAD`". Vidu [Branĉoj](organization.md#brancoj).

??? question "Ĉu estas sekure forigi branĉon post ĝia kunfando?"
    Jes. Post kunfando de branĉo, ĝiaj commit-oj plu vivas en la cela branĉo, do
    `git branch -d <branĉo>` forigas nur la montrilon, ne la historion. Vidu la
    [Ekzemplon](example.md#5-kunfandi-la-brancon-reen-kaj-solvi-konflikton).
