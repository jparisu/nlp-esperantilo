# API-referenco

Ĉiu publika nomo de `esperantilo`, kun sia signaturo, siaj argumentoj kaj siaj
ekzemploj.

!!! info "Generita el la fontkodo"
    Nenio sur ĉi tiu paĝo estas verkita mane. Ĝi estas konstruita el la
    dokumentĉenoj de
    [`src/esperantilo/`](https://github.com/jparisu/nlp-esperantilo/tree/main/src/esperantilo)
    per [mkdocstrings](https://mkdocstrings.github.io/) ĉiufoje kiam la paĝaro
    estas konstruata, do ĝi ne povas kontraŭdiri la kodon. La `>>>`-ekzemploj
    ankaŭ estas rulataj de `pytest` — vidu
    [Gvidilo → Testado](../guide/python-library/testing.md#doctests).

    Ĉiu ero ligas al la precizaj linioj, kiujn ĝi dokumentas: malfaldu
    *Source* por legi ilin.

!!! note "Enhavo en la angla"
    La fontkodo kaj ĝiaj dokumentĉenoj estas verkitaj en la angla, do ĉi tiu
    paĝo aperas en la angla en ĉiuj lingvoj de la paĝaro. La Esperanta klarigo
    pri tio, kion la funkcio faras, troviĝas en
    [Fraz-dividado](sentence-segmentation.md).

::: esperantilo
    options:
      heading_level: 2
      members: false

::: esperantilo.__version__
    options:
      heading_level: 3

::: esperantilo.nlp
    options:
      heading_level: 2
      members:
        - sentence_tokenizer

::: esperantilo.wiki
    options:
      heading_level: 2
      members:
        - WikiPage
