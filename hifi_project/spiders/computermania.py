# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class ComputermaniaSpider(CrawlSpider):
    name = 'computermania'
    start_urls = ['https://www.computermania.co.za/home/accessories.html/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'hifi_project.pipelines.ComputermaniaProjectPipeline': 400,
        },
        # "FEED_URI": "file:///users/computermania.csv",
    }

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='col-md-3 col-sm-4 col-lg-2 category-list-item']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='bottom-pagination']/div/div[2]/ul/li[position()=last()]/a"), callback='parse_item', follow=True),
       
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        # img
        # .//div[@class='product-item-info']/div/div/div/div/a/img/@src

        # title
        # //div[@class='product-item-info']/div[2]/div[2]/h5/a/text()

        # price
        # //div[@class='product-inner']/div[2]/div[2]/span/span/span/text()

        # is_limited_stock
        # //div[@class="low-stock"]/text()

        
        for item in response.xpath("//div[@class='product-item-info']"):

            yield{
                "title": item.xpath(".//div[2]/div[2]/h5/a/text()").extract_first(),
                "price": item.xpath(".//div[@class='product-inner']/div[2]/div[2]/span/span/span/text()").extract_first(),
                "image": item.xpath(".//div/div/div/div/a/img/@src").extract_first(),
                "is_limited": item.xpath(".//div[@class='low-stock']/text()").extract_first(),
                "date": str(datetime.now()),
            }



        
