# Installation and usage

!!! note "Under construction"
    Planned contents are listed below.

Most of the work happens in notebooks (Google Colab), so installing straight
from GitHub is the main path.

## Install from GitHub

```bash
pip install git+https://github.com/jparisu/nlp-esperantilo.git
```

Installing a specific branch, and why this is convenient while the library is
still moving.

## Use it in a notebook

```python
import esperantilo

print(esperantilo.__version__)
```

## Install locally

Briefly: a virtual environment plus an editable install for development.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
```
