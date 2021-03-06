# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# -- Project information -----------------------------------------------------

project = 'osscar-docs'
copyright = '2020, Dou Du'
author = 'Dou Du'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# Ensure our extension is available:
import sys
import os
from os.path import dirname, join as pjoin
docs = dirname(dirname(__file__))
root = dirname(docs)
sys.path.insert(0, root)
sys.path.insert(0, pjoin(docs, 'sphinxext'))
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'nbsphinx',
    'jupyter_sphinx.execute',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

todo_include_todos = False 

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
intersphinx_mapping = {'https://docs.python.org/': None}
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Uncomment this line if you have know exceptions in your included notebooks
# that nbsphinx complains about:

# Set the nbsphinx_widgets_path empty can aovid show twice of the widgets 
nbsphinx_widgets_path = ""

here = os.path.dirname(__file__)

def setup(app):
    app.setup_extension('jupyter_sphinx.execute')
    def add_scripts(app):
        for fname in ['helper.js', 'embed-periodictable.js']:
            if not os.path.exists(os.path.join(here, '_static', fname)):
                app.warn('missing javascript file: %s' % fname)
            app.add_js_file(fname)
    app.connect('builder-inited', add_scripts)
    app.add_css_file('style.css')
