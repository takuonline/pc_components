# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class TakealotSpider(scrapy.Spider):
    name = 'takealot'

    custom_settings = {
        'ITEM_PIPELINES': {
            'hifi_project.pipelines.TakealotProjectPipeline': 400,
        },

        # "FEED_URI": "file:///users/takealot.csv",
    }


    url = "https://api.takealot.com/rest/v-1-9-1/searches/products,filters,facets,sort_options,breadcrumbs,slots_audience,context,seo?department_slug=computers&category_slug=components-26415&sort=Relevance"

    
    def start_requests(self):
        yield scrapy.Request(self.url,self.parse)


    def parse(self, response):
        data = json.loads(response.body)

        for item in data.get("sections").get("products").get("results"):
            yield {
                "title": item.get("product_views").get("core").get("title"),
                "brand": item.get("product_views").get("core").get("brand"),
                "price": item.get("product_views").get("buybox_summary").get("prices"),
                # "pretty_price": item.get("product_views").get("buybox_summary").get("pretty_price")[0],
                "listing_price": item.get("product_views").get("buybox_summary").get("listing_price"),
                "savings": item.get("product_views").get("buybox_summary").get("saving"),
                "image_url":item.get("product_views").get("gallery").get("images")[0],  #check takealot to see what can be put under size
                "date": str(datetime.now()),
            }

        
        next_page_code = data.get("sections").get("products").get("paging").get("next_is_after")

        if  next_page_code != "":
            yield scrapy.Request(self.url + f"&after={next_page_code}", self.parse)


            

