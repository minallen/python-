# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
        在itmes 中定义字段之后，能直观的看到自己要爬取的字段，这些字段和spider中的字段是一样的，
        所以，爬取字段前，先制定item
    '''

    title = scrapy.Field()  #scrapy.Field是个字典
    position = scrapy.Field()
    publish_data = scrapy.Field()


'''
item 可以有多个：


class JDItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
        在itmes 中定义字段之后，能直观的看到自己要爬取的字段，这些字段和spider中的字段是一样的，
        所以，爬取字段前，先制定item
    

    title = scrapy.Field()
    position = scrapy.Field()
    publish_data = scrapy.Field()

'''
