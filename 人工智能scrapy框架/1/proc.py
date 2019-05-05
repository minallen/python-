#
# from lxml import etree
#
# html = '''<div class="top"><span>世界</span>你好</div>'''
#
# html = etree.HTML(html)
# html_str1 = html.xpath("//div[@class='top']//text()")
# html_str2 = html.xpath("//div[@class='top']/text()")
# print(html_str1,html_str2)



a = {"k1":"v1","k2":"v2"}



b = a
b["k1"] = "v11"
print(b)    #{'k1': 'v11', 'k2': 'v2'}
#修改b的值，a也会被修改
print(a)    #{'k1': 'v11', 'k2': 'v2'}

#防止a被修改：
from copy import deepcopy
b = deepcopy(a)
b["k1"] = "v11"
print(b)
print(a)

