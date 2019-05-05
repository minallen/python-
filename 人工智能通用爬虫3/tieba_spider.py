import json
import requests
from lxml import etree

#提取贴吧的标题和url地址和相应图片地址
#图片包含在详情页页面中


class TiebaSpider:

    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw="+tieba_name+"&pn=0"
        self.headers= {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
        self.part_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"


    def parse(self,url):    #发送请求
        response = requests.get(url,headers=self.headers)
        return response.content


    def get_content_list(self,html_str):
        html = etree.HTML(html_str)

        div_list = html.xpath("//div[contians(@calss,'i')]")   #根据div分组
        content_list = []

        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")) > 0 else None    #提取标题
            item["href"] = self.part_url + div.xpath("./a/@href")[0] if len(div.xpath("./a/href")) > 0 else None        #提取标题对应的url,详情页页面

            item["img_list"] = self.get_img_list(item["href"],[])  #获取详情页的图片的地址
            #这是一个item字典：   {'title': '...', 'href': '..', 'img_list': ['1...','2...']}
            #总的是这样的：    [
            #                   {'title': '...', 'href': '..', 'img_list': ['1...','2...']},
            #                   {'title': '...', 'href': '..', 'img_list': ['1...', '2...']},
            #                   {'title': '...', 'href': '..', 'img_list': ['1...', '2...']},
            #               ]


            content_list.append(item)

        next_url = self.part_url + html.xpath("//a[text()='下一页']/@href")[0] if len(("//a[text()='下一页']/@href")) > 0 else None
        return content_list,next_url


    def get_img_list(self,detail_url,total_img_list):   #获取帖子中的所有的图片
        detail_html_str = self.parse(detail_url)
        detail_html = etree.HTML(detail_html_str)
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")    # 获取详情页中的图片地址
        total_img_list.extend(img_list)                                   #extend能防止图片地址被覆盖
        detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")  #获取详情页中下一页的url，目的是获取里面的图片地址
        if len(detail_next_url) > 0:                                      #判断详情页中是否有下一页
            detail_next_url = self.part_url + detail_next_url[0]
            return self.get_img_list(detail_next_url,total_img_list)
        return total_img_list


    def save_content_list(self,content_list):
        file_path = self.tieba_name + '.txt'
        with open(file_path,'a',encoding='utf-8') as f:
            f.write(json.dumps(content_list,ensure_ascii=False,indent=2))
            f.write("\n")
        print("保存成功")


    def run(self):
        #1.start_url
        #2.发送请求，获取相应
        #3.提取数据，提取下一页的url
        #4.保存数据
        #5.请求下一页的url,循环2-5步
        next_url = self.start_url
        while True:
            html_str = self.parse(next_url)
            content_list, next_url = self.get_content_list(html_str)

            self.save_content_list(content_list)


if __name__ == '__main__':
    ts = TiebaSpider('做头发')
    ts.run()

