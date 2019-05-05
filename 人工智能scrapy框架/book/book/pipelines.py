# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from book.items import BookItem

client = MongoClient(host="192.16.16.1",port=27017)
collection = client["jd_book"]["book"]

class BookPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def process_item(self, item, spider):
        collection.insert(item)
        #判断item是不是BookItem的实例对象，当有多个item的时候，可以进行判断
        # if isinstance(item,BookItem):
        #     #把item转化成字典才能传入mongodb
        #     collection.insert(dict(item))
        return item