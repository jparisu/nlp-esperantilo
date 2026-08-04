# Preguntas frecuentes

Preguntas habituales sobre GitHub y el flujo de trabajo colaborativo. Cada
respuesta enlaza a la página donde el tema se trata en detalle.

??? question "¿Cuál es la diferencia entre Git y GitHub?"
    **Git** es la herramienta de control de versiones que se ejecuta en tu
    ordenador; **GitHub** es un sitio web que aloja repositorios Git y añade
    funciones de colaboración (pull requests, issues, Actions, Pages). Puedes usar
    Git sin GitHub; GitHub siempre usa Git por debajo. Véase
    [Qué es GitHub](github.md#git-no-es-github).

??? question "¿Tengo que pagar para usar GitHub?"
    No. Una cuenta gratuita cubre todo lo de esta guía: repositorios públicos *y*
    privados, colaboradores ilimitados, GitHub Actions y GitHub Pages. Los planes
    de pago añaden límites más altos y funciones de organización que aquí no
    necesitarás.

??? question "¿Cuándo creo una rama y cuándo hago un fork?"
    Si tienes acceso de escritura al repositorio (el tuyo o el de tu equipo), crea
    una **rama**. Si no lo tienes (el repositorio público de otra persona), hazle
    un **fork** —crea tu propia copia— y luego abre un pull request de vuelta al
    original. Véase [Flujo de trabajo § Rama o fork](workflow.md#rama-o-fork).

??? question "¿Qué es exactamente un pull request?"
    Una propuesta de fusionar una rama en otra, con un diff, una descripción y una
    discusión adjuntas. Es donde ocurren la revisión y las comprobaciones
    automatizadas antes de que el código llegue a `main`. Véase
    [Flujo de trabajo § Pull request](workflow.md#pull-request).

??? question "¿Cuál es la diferencia entre un issue y un pull request?"
    Un **issue** describe algo que hacer o arreglar — es una conversación, sin
    código. Un **pull request** propone un cambio real y lleva un diff. Un PR puede
    decir `Closes #12` para cerrar automáticamente el issue que resuelve al
    fusionarse. Véase
    [Primeros pasos § Issues y pull requests](first-steps.md#issues-y-pull-requests).

??? question "Git me pide una contraseña al hacer push, pero rechaza la de mi cuenta de GitHub. ¿Por qué?"
    GitHub dejó de aceptar las contraseñas de cuenta para operaciones de Git. Haz
    push sobre HTTPS con un **Personal Access Token** en lugar de la contraseña, o
    configura una **clave SSH**. Véase
    [Primeros pasos § Crear una cuenta](first-steps.md#crear-una-cuenta).

??? question "¿Qué significa la insignia verde `Verified` en un commit?"
    Que el commit fue **firmado criptográficamente** con una clave que GitHub
    asocia con el autor, de modo que su autoría es de fiar. Configúralo con firma
    GPG o SSH. Véase [Flujo de trabajo § Firma de commits](workflow.md#firma-de-commits).

??? question "¿Qué son las GitHub Actions?"
    Automatización que se ejecuta en los servidores de GitHub cuando ocurre un
    evento (un push, un pull request). Este repositorio las usa para ejecutar
    pruebas, revisar la ortografía y construir la documentación automáticamente.
    Véase [GitHub Actions](actions.md).

??? question "Una comprobación de mi pull request está en rojo. ¿Qué hago?"
    Abre la comprobación que falla en la pestaña **Actions** y lee su log — indica
    exactamente qué falló. Cada comprobación es un comando que puedes ejecutar en
    local (`pytest`, `mkdocs build --strict`, `codespell`); arregla el problema,
    vuelve a hacer push y la comprobación se repite. Véase
    [GitHub Actions](actions.md).

??? question "¿Por qué no puedo hacer push directamente a `main`?"
    Porque el repositorio tiene un **ruleset** que lo protege: los cambios deben
    pasar por un pull request revisado. Es deliberado — evita que `main` se rompa.
    Véase [Configuración del repositorio](repository-configuration.md).

??? question "¿Cómo se publica este sitio web de documentación?"
    Un workflow construye el sitio MkDocs y lo sube a la rama `gh-pages`, que
    **GitHub Pages** sirve en `https://jparisu.github.io/nlp-esperantilo/`. Los
    pull requests también obtienen un sitio de previsualización temporal. Véase
    [GitHub Pages](pages.md).

??? question "Abrí un pull request pero no hay enlace de previsualización. ¿Por qué?"
    Lo más probable es que el pull request venga de un **fork**, que se ejecuta con
    un token de solo lectura y no puede publicar una previsualización. La
    documentación igualmente se construye y se comprueba; solo que no obtiene URL.
    Véase [GitHub Pages § Pull requests desde forks](pages.md#previsualizar-un-pull-request).
