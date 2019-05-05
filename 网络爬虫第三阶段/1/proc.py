# import requests
#
#
#
# session = requests.session()
# post_url = "http://www.renren.com/PLogin.do"
# post_data = {"email":"970138074@qq.com", "password":"pythonspider"}
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
# }
# #使用session发送post请求
# #第一次用session进行登陆之后，cookie保存在其中
# session.post(post_url,data=post_data,headers=headers)
#
# #session进行请求的是，第一次成功登陆之后访问的地址
# r = session.get("http://www.renren.com/327550029/profile",headers=headers)
#
# #保存页面
# with open("renren1.html","w",encoding="utf-8") as f:
#     f.write(r.content.decode())

"""
choice() 方法返回一个列表，元组或字符串的随机项。
choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

import random
random.choice( seq  )
    seq -- 可以是一个列表，元组或字符串。
"""

import random

li = ['aa','bb','cc','dd','ee','ff']

r = random.choice(li)
print(r)

