# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json
import urllib



class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com','p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt")    #大分类
        for dt in dt_list:
            item = {}
            #大分类的名字
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            #获取当前标签的下一个兄弟节点：dt.xpath("./following-sibling::dd[1]")
            #每个dd标签下面有很多em标签
            em_list = dt.xpath("./following-sibling::dd[1]/em") #小分类列表
            for em in em_list:
                #小分类的url
                item["s_href"] = em.xpath("./a/@href").extract_first()
                #小分类的名字
                item["s_cate"] = em.xpath("./a/text()").extract_first()

                #判断小分类的url是不是存在
                if item["s_href"] is not None:
                    item["s_href"] = "https:" + item["s_href"]
                    #构造小分类的请求
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        meta={"item":deepcopy(item)}
                    )

    def parse_book_list(self,response):         #解析列表页（就是小分类详情页数据请求）
        item = response.meta["item"]
        #
        li_list = response.xpath("//div[@id='plist']/ul/li")
        for li in li_list:
            item["book_img"] = li.xpath(".//div[@class='p-img']//img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = li.xpath(".//div[@class='p-img']//img/@data-lazy-img").extract_first()
            item["book_img"] = "https:" + item["book_img"] if item["book_img"] is not None else None
            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first().strip()
            item["book_auther"] = li.xpath(".//span[@class='author_type_1']/a/text()").extract()
            #出版社名字
            item["book_press"] = li.xpath(".//span[@class='p-bi-store']/a/text()").extract_first()
            #出版日期
            item["book_publish_date"] = li.xpath(".//span[@class='p-bi-date']/text()").extract_first().strip()
            item["book_sku"] = li.xpath("./div/@data-sku").extract_first()

            #构造价格的请求
            yield scrapy.Request(
                #域名和上面的域名不相同，所以需要添加到allowed_domains当中
                "https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["book_sku"]),
                callback=self.parse_book_price,
                meta={"item": deepcopy(item)}
            )
        #列表页翻页（就是小分类详情页翻页）
        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            #next_url = "https://list.jd.com" + next_url        #原始补全方法
            next_url = urllib.parse.urljoin(response.url, next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                #meta={"item": item}
                meta={"item":item}
            )

    def parse_book_price(self,response):
        item = response.meta["item"]
        #价格请求页面response是个json,
        item["book_price"] = json.loads(response.body.decode())[0]["op"]
        print(item)
        #yield item