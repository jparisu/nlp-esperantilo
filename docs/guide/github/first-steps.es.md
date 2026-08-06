# Primeros pasos

Esta página te lleva de *no tener cuenta* a *tener tu propio repositorio en
GitHub*, listo para el [flujo de trabajo](workflow.md) que sigue. Si ya tienes
cuenta y un repositorio, puedes ojearla y saltar adelante.

## Crear una cuenta

Ve a [github.com](https://github.com) y regístrate. Una cuenta gratuita basta
para todo lo de esta guía, incluidos los repositorios privados y GitHub Actions.

Dos pasos iniciales conviene hacerlos bien:

- **Tu perfil.** Usa un nombre de usuario reconocible y un nombre real — en un
  proyecto en equipo, tus compañeros y profesores necesitan saber quién es quién.
  Tus commits se vinculan a la dirección de correo configurada en
  [`git config`](../git/example.md), así que usa aquí el mismo correo.
- **Autenticación para hacer push.** Iniciar sesión en el sitio web usa una
  contraseña; hacer push desde la línea de comandos **no**. Necesitas una de
  estas dos:
    - un **Personal Access Token (PAT)**, usado en lugar de una contraseña sobre
      HTTPS, o
    - una **clave SSH**, un par de claves cuya mitad pública añades a GitHub.

!!! tip "¿Cuál debo usar?"
    Para trabajar en notebooks o hacer push de vez en cuando, un **PAT sobre
    HTTPS** es lo más simple: créalo en **Settings → Developer settings →
    Personal access tokens**, y pégalo cuando Git te pida una contraseña. Para
    trabajo local frecuente, una **clave SSH** (añadida en **Settings → SSH and
    GPG keys**) evita tener que reescribir nada. Cualquiera vale — elige una y
    sigue adelante.

## Crear un repositorio

Haz clic en **New** (el botón verde en tu página de repositorios) y rellena:

- **Nombre** — corto y descriptivo, p. ej. `nlp-esperantilo`.
- **Visibilidad** — **público** (cualquiera puede verlo) o **privado** (solo tú y
  los colaboradores invitados). Puedes cambiarlo más tarde.
- **Inicializar con** — GitHub puede añadirte tres archivos en el momento de la
  creación:
    - un **README**, la portada del repositorio;
    - un **`.gitignore`**, precargado para el lenguaje que elijas (elige
      *Python*);
    - una **licencia**, que indica cómo pueden usar los demás tu código.

!!! note "README, .gitignore y licencia"
    Dejar que GitHub los cree significa que el repositorio empieza ya con un
    commit dentro. Si en cambio construiste el repositorio en local (como en el
    [ejemplo de Git](../git/example.md)), deja estas casillas sin marcar y sube tu
    propio historial.

## Configurarlo

Conviene cambiar pronto algunos ajustes, desde la pestaña **Settings** del
repositorio y su página principal:

- **Descripción y temas (topics).** Una descripción de una línea y unas cuantas
  etiquetas de tema hacen el repositorio más fácil de encontrar y entender.
- **Colaboradores.** En **Settings → Collaborators**, invita a tus compañeros para
  que puedan hacer push a las ramas y revisar los pull requests.
- **Rama por defecto.** Confirma que se llama `main`.

La configuración que *impone* un flujo de trabajo de equipo saludable —proteger
`main`, exigir revisiones y comprobaciones que pasen— es lo bastante importante
como para tener su propia página: [Configuración del repositorio](repository-configuration.md).
Configúrala una vez que el flujo de trabajo y las Actions estén en su sitio.

## Explorar

La mayor parte de tu tiempo en GitHub la pasas leyendo repositorios *de otras
personas*. Todos los repositorios tienen las mismas pestañas, y conocerlas hace
legible cualquier proyecto:

| Pestaña | Qué encuentras ahí |
| --- | --- |
| **Code** | Los archivos, el README, el selector de ramas y el historial de commits. |
| **Issues** | Errores reportados, tareas y peticiones de funciones, abiertos y cerrados. |
| **Pull requests** | Cambios propuestos en revisión, y los ya fusionados. |
| **Actions** | Las ejecuciones automatizadas (pruebas, builds) y si pasaron. |
| **Insights** | La actividad de contribución, y una imagen de cómo se mueve el proyecto. |

Navegar por un proyecto bien llevado —leer cómo se describen sus pull requests y
cómo se discuten sus issues— es una de las mejores formas de aprender las
convenciones de la colaboración en software.

## Issues y pull requests

Estos dos son la columna vertebral de la colaboración en GitHub, y desempeñan
papeles distintos:

- Un **issue** describe *algo que hacer o arreglar*: un error, una tarea, una
  pregunta. Es una conversación, no código. Los issues están numerados (`#12`) y
  pueden etiquetarse y asignarse.
- Un **pull request** (PR) propone *un cambio real en el código*: "aquí hay una
  rama con commits, por favor revísala y fusiónala". También está numerado y se
  discute, pero lleva un diff.

Ambos se referencian mutuamente. Un pull request puede decir *"Closes #12"* en su
descripción, y cuando se fusiona, GitHub cierra automáticamente el issue #12 y
enlaza los dos. Esto es lo que ata el *plan* (issues) al *trabajo* (pull
requests) en un historial rastreable.

```mermaid
flowchart LR
    I["Issue: Add stop-word list"] -.-> PR["Pull request: Closes the issue"]
    PR -->|merged| M[main]
    PR -.->|auto-closes| I
```

El pull request en sí —cómo abrirlo, describirlo, revisarlo y fusionarlo— es el
tema de la página siguiente.

## Adónde ir después

- [Flujo de trabajo](workflow.md) — el ciclo completo rama → commit → pull request
  → merge.
