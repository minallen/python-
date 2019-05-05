import re
import requests
import json


class NeihanSpider:
    """
    抓取内涵段子
    内涵段子官网报502错误，无法实施
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }

        self.start_url = "http://neihanshequ.com/"
        self.next_url_temp = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time={}"

    def parse(self, url):  # 发送请求
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_first_page_content_list(self, html_str):  # 提取第一页的数据
        content_list = re.findall(r"<h1 class=\"title\">.*?<p>(.*?)</p>", html_str, re.S)
        max_time = re.findall("max_time: '(.*?)',", html_str)[0]
        return content_list, max_time

    def save_content_list(self, content_list):
        with open("内涵段子.txt", 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功！")

    def get_content_list(self, json_str):  # 提取从第二页开始的json中的数据
        dict_ret = json.loads(json_str)
        data = dict_ret["data"]["data"]
        content_list = [i["group"]["content"] for i in data]
        max_time = dict_ret["data"]["max_time"]
        has_more = dict_ret["data"]["has_more"]
        return content_list, max_time, has_more

    def run(self):
        html_str = self.parse(self.start_url)
        content_list, max_time = self.get_first_page_content_list(html_str)
        self.save_content_list(content_list)
        has_more = True  # 刚开始假设有第二页
        while has_more:  # 内涵社区是用has_more 来判断是否有下一页的
            # 构造下一页的url地址：
            next_url = self.next_url_temp.format(max_time)
            json_str = self.parse(next_url)
            # 提取第二页之后的数据
            content_list, max_time, has_more = self.get_content_list(json_str)
            self.save_content_list(content_list)


if __name__ == '__main__':
    ns = NeihanSpider()
    ns.run()
