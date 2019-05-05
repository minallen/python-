import requests
# etree是用c语言编写的，所以不显示
from lxml import etree
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "Referer": "https://movie.douban.com/"
}

url = "https://movie.douban.com/cinema/nowplaying/wuhai/"

response = requests.get(url, headers=headers)

content = response.content.decode()

content = etree.HTML(content)

ul_list = content.xpath("//ul[@class='lists']")[0]
# 查看一下获取了几个ul_list
# print(ul_list)

li_list = ul_list.xpath("./li")
# print(li_list)

l = []

for li in li_list:
    title = li.xpath("./@data-title")[0]
    score = li.xpath("./@data-score")[0]
    href = li.xpath(".//a/@href")[0]
    img = li.xpath(".//li[1]//img/@src")[0]
    # print(img)
    item = {
        "title": title,
        "score": score,
        "href": href,
        "img": img,
    }

    l.append(item)

with open("douban.txt", 'a', encoding="utf-8") as f:
    for item in l:
        f.write(json.dumps(item, ensure_ascii=False, indent=4))
