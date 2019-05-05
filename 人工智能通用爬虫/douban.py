'''
注意：
    1.豆瓣网爬取的url在search_subjects...里面
    2.用手机的形式进行访问
'''

import requests
import json


class DoubanWang:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def run(self):
        response = requests.get(url=self.url)
        response = response.content.decode()
        response = json.loads(response)

        with open(self.name + '.json', 'w', encoding='utf-8') as f:
            #ensure_ascii=False 就是让页面上的中文爬取过来以后也显示中文
            #indent=4缩进四个空格
            f.write(json.dumps(response, ensure_ascii=False, indent=4))


# if __name__ == '__main__':
#     doubanwang = DoubanWang(
#         'https://movie.douban.com/j/search_subjects?type=tv&tag=%E6%97%A5%E6%9C%AC%E5%8A%A8%E7%94%BB&sort=recommend&page_limit=20&page_start=0',
#         '日本动漫')
#     doubanwang.run()
