# NLP Esperantilo

**NLP Esperantilo** is an educational project that helps you build a Natural Language Processing (NLP) library for Esperanto.
The project has 2 parts:

<div class="grid cards" markdown>

- :material-package-variant:{ .lg .middle } **[Library](library/index.md)**

    ---

    The reference manual of `esperantilo`, a rule-based NLP library for
    Esperanto: what it does today, and what every public name means. Its
    [API reference](library/api.md) is generated from the source.

- :material-book-open-page-variant:{ .lg .middle } **[Guide](guide/index.md)**

    ---

    How a library like it is built and shipped: Git, GitHub, packaging and
    Esperanto linguistics.

</div>

## Try it

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

```python
import esperantilo

esperantilo.sentence_tokenizer("Zamenhof kreis Esperanton. Ĉu vere? Jes!")
# ['Zamenhof kreis Esperanton.', 'Ĉu vere?', 'Jes!']
```

!!! warning "The library is deliberately small"
    `esperantilo` is an educational project; it does not try to be a complete,
    production-ready library.

## Building this site locally

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

The site is then available at <http://127.0.0.1:8000>. Every push to `main`
rebuilds it and publishes it to GitHub Pages.
