# Oftaj demandoj

Kutimaj demandoj pri GitHub kaj la kunlabora laborfluo. Ĉiu respondo ligas al la
paĝo, kie la temo estas traktata pli detale.

??? question "Kio estas la diferenco inter Git kaj GitHub?"
    **Git** estas la versikontrola ilo, kiu funkcias sur via komputilo; **GitHub**
    estas retejo, kiu gastigas Git-deponejojn kaj aldonas kunlaborajn funkciojn
    (kunfandaj petoj, problemoj, Actions, Pages). Vi povas uzi Git sen GitHub; GitHub
    ĉiam uzas Git sube. Vidu [Kio estas GitHub](github.md#git-ne-estas-github).

??? question "Ĉu mi devas pagi por uzi GitHub-on?"
    Ne. Senpaga konto kovras ĉion en ĉi tiu gvidilo: publikajn *kaj* privatajn
    deponejojn, senlimajn kunlaborantojn, GitHub Actions kaj GitHub Pages. La pagaj
    planoj aldonas pli altajn limojn kaj organizajn funkciojn, kiujn vi ĉi tie ne
    bezonos.

??? question "Kiam mi kreas branĉon kaj kiam mi faras fork?"
    Se vi havas skriban aliron al la deponejo (la via aŭ tiu de via teamo), kreu
    **branĉon**. Se vi ne havas (la publika deponejo de alia persono), faru **fork**
    de ĝi —kreu vian propran kopion— kaj poste malfermu kunfandan peton reen al la
    originalo. Vidu [Laborfluo § Branĉo aŭ fork](workflow.md#branco-au-fork).

??? question "Kio estas ekzakte kunfanda peto?"
    Propono kunfandi unu branĉon en alian, kun diff, priskribo kaj diskuto kunligitaj.
    Ĝi estas kie okazas la revizio kaj la aŭtomataj kontroloj antaŭ ol la kodo atingas
    `main`. Vidu [Laborfluo § Kunfanda peto](workflow.md#kunfanda-peto).

??? question "Kio estas la diferenco inter problemo (issue) kaj kunfanda peto?"
    **Problemo** priskribas ion farendan aŭ riparendan — ĝi estas konversacio, sen
    kodo. **Kunfanda peto** proponas realan ŝanĝon kaj portas diff-on. PR povas diri
    `Closes #12` por aŭtomate fermi la problemon kiun ĝi solvas ĉe la kunfando. Vidu
    [Unuaj paŝoj § Problemoj kaj kunfandaj petoj](first-steps.md#problemoj-kaj-kunfandaj-petoj).

??? question "Git petas pasvorton kiam mi puŝas, sed ĝi rifuzas mian GitHub-pasvorton. Kial?"
    GitHub ĉesis akcepti la kontajn pasvortojn por Git-operacioj. Puŝu per HTTPS kun
    **Personal Access Token** anstataŭ la pasvorto, aŭ agordu **SSH-ŝlosilon**. Vidu
    [Unuaj paŝoj § Krei konton](first-steps.md#krei-konton).

??? question "Kion signifas la verda insigno `Verified` sur commit?"
    Ke la commit estis **kriptografie subskribita** per ŝlosilo, kiun GitHub asocias
    kun la aŭtoro, do ĝia aŭtoreco estas fidinda. Agordu ĝin per GPG- aŭ
    SSH-subskribado. Vidu [Laborfluo § Subskribado de commit-oj](workflow.md#subskribado-de-commit-oj).

??? question "Kio estas GitHub Actions?"
    Aŭtomatigo, kiu ruliĝas sur la serviloj de GitHub kiam okazas evento (push,
    kunfanda peto). Ĉi tiu deponejo uzas ilin por ruli testojn, kontroli la
    ortografion kaj konstrui la dokumentaron aŭtomate. Vidu [GitHub Actions](actions.md).

??? question "Kontrolo sur mia kunfanda peto estas ruĝa. Kion mi faru?"
    Malfermu la malsukcesan kontrolon en la langeto **Actions** kaj legu ĝian
    protokolon — ĝi nomas ekzakte kio malsukcesis. Ĉiu kontrolo estas komando, kiun
    vi povas ruli loke (`pytest`, `mkdocs build --strict`, `codespell`); riparu la
    problemon, puŝu denove, kaj la kontrolo reruliĝas. Vidu [GitHub Actions](actions.md).

??? question "Kial mi ne povas puŝi rekte al `main`?"
    Ĉar la deponejo havas **ruleton**, kiu protektas ĝin: la ŝanĝoj devas trairi
    revizititan kunfandan peton. Ĝi estas intenca — ĝi malhelpas, ke `main` rompiĝu.
    Vidu [Agordo de la deponejo](repository-configuration.md).

??? question "Kiel estas publikigita ĉi tiu dokumentara retejo?"
    Laborfluo konstruas la MkDocs-paĝaron kaj puŝas ĝin al la branĉo `gh-pages`, kiun
    **GitHub Pages** servas ĉe `https://jparisu.github.io/nlp-esperantilo/`. La
    kunfandaj petoj ankaŭ ricevas provizoran antaŭrigardan paĝaron. Vidu
    [GitHub Pages](pages.md).

??? question "Mi malfermis kunfandan peton sed ne estas antaŭrigarda ligilo. Kial?"
    Plej verŝajne la kunfanda peto venas de **fork**, kiu ruliĝas kun nur-lega ĵetono
    kaj ne povas publikigi antaŭrigardon. La dokumentaro tamen konstruiĝas kaj
    kontroliĝas; ĝi nur ne ricevas URL-on. Vidu
    [GitHub Pages § Kunfandaj petoj de fork-oj](pages.md#antaurigardi-kunfandan-peton).
