#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#####
# DISABLE THIS
# LOAD_CONTENT_CACHE = False
########

AUTHOR = 'Bryan W. Weber'
SITENAME = 'Bryan W. Weber'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'writing/{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'writing/{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Blogroll
LINKS = ()
DISPLAY_PAGES_ON_MENU = True

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/bryanwweber'),
    ('ORCID', 'https://orcid.org/0000-0003-0815-9270'),
    ('Google Scholar', 'https://scholar.google.com/citations?user=48LLBNMAAAAJ&hl=en'),
    ('LinkedIn', 'https://www.linkedin.com/in/bryanwweber'),
    ('Mendeley', 'https://www.mendeley.com/profiles/bryan-w-weber/'),
    ('Academia.edu', 'https://uconn.academia.edu/BryanWWeber'),
    ('Zotero', 'https://www.zotero.org/darthbith'),
    ('arXiv', 'https://arxiv.org/a/weber_b_1.html'),
)

# Static Files
STATIC_PATHS = [
    'images',
    'extra',
    'files',
]

GITHUB_URL = 'https://github.com/bryanwweber/bryanwweber.com'

EXTRA_PATH_METADATA = {
    'extra/extra.css': {'path': 'css/extra.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/htaccess': {'path': '.htaccess'},
    'extra/keybase.txt': {'path': 'keybase.txt'},
    # 'extra/css/academicons.css': {'path': 'extra/css/academicons.css'},
    'extra/css/academicons.min.css': {'path': 'extra/css/academicons.min.css'},
}

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = './bulrush'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets', 'summary', 'md_inline_extension']
JINJA_ENVIRONMENT = {
    'extensions': ['webassets.ext.jinja2.AssetsExtension', 'jinja2.ext.with_'],
}
SUMMARY_END_MARKER = '<!--more-->'
SUMMARY_USE_FIRST_PARAGRAPH = True

MD_INLINE = {
    '|-|': 'cv-position',
    '|+|': 'cv-duty',
    '|=|': 'cv-location',
    '|a|': 'cv-award',
    '|p|': 'papertitle',
    '|u|': 'paperauthors',
    '|j|': 'paperjournal',
    '|d|': 'paperdoi',
    '|c|': 'papercomment',
    '|a|': 'paperarxiv',
}

TYPOGRIFY = True
