#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime
import pathlib
import re

from markdown_include.include import MarkdownInclude

# The Pelican settings are documented here:
#   https://docs.getpelican.com/en/stable/settings.html
# and the Flex theme's settings are documented here:
#   https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings

# Pelican general site settings
# Depending on the scope of changes, you may want to change "westlanetv.org"
# in the SITEURL to wherever the staging site is so links point within the
# staging site.
SITEURL = 'https:///idlecreativity.pages.dev'
SITENAME = 'IdleCreativity'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# The Flex theme can accommodate our non-blog site well and is MIT license
THEME = 'Flex'

# Flex general site settings
SITETITLE = SITENAME
SITESUBTITLE = 'Fused Glass Art'
SITEDESCRIPTION = \
    "Fused Glass Art by Kristin Anderson"
AUTHOR = 'Kristin Anderon'
COPYRIGHT_NAME = AUTHOR
FIRST_YEAR = '2024'
CURRENT_YEAR = str(datetime.datetime.today().year)
if CURRENT_YEAR == FIRST_YEAR:
    COPYRIGHT_YEAR = CURRENT_YEAR
else:
    COPYRIGHT_YEAR = f'{FIRST_YEAR}-{CURRENT_YEAR}'
ROBOTS = 'index, follow'
FAVICON = SITEURL + '/images/favicon.ico'
SITELOGO = SITEURL + '/images/logo.jpg'

# Enable some Markdown extensions.  The list of available extensions and
# documentation for them is available here:
#   https://python-markdown.github.io/extensions/
# For completeness, the basic Markdown syntax is documented here:
#   https://daringfireball.net/projects/markdown/syntax
MARKDOWN = {
    'extensions': {
        'markdown.extensions.extra',
        'markdown.extensions.meta',
        'markdown.extensions.smarty',
        'markdown.extensions.toc',
        MarkdownInclude({'base_path': 'content'})
    },
    'output_format': 'html5'
}

# I don't feel compelled to tell the world our site was built with
# Pelican and Flex.  This relies on local changes to Flex.
ALT_CREDIT=''

# By default, the links point to the main page heading so that the top
# menu isn't seen unless you scroll or if the page happens to be
# smaller than your browser window.  Disable that.
DISABLE_URL_HASH = True

# Output our canonical URL.
REL_CANONICAL = True

# Tell the world via the JSON-LD and Open Graph types that we are a
# website and not a blog.  These rely on local changes to Flex.
OG_TYPE = 'website'
JSONLD_TYPE = 'WebPage'

# This is a simple website and not a blog so disable all the bloggy stuff
DIRECT_TEMPLATES = []
ARCHIVES_SAVE_AS = ''
ARTICLE_PATHS = []
ARTICLE_SAVE_AS = ''
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = ''
CATEGORY_FEED_ATOM = None
CATEGORY_SAVE_AS = ''
DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False
DRAFT_SAVE_AS = ''
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ''
TAG_SAVE_AS = ''
TRANSLATION_FEED_ATOM = None
# We don't have SOCIAL nor articles so turn on this local change to
# prevent links to font-awesome being emitted.
FONT_AWESOME_UNNEEDED = True

# The site is small, so rebuild it from scratch every time.
DELETE_OUTPUT_DIRECTORY = False
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# Tell Pelican where things come from and go to.
PATH = 'content'  # Keep content separate from how to build.
PAGE_PATHS = ['pages']  # Where to look in content subdirectory for our pages.
STATIC_PATHS = ['images']  # Copy things from these to output.
OUTPUT_PATH = 'output/'  # Where to put the output.
PAGE_URL = '{slug}.html'  # Output the HTML at the root instead of in pages/
PAGE_SAVE_AS = '{slug}.html'

# The configuration of the menus is custom and somewhat hacky.

# Pages can be placed in one of three different menus of links:
#   1) at the top of the page,
#   2) on the left side of the page, or
#   3) at the bottom of the page by the copyright (via a local change).

# The items in the menu at the bottom of the page are defined via
# FOOTERMENUITEMS (a local change).  Defining it also enables it.
# FOOTERMENUITEMS will also be set via the Python code that follows.

# Each page Markdown file has our own locally defined 'Menu' metadata.
# It is used for two purposes.  The first is to construct the
# MENUITEMS and FOOTERMENUITEMS lists.  The second is to define the
# order of the pages within each menu:
PAGES_SORT_ATTRIBUTE = 'menu'

# We'll use the default SLUG_REGEX_SUBSTITUTIONS for generating the slug.
SLUG_REGEX_SUBSTITUTIONS = [
    (r'[^\w\s-]', ''), # remove non-alphabetical/whitespace/'-' chars
    (r'(?u)\A\s*', ''), # strip leading whitespace
    (r'(?u)\s*\Z', ''), # strip trailing whitespace
    (r'[-\s]+', '-'), # reduce multiple whitespace or '-' to single '-'
]

# Build up a list of the Markdown pages.  Each element of the list is
# a tuple containing:
#   1) the value of the 'Menu' metadata,
#   2) the value of the 'Title' metadata, and
#   3) the URL of the page (which makes assumptions about slugification)
path_path = pathlib.Path(PATH)
pages_path = path_path / 'pages'
pages_menu_info = []
for md in pages_path.glob('**/*.md'):
    title = ''
    menu = ''
    with md.open() as f:
        while True:
            line = f.readline()
            if not line or ':' not in line:
                break
            if line.lower().startswith('title:'):
                title = line[6:].strip()
            if line.lower().startswith('menu:'):
                menu = line[5:].strip()
    assert title
    if menu:
        slug = title
        for pattern, repl in SLUG_REGEX_SUBSTITUTIONS:
            slug = re.sub(pattern, repl, slug)
        slug = slug.lower()
        page_url = f'{SITEURL}/{slug}.html'
        pages_menu_info.append((menu, title, page_url))

# Now iterate through the list of Markdown pages to form FOOTERMENUITEMS:
FOOTERMENUITEMS = []
for menu, title, page_url in sorted(pages_menu_info):
    if menu.lower().startswith('bottom'):
        FOOTERMENUITEMS.append((title, page_url))
# Done!

