# Oftaj demandoj

Kutimaj demandoj pri Esperanto kaj pri transformi ĝin en datumojn por la biblioteko.
Ĉiu respondo ligas al la paĝo, kie la temo estas traktata pli detale.

??? question "Kio estas Esperanto, en unu frazo?"
    Konstruita internacia helplingvo, publikigita de L. L. Zamenhof en 1887, dezajnita
    por esti **regula kaj facile lernebla** — sen gramatikaj esceptoj. Vidu
    [Historio](history.md).

??? question "Kial konstrui NLP-bibliotekon specife por Esperanto?"
    Ĉar ĝia gramatiko estas plene regula, do **regul-bazitaj** tokenizilo, lematizilo
    kaj vortklasa markilo estas efektive realigeblaj — la finaĵoj kaj afiksoj sekvas
    regulojn, kiuj neniam rompiĝas, male al la naturaj lingvoj. Vidu
    [Historio § Kial ĝi gravas ĉi tie](history.md#kial-gi-gravas-ci-tie).

??? question "Kiel mi scias la vortklason de vorto?"
    El ĝia fina vokalo: `-o` estas substantivo, `-a` adjektivo, `-e` adverbo, `-i`
    verbo en infinitivo. Ĉi tiu sola regulo kovras la plimulton de la enhavaj vortoj.
    Vidu [Gramatiko § Vortklasaj finaĵoj](grammar.md#vortklasaj-finajoj).

??? question "Kiel funkcias la lematizado en Esperanto?"
    Senŝeligu la gramatikajn finaĵojn kaj afiksojn de vorto por atingi ĝian radikon,
    poste remetu la vortklasan vokalon. `malsanulejojn` → forigu `-n`, `-j`, `-o`,
    poste `-ej-`, `-ul-`, `mal-` → radiko `san-`. Ĉiu paŝo estas serĉo en tabelo. Vidu
    [Gramatiko § Afiksoj](grammar.md#afiksoj).

??? question "Kio estas la korelativoj?"
    Regula 5 × 9-krado de 45 oftaj vortoj (kiu/tiu/iu/ĉiu/neniu × -o/-u/-a/-e/-am…),
    ĉiu prefikso plus finaĵo. Lernu la kradon kaj vi ricevas ĉiujn 45. Vidu
    [Gramatiko § Korelativoj](grammar.md#korelativoj).

??? question "Por kio estas la akuzativo `-n`?"
    Ĝi markas la **rektan objekton** de verbo (kaj la direkton de movo). Prenas ĝin kaj
    la substantivoj kaj iliaj adjektivoj, kaj ĝi staplas post la pluralo `-j`:
    `interesajn librojn`. Vidu [Gramatiko § Gramatikaj fleksioj](grammar.md#gramatikaj-fleksioj).

??? question "Kiel mi traktu la specialajn literojn `ĉ ĝ ĥ ĵ ŝ ŭ` en la kodo?"
    Traktu ilin kiel ordinarajn Unikodajn literojn kaj **normigu** la enigon al unu
    sola kanona formo (NFC, realaj diakritaj signoj) antaŭ la tokenizado, konvertante la
    x-sistemon (`cx`, `gx`, …) aŭ la h-sistemon se ĉeestas. Vidu
    [Gramatiko § Alfabeto](grammar.md#alfabeto).

??? question "Kio validas kiel ignorinda vorto en Esperanto?"
    La artikolo `la`, la pronomoj, la korelativoj, kaj fiksa aro da prepozicioj,
    konjunkcioj kaj oftaj adverboj — plejparte fermitaj klasoj, do la listo estas finia.
    Ĉi tiu projekto distribuas 122 el ili — nur *radikojn*, ĉar la fleksiitajn
    formojn generas reguloj. Vidu
    [`resources/README.md` § Roots, not forms](https://github.com/jparisu/nlp-esperantilo/blob/main/resources/README.md#roots-not-forms).

??? question "De kie la biblioteko prenas siajn vortlistojn?"
    El JSON-dosieroj sub `resources/`, kiuj estas la sola fonto de vero: la dokumentaro
    prezentas ilin konstrutempe kaj la biblioteko legos la samajn dosierojn rultempe, do
    ili neniam povas malkonsenti. Vidu [`resources/README.md`](https://github.com/jparisu/nlp-esperantilo/blob/main/resources/README.md).

??? question "Kie mi povas trovi realan Esperantan tekston por testi la bibliotekon?"
    En korpusoj kiel la [Tekstaro de Esperanto](https://tekstaro.com), la Esperanta
    Vikipedio, kaj publik-domajnaj libroj ĉe Project Gutenberg — atentu la licencon de
    ĉiu fonto. Vidu [Rimedoj § Korpusoj](resources.md#korpusoj).

??? question "Ĉu la gramatika enhavo ĉi tie estas fidinda?"
    Ĝi sekvas *A Complete Grammar of Esperanto* de Ivy Kellerman Reed (1910),
    publik-domajnan referencon inkluzivitan en la deponejo. Vidu
    [Rimedoj § Libroj](resources.md#libroj).
