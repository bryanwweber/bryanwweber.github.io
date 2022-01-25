import bulrush

#####
# DISABLE THIS
# LOAD_CONTENT_CACHE = False
########

AUTHOR = "Bryan Weber"
SITENAME = "Bryan Weber"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_URL = "writing/{slug}.html"
ARTICLE_SAVE_AS = "writing/{slug}.html"
DIRECT_TEMPLATES = ["index"]
AUTHOR_SAVE_AS = ""
INDEX_SAVE_AS = "writing.html"
DEFAULT_CATEGORY = "writing"
USE_FOLDER_AS_CATEGORY = True
SLUGIFY_SOURCE = "basename"

# Blogroll
LINKS = ()
DISPLAY_PAGES_ON_MENU = True

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/bryanwweber"),
    # ("ORCID", "https://orcid.org/0000-0003-0815-9270"),
    # ("Google Scholar", "https://scholar.google.com/citations?user=48LLBNMAAAAJ&hl=en"),
    ("LinkedIn", "https://www.linkedin.com/in/bryanwweber"),
    # ('Mendeley', 'https://www.mendeley.com/profiles/bryan-w-weber/'),
    # ('Academia.edu', 'https://uconn.academia.edu/BryanWWeber'),
    # ("Zotero", "https://www.zotero.org/darthbith"),
    # ("arXiv", "https://arxiv.org/a/weber_b_1.html"),
)

# Static Files
STATIC_PATHS = [
    "extra",
    "files",
]

GITHUB_URL = "https://github.com/bryanwweber/bryanwweber.github.io"

EXTRA_PATH_METADATA = {
    "extra/extra.css": {"path": "css/extra.css"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/keybase.txt": {"path": "keybase.txt"},
    "extra/CNAME": {"path": "CNAME"},
    # "extra/css/academicons.css": {"path": "extra/css/academicons.css"},
    "extra/css/academicons.min.css": {"path": "extra/css/academicons.min.css"},
}

DEFAULT_PAGINATION = 6

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS
BULRUSH_SHOW_SUMMARY = True
THEME_TEMPLATES_OVERRIDES = ["template_overrides"]
LICENSE = "CC BY-SA 3.0"

SUMMARY_END_MARKER = "<!--more-->"
SUMMARY_USE_FIRST_PARAGRAPH = True

MARKDOWN = {
    "tab_length": 2,
    "extensions": [
        "pymdownx.superfences",
        "pymdownx.inlinehilite",
        "pymdownx.tilde",
        "pymdownx.caret",
        "pymdownx.keys",
        "attr_list",
        "tables",
    ],
}

TYPOGRIFY = True
