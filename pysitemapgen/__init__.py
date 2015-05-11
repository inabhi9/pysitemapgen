__all__ = ['SitemapIndex', 'Sitemap']

import os
import xml.etree.ElementTree as ET
from datetime import datetime

from lxml import etree


class BaseSiteMap(object):
    _init_content = ''

    CHANGEFREQ_ALWAYS = 'always'
    CHANGEFREQ_HOURLY = 'hourly'
    CHANGEFREQ_DAILY = 'daily'
    CHANGEFREQ_WEEKLY = 'weekly'
    CHANGEFREQ_MONTHLY = 'monthly'
    CHANGEFREQ_YEARLY = 'yearly'
    CHANGEFREQ_NEVER = 'never'

    def __init__(self, filename, timezone='Z'):
        self.filename = filename
        self.timezone = timezone

        if not os.path.exists(filename):
            self._init_file()
        self._read_file()

    def _init_file(self):
        with open(self.filename, 'w') as f:
            f.write(self._init_content)

    def _read_file(self):
        self.tree = etree.parse(self.filename)
        self.root = self.tree.getroot()

    def save(self):
        self.tree.write(self.filename, encoding='utf-8', xml_declaration=True)

    def _format_iso8601(self, obj):
        updated = '%Y-%m-%dT%H:%M' + self.timezone
        return obj.strftime(updated)


class SitemapIndex(BaseSiteMap):
    _init_content = '''<sitemapindex xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></sitemapindex>'''

    def add(self, index_url):
        sitemap = ET.SubElement(self.root, 'sitemap')
        loc = ET.SubElement(sitemap, 'loc')
        loc.text = index_url
        self.root.append(sitemap)


class Sitemap(BaseSiteMap):
    _init_content = '''<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:n="http://www.google.com/schemas/sitemap-news/0.9"
    xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
    http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"></urlset>'''

    def add(self, url, lastmod=None, changefreq=None, priority=None, **kwargs):
        sitemap = ET.SubElement(self.root, 'url')
        loc = ET.SubElement(sitemap, 'loc')
        loc.text = url

        if lastmod and isinstance(lastmod, datetime):
            lm = ET.SubElement(sitemap, 'lastmod')
            lm.text = self._format_iso8601(lastmod)
        if changefreq:
            cf = ET.SubElement(sitemap, 'changefreq')
            cf.text = changefreq
        if priority:
            p = ET.SubElement(sitemap, 'priority')
            p.text = priority

        self.root.append(sitemap)
