# -*- coding: utf-8 -*-

import scrapy
from yangguang.items import YangguangItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    #start_urls = ['http://sun0769.com/']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        #分组：
        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        for tr in tr_list:
            item = YangguangItem()
            item["title"] = tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item["href"] = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item["publish_date"] = tr.xpath("./td[last()]/text()").extract_first()
           

            #调用函数处理详情页
            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                #meta是用来把数据传递给调用的函数
                meta={"item":item}
            )
        #翻页   根据文本内容进行获取：a[text()='>']
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    def parse_detail(self,response):       #处理详情页
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='c1 text14_2']//text()").extract()
        item["content_img"] = response.xpath("//div[@class='c1 text14_2']//img/@src").extract()
        #图片地址头部不完整,所以加上前面的信息：
        item["content_img"] = ["http://wz.sun0769.com"+ i for i in item["content_img"]]
        yield item



