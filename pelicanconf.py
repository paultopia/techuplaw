#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Paul Gowder'
SITENAME = 'Tech and Math For Lawyers'
SITEURL = ''

MARKUP = ('md')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['render_math', 'pelican_javascript', 'simple_footnotes']
PATH = 'content'
MATH_JAX={"mathjax_font": "typewriter", 'color':'blue'}
THEME='blue-penguin'
USE_FOLDER_AS_CATEGORY = True
TIMEZONE = 'America/Chicago'
SUMMARY_MAX_LENGTH = 100
TYPOGRIFY = True

DELETE_OUTPUT_DIRECTORY = True

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
)
# additional menu items
MENUITEMS = (
    ('Repository', 'https://github.com/paultopia/techuplaw'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
