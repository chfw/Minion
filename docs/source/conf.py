# -*- coding: utf-8 -*-
DESCRIPTION = (
    'Make your machine as a deligent minion' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Minion'
copyright = u'2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.1'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'Miniondoc'
latex_elements = {}
latex_documents = [
    ('index', 'Minion.tex',
     'Minion Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'Minion',
     'Minion Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'Minion',
     'Minion Documentation',
     'Onni Software Ltd.', 'Minion',
     DESCRIPTION,
     'Miscellaneous'),
]
