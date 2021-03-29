#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Oriana and Amanda'
SITENAME = "Let's Chat Ethics"
SITEURL = ''

PATH = 'content'
THEME = '/Users/amandacurry/pelican-themes/pelican-fh5co-marble'
TIMEZONE = 'Europe/London'

STATIC_PATHS = [
    'images',
    'extra',  # this
]

PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

LOGO = '/images/logo.png'
FAVICON = '/images/logo.png'
DEFAULT_LANG = 'en'

ABOUT = {
  'image': '/images/orianda.png',
  'mail': 'letschatethics@gmail.com',
  # keep it a string if you dont need multiple languages
  'text': {
    'en': 'We always look forward to hearing from our listeners. Got something to discuss?',
  },
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'London, United Kingdom',
}

# content paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']

I18N_GETTEXT_LOCALEDIR = '../pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_UK'
DEFAULT_LANG = 'en'
LOCALE = 'en_UK'
# i18n


# navigation and homepage options
DISPLAY_PAGES_ON_MENU = False
DISPLAY_PAGES_ON_HOME = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
#PAGE_ORDER_BY = 'order'

MENUITEMS = [
  #('Home', 'index.html'),
  ('About', 'pages/about.html'),
  ('Podcast', 'podcast.html'),
  ('Recommended Books', 'pages/recommended-books.html'),
  ('Support the podcast', 'pages/support-the-podcast.html'),
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'podcast',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/LetsChatEthics'),
          ('Instagram', 'https://www.instagram.com/lets.chat.ethics/'),
          ('LinkedIn', 'https://www.linkedin.com/company/letschatethics/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True