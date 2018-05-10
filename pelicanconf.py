#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')

AUTHOR = ''
SITENAME = 'hella labs'
TAGLINE = 'On the one hand information wants to be expensive, because it\'s so valuable. The right information in the right place just changes your life. On the other hand, information wants to be free, because the cost of getting it out is getting lower and lower all the time. So you have these two fighting against each other. -Stewart Brand of Whole Earth Catalog to Steve Wozniak (1984)'
SITEURL = ''
# CONTACT_URL = '/pages/about.html'

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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = [
    'blob'
]

DEFAULT_DATE = 'fs'

DIRECT_TEMPLATES = ['index', 'categories', 'archives']

THEME = '../pelican-themes-frankv-twenty-pelican-html5up'
THEME_STATIC_DIR = '.'
THEME_STATIC_PATHS = ['static']


PLUGIN_PATHS = ["plugins", "../pelican-plugins"]
PLUGINS = ['neighbors']

import jinja_filter_sidebar
JINJA_FILTERS = { 'sidebar': jinja_filter_sidebar.sidebar }

DISPLAY_PAGES_ON_MENU = True
