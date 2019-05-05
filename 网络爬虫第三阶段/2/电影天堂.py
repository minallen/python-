import requests
import json
from lxml import etree


class DianYING:
    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
        }
        self.start_url = "https://www.dy2018.com/html/gndy/dyzz/index.html"
        self.part_url = "https://www.dy2018.com"

    def parse(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode("gbk")

    def get_content(self, html_str):
        html = etree.HTML(html_str)
        tb_list = html.xpath("//div[@class='co_content8']//table")
        content_list = []
        for tb in tb_list:
            item = {}
            item["title"] = tb.xpath(".//tr[2]//a/@title")
            item["href"] = tb.xpath(".//tr[2]//a/@href")
            item["href"] = ["https://www.dy2018.com" + i for i in item["href"]][0]
            item["img"],item["movi_name"] = self.get_detail_content(item["href"])
            content_list.append(item)
        next_url = self.part_url + html.xpath("//div[@class='co_content8']/div[@class='x']/a[text()='下一页']/@href")[0] \
            if len(("//a[text()='下一页']/@href")) > 0 else None
        return content_list, next_url

    def get_detail_content(self, href):
        detail_html_str = self.parse(href)
        detail_html = etree.HTML(detail_html_str)
        img_src = detail_html.xpath("//div[@id='Zoom']/p[1]/img/@src")
        movi_name = detail_html.xpath("//div[@id='Zoom']/p[3]/text()")
        return img_src,movi_name

    def save_content(self, content_list):
        with open("dy.txt", 'a', encoding="utf-8") as f:
            for item in content_list:
                f.write(json.dumps(item, ensure_ascii=False, indent=4))

    def run(self):
        # 1.start_url
        # 2.发送请求，获取响应
        # 3.提取数据，
        # 4.保存数据
        # html_str = self.parse(self.start_url)
        # content_list, next_url = self.get_content(html_str)
        # self.save_content(content_list)
        next_url = self.start_url
        while True:
            html_str = self.parse(next_url)
            content_list, next_url = self.get_content(html_str)
            self.save_content(content_list)


if __name__ == '__main__':
    dy = DianYING()
    dy.run()
