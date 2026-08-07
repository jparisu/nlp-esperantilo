# Gramatiko

Ĉi tiu estas la centra referenca paĝo de la Esperanto-sekcio. Ĝi kolektas la
regulojn, kiujn bezonas regul-bazita prilabora ĉeno — por la tokenizilo, la
lematizilo, la vortklasa markilo kaj la traktado de ignorindaj vortoj. Ĉar la
morfologio de Esperanto ne havas esceptojn, ĉiun regulon sube eblas transformi
preskaŭ rekte en kodon.

La gvida ideo: Esperanta vorto konstruiĝas el **radiko** plus **gramatikaj finaĵoj**
kaj laŭvolaj **afiksoj**. Forigu la finaĵojn kaj afiksojn kaj vi havas la lemon; legu
la finaĵojn kaj vi havas la vortklason kaj la fleksion.

!!! note "Kion ĉi tiu paĝo ne kovras"
    La **participoj** (`-ant-`, `-int-`, `-ont-` aktivaj; `-at-`, `-it-`, `-ot-`
    pasivaj), la kunmetitaj tempoj formataj el ili kun `esti`, kaj la pasivo estas
    same regulaj, sed ili ne estas traktataj ĉi tie. Prilabora ĉeno, kiu efektivigas
    nur la subajn regulojn, misanalizos formojn kiel `leganta`, `legita` aŭ
    `estas legata`.

