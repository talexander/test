# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    underground = scrapy.Field()
    street = scrapy.Field()
    rent = scrapy.Field()
    fee = scrapy.Field()
    descr = scrapy.Field()
