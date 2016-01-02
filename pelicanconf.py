#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lei Gong'
SITENAME = 'LeiG'
SITEURL = 'http://LeiG.github.io'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/imleigong'),
          ('github', 'https://github.com/LeiG'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Basic settings
DEFAULT_DATE = 'fs'
OUTPUT_PATH = 'output/'
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']
SUMMARY_MAX_LENGTH = 50

EMAIL = 'LeiG.inbox@gmail.com'

# Themes
THEME = 'pelican-themes/bootstrap2'
DISQUS_SITENAME = 'lei-gong'
TWITTER_USERNAME = '__LeiG__'
