# -*- coding: utf-8 -*-
# Define your item pipelines here

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from tencent.items import TencentItem


client = MongoClient(host="192.16.16.1",port=27017)

'''
在mongo中写入数据时，注意：
    写入的数据库名要存在， 例如：tencent存在
'''
collection = client["tencent2"]["hr"]


class TencentPipeline(object):
    def process_item(self, item, spider):

        #collection.insert(item)

        #判断item是不是TencentItem的实例对象，当有多个item的时候，可以进行判断
        if isinstance(item,TencentItem):
            #把item转化成字典才能传入mongodb
            collection.insert(dict(item))


        #print(item)
        return item
