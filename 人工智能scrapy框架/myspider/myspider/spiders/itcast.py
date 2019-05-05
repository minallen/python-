# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'     #爬虫名字
    allowed_domains = ['itcast.cn']             #允许爬取的范围
    #start_urls = ['http://itcast.cn/']      #最开始的url地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)

        #分组：
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            # item["name"]=li.xpath(".//h3/text()").extract()[0]
            # item["title"]=li.xpath(".//h4/text()").extract()[0]

            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            #print(item)
            '''
            extract拿不到结果是个空值，extract_first拿不到结果是个None
            
            1.把数据传递给piplines,yield 的效果就是减少内存的占用
            2.需要把pipline在settings.py中开启才行
                ITEM_PIPELINES = {
                                   'myspider.pipelines.MyspiderPipeline': 300,
                                }
                300表示的是距离引擎的远近,数字越小，则先执行。
            3.为了把数据在不同的pipline中进行传递，前一个pipline类必须有return才行，否则，下一个类执行结果就是none值
                
                
            '''

            yield  item