!!! quote "Referenco"
    La reguloj kaj ekzemploj sur ĉi tiu paĝo sekvas la klasikan **_A Complete Grammar
    of Esperanto_** de Ivy Kellerman Reed (1910), publik-domajna verko inkluzivita en
    la deponejo ĉe `resources/esperanto/books/esperanto_grammar.txt`. Vidu
    [Rimedoj § Libroj](resources.md#libroj) por la plena citaĵo.

## Alfabeto

Esperanto uzas latinan alfabeton de **28 literoj**. Ĝi estas strikte **fonetika**: ĉiu
litero estas ĉiam prononcata same, kaj ĉiu sono estas skribata per ekzakte unu litero.
Ses literoj portas diakritajn signojn: la kvin cirkumfleksitajn konsonantojn uzas
neniu alia lingvo, kaj `ŭ` aperas ankaŭ en la latina alfabeto de la belorusa.

| Litero | Nomo | Sono |
| --- | --- | --- |
| `ĉ` | ĉo | kiel *ĉ* en "ĉevalo" |
| `ĝ` | ĝo | kiel *ĝ* en "ĝardeno" (voĉa) |
| `ĥ` | ĥo | forta *ĥ*, kiel en "eĥo" |
| `ĵ` | ĵo | kiel *ĵ* en "ĵurnalo" |
| `ŝ` | ŝo | kiel *ŝ* en "ŝipo" |
| `ŭ` | ŭo | mallonga *ŭ* en diftongoj, kiel en "aŭto" |

La literoj `q`, `w`, `x`, `y` **ne** apartenas al la alfabeto.

!!! warning "La kodoprezento gravas por la tokenizado"
    La diakritaj signoj estas realaj Unikodaj literoj (`ĉ` estas U+0109), ne `c` plus
    kombina signo — sed teksto trovita en la reto povas uzi ambaŭ formojn. Ekzistas
    ankaŭ du ASCII-alternativoj por klavaroj, kiuj ne povas tajpi la diakritajn signojn:

    - la **x-sistemo**: `cx gx hx jx sx ux` por `ĉ ĝ ĥ ĵ ŝ ŭ`;
    - la **h-sistemo** (el la *Fundamento*): `ch gh hh jh sh u`.

    Fortika tokenizilo devus **normigi** la enigon al unu sola kanona formo (Unikoda
    NFC, realaj diakritaj signoj) antaŭ ol apliki ajnan alian regulon. La datumdosieroj
    de ĉi tiu projekto konservas la realajn diakritajn signojn kaj neniam la x-sistemon
    (vidu [Vortprovizo § Formato](vocabulary.md#formato)).

## Vortklasaj finaĵoj

Ĉi tiu estas la ununura plej utila regulo por vortklasa markado kaj lematizado: la
**fina vokalo de kompleta vorto markas ĝian vortklason**.

| Finaĵo | Vortklaso | Ekzemplo | Radiko | Signifo (angle) |
| --- | --- | --- | --- | --- |
| `-o` | substantivo | `libro` | `libr-` | book |
| `-a` | adjektivo | `bona` | `bon-` | good |
| `-e` | adverbo (derivita) | `rapide` | `rapid-` | quickly |
| `-i` | verbo (infinitivo) | `kanti` | `kant-` | to sing |

El unu radiko vi ricevas la tutan familion: `muziko`, `muzika`, `muzike`. Por
**lematizi**, forigu la gramatikan finaĵon (kaj ajnan fleksion sube) por reakiri la
radikon, kaj poste remetu la vortklasan vokalon por akiri la vortaran formon.

## Gramatikaj fleksioj

La substantivoj kaj adjektivoj prenas du laŭvolajn finaĵojn, ĉiam **post** la
vortklasa vokalo:

| Finaĵo | Signifo | Ekzemplo |
| --- | --- | --- |
| `-j` | pluralo | `libroj`, `bonaj` |
| `-n` | akuzativo (rekta objekto) | `libron`, `bonan` |
| `-jn` | pluralo **kaj** akuzativo | `bonajn librojn` |

Du reguloj igas ilin plene regulaj:

- **La adjektivoj akordas** kun sia substantivo laŭ nombro kaj kazo: *"la bonaj
  libroj"*, *"mi legas interesajn librojn"*.
- La ordo estas fiksa: radiko → vortklasa vokalo → `-j` → `-n`. Do la analizo de
  `librojn` estas `libr-` + `-o` (substantivo) + `-j` (pluralo) + `-n` (akuzativo).

La akuzativo ankaŭ markas la direkton de movo, sed por la morfologia analizo gravas la
sufikso `-n`.

## Verba sistemo

La verboj **ne** konjugaciiĝas laŭ persono aŭ nombro — nur laŭ tempo kaj modo, kun unu
sola finaĵo por ĉiu. La sama radiko prenas ajnan el ĉi tiuj:

| Finaĵo | Tempo / modo | Ekzemplo (`kant-`, kanti) |
| --- | --- | --- |
| `-as` | prezenco | `kantas` |
| `-is` | preterito | `kantis` |
| `-os` | futuro | `kantos` |
| `-us` | kondicionalo | `kantus` |
| `-u` | imperativo / volitivo | `kantu!` |
| `-i` | infinitivo | `kanti` |

`mi kantas`, `vi kantas`, `ili kantas` — la verbo neniam ŝanĝiĝas laŭ la subjekto. Por
lematizi verbon, anstataŭigu ĝian tempan/modan finaĵon per `-i` (`kantis → kanti`).

## La artikolo

Ekzistas **unu** artikolo, la difinita `la`. Ĝi estas **nevariebla** — sen pluralo, sen
genro, sen kazo:

- `la libro`, `la libroj`, `la bona libro`.

**Ne ekzistas nedifinita artikolo**: `libro` signifas kaj "libro" kaj "unu libro". `la`
estas natura ignorinda vorto (vidu [Vortprovizo](vocabulary.md#ignorindaj-vortoj)).

## Personaj pronomoj

La pronomoj estas malgranda, fermita aro — ideala por rekte kodigi:

| Pronomo | Signifo | Poseda (`+ -a`) |
| --- | --- | --- |
| `mi` | la parolanto | `mia` |
| `vi` | la alparolato (unu aŭ pluraj) | `via` |
| `li` | vira tria persono | `lia` |
| `ŝi` | ina tria persono | `ŝia` |
| `ĝi` | neŭtra tria persono | `ĝia` |
| `ni` | la parolanto kaj aliaj | `nia` |
| `ili` | plurala tria persono | `ilia` |
| `oni` | senpersona subjekto | `onia` |
| `si` | refleksiva: rilatas al la subjekto | `sia` |

La **akuzativo** de pronomo aldonas `-n`: `min`, `vin`, `lin`, `ŝin`, `nin`, `ilin`. La
posedaj pronomoj estas ordinaraj adjektivoj, do ili ankaŭ fleksiiĝas: `miajn librojn`.

## Korelativoj

La **korelativoj** estas rimarkinde regula 5 × 9-krado de 45 oftaj vortoj. Ĉiu estas
**prefikso** (la signifa kategorio) plus **finaĵo** (la tipo). Lernu la kradon kaj vi
ricevas ĉiujn 45 senpage.

La kvin prefiksoj:

| Prefikso | Signifo |
| --- | --- |
| `ki-` | demanda / rilata ("kiu", "kio") |
| `ti-` | montra ("tiu") |
| `i-` | nedifinita ("iu") |
| `ĉi-` | universala ("ĉiu", "ĉio") |
| `neni-` | nea ("neniu", "nenio") |

La naŭ finaĵoj kaj la plena tabelo:

| Finaĵo → tipo | `ki-` | `ti-` | `i-` | `ĉi-` | `neni-` |
| --- | --- | --- | --- | --- | --- |
| `-o` aĵo | kio | tio | io | ĉio | nenio |
| `-u` individuo | kiu | tiu | iu | ĉiu | neniu |
| `-a` speco | kia | tia | ia | ĉia | nenia |
| `-es` posedo | kies | ties | ies | ĉies | nenies |
| `-e` loko | kie | tie | ie | ĉie | nenie |
| `-am` tempo | kiam | tiam | iam | ĉiam | neniam |
| `-al` kaŭzo | kial | tial | ial | ĉial | nenial |
| `-el` maniero | kiel | tiel | iel | ĉiel | neniel |
| `-om` kvanto | kiom | tiom | iom | ĉiom | neniom |

La korelativoj en `-u` kaj `-a` prenas kaj `-j` kaj `-n` (`tiujn`, `kiuj`), kiel la
substantivoj kaj adjektivoj, al kiuj ili similas. Tiuj en `-o` prenas `-n` sed
**neniam** `-j` (`kion`, `tion` — *tioj* ne ekzistas), kaj tiuj en `-e` prenas `-n` por
marki direkton (`tien`, `kien`). La aliaj kvin finaĵoj estas neflekseblaj. La plimulto
de la korelativoj estas ignorindaj vortoj.

## Afiksoj

La afiksoj estas tio, kio igas la Esperantan vortprovizon **kunmeta** — kaj ili estas
la koro de la lematizado, ĉar longa vorto estas kutime radiko envolvita en afiksoj. Ili
alligiĝas *inter* la radiko kaj la gramatika finaĵo.

### Prefiksoj

| Prefikso | Signifo | Ekzemplo |
| --- | --- | --- |
| `mal-` | rekta malo | `bona` → `malbona` |
| `ge-` | ambaŭ seksoj kune | `patro` → `gepatroj` |
| `ek-` | subita komenco / mallonga ago | `iri` → `ekiri` |
| `re-` | denove / reen | `veni` → `reveni` |
| `dis-` | disigo, disĵeto | `doni` → `disdoni` |
| `mis-` | erare | `kompreni` → `miskompreni` |
| `bo-` | parenceco per edziĝo | `patro` → `bopatro` |
| `pra-` | pratempa / pra- (parenceco) | `avo` → `praavo` |

### Sufiksoj

| Sufikso | Signifo | Ekzemplo |
| --- | --- | --- |
| `-in-` | ina | `patro` → `patrino` |
| `-ist-` | profesiulo / ano | `instrui` → `instruisto` |
| `-ej-` | loko por | `lerni` → `lernejo` |
| `-il-` | ilo / instrumento | `tranĉi` → `tranĉilo` |
| `-ar-` | kolekto / aro | `arbo` → `arbaro` |
| `-et-` | malpligrandiga | `domo` → `dometo` |
| `-eg-` | pligrandiga | `domo` → `domego` |
| `-ul-` | persono karakterizita per | `juna` → `junulo` |
| `-an-` | membro / loĝanto | `urbo` → `urbano` |
| `-ec-` | abstrakta eco | `bona` → `boneco` |
| `-ig-` | igi / kaŭzi | `granda` → `grandigi` |
| `-iĝ-` | iĝi | `ruĝa` → `ruĝiĝi` |
| `-ind-` | inda je | `ami` → `aminda` |
| `-em-` | inklina al | `labori` → `laborema` |
| `-aĉ-` | malestima (malbona kvalito) | `domo` → `domaĉo` |

La afiksoj staplas. `mal-san-ul-ej-o` = `mal-` (malo) + `san-` (sano) + `-ul-`
(persono) + `-ej-` (loko) + `-o` (substantivo) = **malsanulejo** (laŭvorte "loko por
nesanaj personoj"). Lematizilo, kiu konas ĉi tiun afiksan tabelon, povas malkomponi
tiajn vortojn per reguloj.

## Nombroj kaj kunmetado

La bazaj (kardinalaj) nombroj konstruiĝas el manpleno da radikoj:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 100 | 1000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `nul` | `unu` | `du` | `tri` | `kvar` | `kvin` | `ses` | `sep` | `ok` | `naŭ` | `dek` | `cent` | `mil` |

La pli grandaj nombroj **kunmetiĝas** per apudmeto: `dek du` (12), `dudek` (20),
`dudek unu` (21), `cent tridek kvin` (135). Aldoni finaĵojn derivas rilatajn vortojn:

- ordaj nombroj per `-a`: `unua`, `dua`;
- obloj per `-obl-`: `duobla`;
- frakcioj per `-on-`: `duono`, `kvarono`;
- kolektivoj per `-op-`: `duope`.

Pli ĝenerale, **ajnaj du radikoj povas kunmetiĝi** en unu vorton, kun la lasta radiko
kiel kapo: `vapor-ŝipo` (vaporŝipo), `dorm-o-ĉambro` (dormoĉambro, kun ligilo `-o-` por
prononcebleco). La vortklaso de la kunmetaĵo venas de ĝia fina finaĵo, ekzakte kiel por
unuopa radiko.

## Prilaboritaj ekzemploj

Kunmetante la regulojn, jen frazo analizita vorto post vorto:

> **La juna instruistino legas interesan libron.**

| Vorto | Malkomponado | Analizo |
| --- | --- | --- |
| `La` | `la` | artikolo (ignorinda vorto) |
| `juna` | `jun-` + `-a` | adjektivo, nominativo, singularo |
| `instruistino` | `instru-` + `-ist-` + `-in-` + `-o` | substantivo, nominativo, singularo |
| `legas` | `leg-` + `-as` | verbo, prezenco (lemo `legi`) |
| `interesan` | `interes-` + `-a` + `-n` | adjektivo, akuzativo, singularo |
| `libron` | `libr-` + `-o` + `-n` | substantivo, akuzativo, singularo (lemo `libro`) |

Dua ekzemplo montras pluralon, akuzativan akordon kaj korelativon:

> **Ĉiuj miaj amikoj legas tiujn librojn.**

`Ĉiuj` (korelativo `ĉiu` + `-j`), `miaj` (poseda `mia` + `-j`), `amikoj` (`amik-o-j`) —
la subjekto estas plurala, do nenio prenas `-n`; `tiujn librojn` (`tiu-j-n`,
`libr-o-j-n`) estas la plurala akuzativa objekto, kaj la montra korelativo akordas kun
sia substantivo. Ĉi tiu regula akordo estas ĝuste tio, kion regul-bazita markilo povas
kontroli kaj ekspluati.

## Kien iri poste

- [Vortprovizo](vocabulary.md) — la afiksaj kaj ignorindaj listoj plene, pretaj por
  nutri la bibliotekon.
- [Python-Biblioteko § API](../python-library/api.md) — kiel ĉi tiuj reguloj fariĝas
  interfaco `Doc` / `Token`.
