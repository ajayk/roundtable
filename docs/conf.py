import os
import sys

from documenteer.sphinxconfig.utils import form_ltd_edition_name
import lsst_sphinx_bootstrap_theme


# Work around Sphinx bug related to large and highly-nested source files
sys.setrecursionlimit(2000)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'documenteer.sphinxext'
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Roundtable'
copyright = '2019 Association of Universities for Research in Astronomy'
author = 'LSST SQuaRE'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
if os.getenv('TRAVIS_BRANCH', default='master') == 'master':
    # Use the current release as the version tag if on master
    version = 'Current'
    release = version
else:
    # Use branch name as the version tag
    version = form_ltd_edition_name(
        git_ref_name=os.getenv('TRAVIS_BRANCH', default='master'))
    release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    'README.rst'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The reST default role cross-links Python (used for this markup: `text`)
default_role = 'py:obj'

# Intersphinx

intersphinx_mapping = {
    # 'python': ('https://docs.python.org/3/', None),
}

rst_epilog = """

.. |roundtable-status| image:: https://cd.roundtable.lsst.codes/api/badge?name=roundtable
   :target: https://cd.roundtable.lsst.codes/applications/roundtable
   :alt: Roundtable app status

.. |argo-cd-status| image:: https://cd.roundtable.lsst.codes/api/badge?name=argo-cd
   :target: https://cd.roundtable.lsst.codes/applications/argo-cd
   :alt: Argo CD app status

.. |nginx-ingress-status| image:: https://cd.roundtable.lsst.codes/api/badge?name=nginx-ingress
   :target: https://cd.roundtable.lsst.codes/applications/nginx-ingress
   :alt: nginx-ingress app status

.. |cert-manager-status| image:: https://cd.roundtable.lsst.codes/api/badge?name=cert-manager
   :target: https://cd.roundtable.lsst.codes/applications/cert-manager
   :alt: cert-manager app status

.. |prometheus-status| image:: https://cd.roundtable.lsst.codes/api/badge?name=prometheus
   :target: https://cd.roundtable.lsst.codes/applications/prometheus
   :alt: Prometheus app status

.. _Helm: https://helm.sh
.. _Kustomize: https://kustomize.io
.. _Argo CD: https://argoproj.github.io/argo-cd/
.. _Prometheus: https://prometheus.io
.. _Grafana: https://grafana.com/grafana
.. _lsst-sqre GitHub organization: https://github.com/lsst-sqre
.. _roundtable-ops team: https://github.com/orgs/lsst-sqre/teams/roundtable-ops
.. _httpie: https://httpie.org
"""

# -- Options for linkcheck builder ----------------------------------------

linkcheck_retries = 2
linkcheck_timeout = 5  # seconds
linkcheck_ignore = [
    r'^https://console.cloud.google.com',
    r'^https://cd.roundtable.lsst.codes',
    r'^https://monitoring.roundtable.lsst.codes',
    r'^https://github.com/organizations/lsst-sqre/settings/'
]

# -- Options for HTML output ----------------------------------------------

templates_path = [
    '_templates',
    lsst_sphinx_bootstrap_theme.get_html_templates_path()
]

html_theme = 'lsst_sphinx_bootstrap_theme'
html_theme_path = [lsst_sphinx_bootstrap_theme.get_html_theme_path()]


html_context = {
    # Enable "Edit in GitHub" link
    'display_github': True,
    # https://{{ github_host|default("github.com") }}/{{ github_user }}/
    #     {{ github_repo }}/blob/
    #     {{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    'github_user': 'lsst-sqre',
    'github_repo': 'roundtable',
    'conf_py_path': 'docs/',
    # TRAVIS_BRANCH is available in CI, but master is a safe default
    'github_version': os.getenv('TRAVIS_BRANCH', default='master') + '/'
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'logotext': project}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = project

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
