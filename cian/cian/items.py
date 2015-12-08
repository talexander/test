# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CianItem(scrapy.Item):
    rent = scrapy.Field(serializer=str)
    fee = scrapy.Field(serializer=str)
    underground = scrapy.Field()
    street = scrapy.Field()
    link = scrapy.Field(serializer=str)
    descr = scrapy.Field()
