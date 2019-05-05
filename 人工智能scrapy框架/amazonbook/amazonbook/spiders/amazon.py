# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import re

class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    #start_urls = ['https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sd_allcat_books_l1?ie=UTF8&node=658390051']
    redis_key = "amazon"

    rules = (
        #匹配大分类和小分类的url(大分类和小分类的url的标签相同)
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='leftNav']//div[contains(@class,'a-row a-expander-container')]/li")),follow=True),
        #匹配图书的url地址(先定位到h2,然后向上取h2的父一级，用‘..’获取)
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..",)),callback="parse_book_detail"),
        #列表页翻页
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']",)),follow=True),
    )

    #rules = (
    #     #匹配大分类的url地址和小分类的url
    #     Rule(LinkExtractor(restrict_xpaths=("//div[@class='categoryRefinementsSection']/ul/li",)), follow=True),
    #     #匹配图书的url地址
    #     Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..",)),callback="parse_book_detail"),
    #     #列表页翻页
    #     Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']",)),follow=True),
    #
    # )

    def parse_book_detail(self,response):
        item = {}
        item["book_title"] = response.xpath("//span[@id='ebooksProductTitle']/text()").extract()

        item["book_title"] = [re.sub(r"\n", "", i) for i in item["book_title"]]
        item["book_title"] = [re.sub(r" ", "", i) for i in item["book_title"]]

        item["book_auther"] = response.xpath("//div[@id='bylineInfo']/span/a/text()").extract()
        item["book_img"] = response.xpath("//div[@id='ebooks-img-canvas']/img/@src").extract_first()
        item["book_price"] = response.xpath("//tr[@class='print-list-price']/td[2]/text()").extract_first()
        item["book_cate"] = response.xpath("//ul[@class='a-unordered-list a-horizontal a-size-small']/li[3]/a/text()").extract()
        item["book_publish"] = response.xpath("//b[text()='出版社:']/../text()").extract_first()
        print(item)