import os
import sys

sys.path.insert(0, os.path.abspath("../../.."))

import triangle

project = "triangle"
author = "Dimitar Dimitrov"
copyright = f"2022, {author}"

version = triangle.__version__
release = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.coverage",
    "sphinx_copybutton",
]

autosummary_generate = True
language = "en"
html_theme = "furo"
todo_include_todos = True

exclude_patterns = []
templates_path = [".templates"]
html_static_path = [".static"]
