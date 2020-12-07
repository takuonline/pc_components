# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class HifiProjectPipeline(object):

    table_name  = "hifi"

    def __init__(self):
        self.databaseURL = 'https://pc-components-77a24-default-rtdb.firebaseio.com/'
        
 

    def open_spider(self,spider):
        cred = credentials.Certificate('./hifi_project/pc-components.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL':self.databaseURL
        })
        
        self.ref = db.reference(self.table_name)


    def process_item(self, item, spider):
        self.ref.push(dict(item))

        return item




class TakealotProjectPipeline(object):

    table_name  = "takealot"

    def __init__(self):
        self.databaseURL = 'https://pc-components-77a24-default-rtdb.firebaseio.com/'  

    def open_spider(self,spider):
        cred = credentials.Certificate('./hifi_project/pc-components.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL':self.databaseURL
        })
        
        self.ref = db.reference(self.table_name)

    def process_item(self, item, spider):
        self.ref.push(dict(item))
        return item


class ComputermaniaProjectPipeline(object):

    table_name  = "computermania"

    def __init__(self):
        self.databaseURL = 'https://pc-components-77a24-default-rtdb.firebaseio.com/'  

    def open_spider(self,spider):
        cred = credentials.Certificate('./hifi_project/pc-components.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL':self.databaseURL
        })
        
        self.ref = db.reference(self.table_name)

    def process_item(self, item, spider):
        self.ref.push(dict(item))
        
        return item






