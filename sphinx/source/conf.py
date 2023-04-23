# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Blog"
copyright = "2023, AnonymousDapper"
author = "AnonymousDapper"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

# templates_path = ['../../templates']
exclude_patterns = ["output", "source"]

primary_domain = None
numfig = True
highlight_language = "text"
# pygments_style = "paraiso-dark"
# pygments_dark_style = "stata-dark"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "theme"
html_theme_path = [".."]
