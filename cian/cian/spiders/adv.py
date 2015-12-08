# -*- coding: utf-8 -*-
import scrapy
from cian.items import CianItem


class AdvSpider(scrapy.Spider):
    name = "adv"
    allowed_domains = ["cian.ru"]

    start_urls = (
    	'http://www.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&foot_min=25&maxprice=35000&metro%5B0%5D=9&metro%5B1%5D=36&metro%5B2%5D=116&minfloor=2&minprice=27000&offer_type=flat&only_foot=2&room1=1&type=-2&wp=1',
    )

    def parse(self, response):
	for elem in response.selector.css('.serp-list .serp-item'):
		item = CianItem()
		item['rent'] = elem.css('.serp-item__price-col .serp-item__solid::text').extract_first().encode('utf-8')
		item['fee'] = elem.css('.serp-item__price-col .serp-item__prop').extract()
		item['underground'] = elem.css('.serp-item__metro a').extract()
		item['street'] = elem.css('.serp-item__address-precise a').extract()
		item['link'] = elem.css('.serp-item__card-link::attr(href)').extract()
		item['descr'] = elem.css('.serp-item__description__text').extract()
		yield item

