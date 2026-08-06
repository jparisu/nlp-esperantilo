# NLP Esperantilo

**NLP Esperantilo** is two things at once, and this site is split accordingly.

<div class="grid cards" markdown>

- :material-package-variant:{ .lg .middle } **[Library](library/index.md)**

    ---

    The reference manual of `esperantilo`, a rule-based NLP library for
    Esperanto: what it does today, and what every public name means. Its
    [API reference](library/api.md) is generated from the source.

- :material-book-open-page-variant:{ .lg .middle } **[Guide](guide/index.md)**

    ---

    How a library like it is built and shipped: Git, GitHub, Python packaging
    and testing, and the Esperanto linguistics that go inside.

</div>

## Which one do you want

| If you want to… | Go to |
| --- | --- |
| Call the library from your own code | [Library](library/index.md) |
| Know exactly what a function returns | [Library → API reference](library/api.md) |
| Learn Git, GitHub, packaging or testing | [Guide](guide/index.md) |
| Learn the Esperanto rules an NLP library encodes | [Guide → Esperanto](guide/esperanto/index.md) |

The two halves cross-link constantly: the guide teaches a technique, then points
at the place in the library where it is actually used.

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
    `esperantilo` is at version `0.1.0` and ships one feature:
    [sentence segmentation](library/sentence-segmentation.md). Tokens, lemmas
    and affix analysis are still a
    [design target](guide/python-library/api.md), not shipped code. Building the
    rest is the exercise this site prepares you for.

## Who this is for

University students who have to build their own Esperanto NLP library. Readers
are expected to have a technical background, but not necessarily experience with
the specific tools and topics explained here.

Two topics are deliberately left out of the guide, because they are taught in
the course lectures: **web scraping and API consumption**, and **text-mining and
Machine-Learning classification**. See
[Guide → what it does not cover](guide/index.md#what-this-guide-does-not-cover).

## Building this site locally

```bash
pip install -r docs/requirements.txt
mkdocs serve
```

The site is then available at <http://127.0.0.1:8000>. Every push to `main`
rebuilds it and publishes it to GitHub Pages.
