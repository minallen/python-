# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem

'''
注意：爬取网页里table里面的数据时，有并列的table或者td之类的，就table[1],table[2],td[1],td[2]这样取值
'''

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]

        for tr in tr_list:
            #item = {}
            item = TencentItem()
            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["position"] = tr.xpath("./td[2]/text()").extract_first()
            item["publish_data"] = tr.xpath("./td[5]/text()").extract_first()
            #发送数据到pipline做持久化
            yield item

        #寻找下一页的url地址
        next_url = response.xpath("//a[@id='next']/@href").extract_first()
        #判断是不是下一页：
        if next_url != 'javascript':
            next_url = "http://hr.tencent.com/" + next_url
            #发送url给调度器
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )