AUTHOR = 'Aldon P Smith'
SITENAME = 'Imperial Tech'
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

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/smithaldon1'),
    ('twitter', 'https://twitter.com/AldonSmith7'),
    ('linkedin', 'https://www.linkedin.com/in/aldon-smith/')
)

DEFAULT_PAGINATION = 10

THEME = "bootstrap2"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

STATIC_PATHS = ['images',]
