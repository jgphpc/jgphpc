# Configuration file for the Sphinx documentation builder (sphinx-quickstart)
# http://www.sphinx-doc.org/en/master/config
import os
import re
import sys
import sphinx_rtd_theme
source_suffix = '.rst'
master_doc = 'index'
# -- Project information -----------------------------------------------------
project = 'HPCTOOLS'
copyright = '2020, Swiss National Supercomputing Center (CSCS), All rights reserved.'
author = 'jg'
# -- General configuration ---------------------------------------------------
extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
    'navigation_depth': 5,
}
# html_static_path = ['_static']
