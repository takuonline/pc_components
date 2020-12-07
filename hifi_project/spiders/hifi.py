# -*- coding: utf-8 -*-
import scrapy
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



class HifiSpider(scrapy.Spider):
    name = 'hifi'
    # allowed_domains = ['https://www.hificorp.co.za']

    custom_settings = {
        'ITEM_PIPELINES' : {
                            'hifi_project.pipelines.HifiProjectPipeline': 400,
                            }

        # "FEED_URI": "file:///users/hifi.csv",
    }

    def start_requests(self):
        url = 'https://www.hificorp.co.za/products/computing/computing'
        yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):

        # image url
        # .//ol[@class='products list items product-items']/li/div/a/span/span/img/@src

        # title
        # .//ol[@class='products list items product-items']/li/div/strong/a/text()

        # price
        # .//ol[@class='products list items product-items']/li/div/div[2]/div[2]/div/span/span/span/text()

        # rating
        # .//div[@class='review-mask']/@style
                            # style="width: 0" means no rating        #example 
                            # style="width: 90" means a rating of 90% 

        # number of people who gave a rating
        # //div[@class='product-item-rating']/div/span/text()


        # pagination
        # //a[@class='action  next']/@href
    
        for item in  response.xpath("//ol[@class='products list items product-items']/li"):

            title = item.xpath(".//div/strong/a/text()").extract_first()
            price = item.xpath(".//div/div[2]/div[2]/div/span/span/span/text()").extract_first()
            image_url = item.xpath(".//img[@class='product-image-photo lazyload']/@data-src").extract_first()
            date = str(datetime.datetime.now())

            data={
                "title": title,
                "image_url":image_url,
                "price": price,
                "date": date
                # "rating":response.xpath(".//div[@class='review-mask']/@style").extract_first(),
                # "number_of_ratings":response.xpath(".//div[@class='product-item-rating']/div/span/text()").extract_first(),
            }

        
            yield data

        next_page = response.xpath(".//a[@class='action  next']/@href").extract_first()

        if (next_page is not None):
            # print(f"\t\t {next_page}")
            yield scrapy.Request(url=next_page, callback = self.parse)




