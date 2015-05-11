PySitemapGen
===========
This library is intended to create/update site map with few simple method

## Installation

    python setup.py install
    
the pip way

    pip install pysitemapgen
    


## How to use

To create a sitemap index

    from pysitemapgen import SitemapIndex
    
    sitemapindex = SitemapIndex('sitemap.xml')
    sitemapindex.add('http://example.com/sitemap-0.xml')
    sitemapindex.save()

To create a sitemap

    from pysitemapgen import Sitemap
        
        sitemap = SitemapIndex('sitemap-0.xml')
        sitemap.add('http://example.com/page/1')
        sitemap.save()


## To Do:

* Test case
