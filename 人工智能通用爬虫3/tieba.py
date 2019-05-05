import requests, json
from lxml import etree
'''
#把cookie对象转化为字典
requests.utils.dict_from_cookiejar(放cookies对象)
#把cookie字典转化为对象
requests.utils.cookiejar_from_dict(放cookies字典)   

'''

class TieBa:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
        self.url_list = "https://www.qiushibaike.com/text/page/{}/"
        #实力化一个全局的session,这样就携带第一次的cookie进行访问
        #self.session = requests.session()

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        #response = self.session.get(url, headers=self.headers)
        #print(response.cookies,type(response.cookies))
        # 把cookie对象转化为字典
        cookies = requests.utils.dict_from_cookiejar(response.cookies)
        print('------------->',cookies)
        return response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            item = {}
            item["content"] = div.xpath(".//a[@class='contentHerf']//span/text()")
            item["content"] = [i.replace("\n", "") for i in item["content"]]
            item["img_src"] = div.xpath("./div[contains(@class,'author')]//img/@src")
            # print(item["content"])
            content_list.append(item)       #[{'content':'c1','img_src':'i1'},{content':'c2','img_src':'i2},...]
        return content_list

    def get_url_list(self):
        return [self.url_list.format(i) for i in range(1, 14)]

    def save_content_list(self, content_list):
        # with open('qiushi.txt', 'a', encoding='utf-8') as f:
        #     for item in content_list:     #item是一个个的字典
        #         f.write(json.dumps(item, ensure_ascii=False, indent=4))
        #         f.write("\n")
        print('保存成功')

    def run(self):
        '''
        1.url_list
        2.发送请求，获取响应
        3.提取数据
        4.保存数据
        '''
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)


if __name__ == '__main__':
    tb = TieBa()
    tb.run()
