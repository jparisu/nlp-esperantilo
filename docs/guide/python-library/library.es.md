# Qué es una biblioteca

Una **biblioteca** es un fragmento de código escrito para ser *reutilizado* por
otro código. En lugar de copiar funciones entre proyectos, las empaquetas una vez,
les das una interfaz pública clara, y dejas que cualquier proyecto las instale e
importe. `esperantilo` —la biblioteca que construye esta guía— es una: un conjunto
de herramientas de NLP basado en reglas para el Esperanto que un notebook puede
instalar y usar en un par de líneas.

Esta página ordena el vocabulario, explica qué te aporta una biblioteca y observa
un ejemplo conocido a imitar.

## Módulo, paquete, biblioteca, distribución

Estas cuatro palabras se usan a menudo de forma imprecisa. En Python significan
cosas concretas:

| Término | Qué es |
| --- | --- |
| **Módulo** | Un único archivo `.py`. Importarlo lo ejecuta una vez y expone sus nombres. |
| **Paquete** | Una *carpeta* de módulos importada como una unidad, normalmente marcada por un `__init__.py`. |
| **Biblioteca** | Un paquete (o conjunto de paquetes) pensado para ser reutilizado por otro código. |
| **Distribución** | El artefacto empaquetado que instalas — lo que `pip install` descarga. |

La progresión es de escala: un **módulo** es un archivo, un **paquete** agrupa
módulos en una carpeta, una **biblioteca** es un paquete diseñado para
reutilizarse, y una **distribución** es esa biblioteca empaquetada para poder
instalarse en otro sitio.

```mermaid
flowchart LR
    M["Módulo<br/>(tokenizer.py)"] --> P["Paquete<br/>(esperantilo/)"]
    P --> L["Biblioteca<br/>(API reutilizable)"]
    L --> D["Distribución<br/>(pip install esperantilo)"]
```

En este proyecto, `src/esperantilo/` es el **paquete**, la API que expone lo
convierte en una **biblioteca**, y `pyproject.toml` es lo que lo convierte en una
**distribución** instalable (véase [Organización](organization.md)).

## Qué te aporta una biblioteca

¿Por qué empaquetar código en lugar de tener por ahí un simple `utils.py`? Una
biblioteca te da cuatro cosas:

- **Reutilización.** Escribe el tokenizador de Esperanto una vez; impórtalo desde
  cada notebook, script y prueba sin copiar y pegar.
- **Una interfaz estable.** Los usuarios dependen de la API *pública*, no de los
  detalles internos. Puedes reescribir el interior libremente mientras la interfaz
  se mantenga (de eso trata [la página de la API](api.md)).
- **Versionado.** Las versiones se numeran (`0.1.0`, `0.2.0`, …), de modo que los
  usuarios pueden decir "necesito la versión 0.1" y obtener un comportamiento
  reproducible.
- **Distribución.** Un solo comando `pip install` entrega el código y sus
  dependencias a cualquiera, en cualquier lugar — incluido un notebook de Google
  Colab.

## Un ejemplo concreto

La forma más clara de ver qué significa "una buena biblioteca" es usar una.
**scikit-learn** es una biblioteca de machine learning muy usada y un modelo de
diseño agradable. La instalas una vez:

```bash
pip install scikit-learn
```

importas una pieza pequeña y bien nombrada:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)      # entrenar
predictions = model.predict(X_test)  # usar
```

y eres productivo de inmediato — sin leer su código fuente. De eso se trata una
biblioteca. Vale la pena nombrar qué hace que funcione, porque son exactamente las
cualidades a las que aspirar en `esperantilo`:

- **Una interfaz consistente.** Casi todos los estimadores de scikit-learn tienen
  los mismos métodos `.fit()` / `.predict()`, así que en cuanto aprendes uno,
  puedes adivinar los demás.
- **Valores por defecto sensatos.** `LogisticRegression()` funciona sin
  argumentos; solo tocas los parámetros cuando lo necesitas.
- **Nombres y documentación claros.** `fit`, `predict`, `LogisticRegression` dicen
  lo que hacen, y cada objeto público tiene documentación.

La biblioteca de NLP **spaCy** —la referencia de diseño para la propia API de este
proyecto— tiene las mismas cualidades, aplicadas al texto. Volvemos a ella en
detalle en [la página de la API](api.md).

## Adónde ir después

- [Organización](organization.md) — los archivos y carpetas que convierten este
  código en una biblioteca instalable.
- [Instalación y uso](installation-and-usage.md) — instalar `esperantilo` desde
  GitHub y usarlo en un notebook.
