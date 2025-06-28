# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Panda3D Internal Docs'
copyright = '2025, shivam'
author = 'shivam'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'sphinx.ext.intersphinx',
        'breathe',
        'exhale'
]

# -- Breathe and Exhale configuration ----------------------------------------

# Tell breathe where to find the doxygen output
breathe_projects = {
    "Panda3D": "doxygen_output/xml"
}

# Tell breathe what is the default project
breathe_default_project = "Panda3D"

# Setup the exhale configuration
exhale_args = {
    "containmentFolder": "./api",  # <-- correct key
    "rootFileName": "library_root.rst",
    "rootFileTitle": "C++ API Reference",
    "doxygenStripFromPath": "../",
    "createTreeView": True,
    "exhaleExecutesDoxygen": False,
    "exhaleDoxygenStdin": "INPUT = ../panda/src ../dtool/src ../pandatool/src\nFILE_PATTERNS = *.cxx *.h *.cpp *.hpp\nRECURSIVE = YES"
}

# Tell Sphinx to do a mock build for exhale
autodoc_mock_imports = ["dtool_config"] # You might need to add other modules here

# Primary Sphinx page for exhale to use as a landing page
# This is usually your main index.rst file
# The path is relative to your Sphinx source directory
exhale_toctreedef_file = "index.rst"

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
