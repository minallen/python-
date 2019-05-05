import requests

'''

1.
response = requests.get(url='http://www.baidu.com')
#修改编码方式
response.encoding = 'utf-8'
print(response.text)   返回的是标签信息
print(response.content.decode())  对返回的二进制进行解码变成str形式

2.
response = requests.get(url='https://www.baidu.com/img/bd_logo1.png')
#保存二进制的文件用二进制的方式
with open('百度.png','wb') as f:
    f.write(response.content)
    
3.    
response = requests.get(url='https://www.sina.com.cn/')
print(response.status_code)
#返回状态码
print(response.text)
print('----------------------')
print(response.content.decode())
print(response.request.其他参数)


4.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
response = requests.get(url='http://www.baidu.com',headers=headers)
print(response.content.decode())


#①
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
url_temp = 'http://www.baidu.com/?wd={}'.format('python')
response = requests.get(url=url_temp,headers=headers)
print(response.status_code)
print(response.request.url)


#②
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"}
p = {"wd":"老男孩"}
url_temp = 'http://www.baidu.com/s'
response = requests.get(url=url_temp,headers=headers,params=p)
print(response.status_code)
print(response.request.url)


5.requests.post 这个实验没成功，但是整体还是简单的。
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Mobile Safari/537.36"}
post_data ={
    "query": "人生苦短，我用python",
    "from": "zh",
    "to": "en",
}
post_url = "https://fanyi.baidu.com/basetrans"
response = requests.post(url=post_url,headers=headers,data=post_data)
print(response.content.decode())


requests 中的编码和解码问题：
        1.response.content.decode() 这种方式默认用utf-8进行解码
        2.response.content.decode('gbk')
        3.response.text
        4.bytes转化为str:  用decode()


代理IP网址：https://proxy.mimvp.com

-----------------------------------------
如果爬取必须要先登陆的页面时，用session进行访问：
import requests

session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}
#使用session发送post请求，cookie保存在其中
session.post(post_url,data=post_data,headers=headers)

#session进行请求的是，第一次成功登陆之后访问的地址
r = session.get("http://www.renren.com/327550029/profile",headers=headers)

#保存页面
with open("renren1.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())
-----------------------------------------

#字典推到式：
ret1 = {i:i+6 for i in range(8)}
print(ret1)
ret2 = {i:'v' for i in range(10)}
print(ret2)

-----------------------------------------

# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
}

cookies="anonymid=j3jxk555-nrn0wh; _r01_=1; _ga=GA1.2.1274811859.1497951251; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; ln_uact=mr_mao_hacker@163.com; depovince=BJ; jebecookies=54f5d0fd-9299-4bb4-801c-eefa4fd3012b|||||; JSESSIONID=abcI6TfWH4N4t_aWJnvdw; ick_login=4be198ce-1f9c-4eab-971d-48abfda70a50; p=0cbee3304bce1ede82a56e901916d0949; first_login_flag=1; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg; t=79bdd322e760beae79c0b511b8c92a6b9; societyguester=79bdd322e760beae79c0b511b8c92a6b9; id=327550029; xnsid=2ac9a5d8; loginfrom=syshome; ch_id=10016; wp_fold=0"
cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
print(cookies)

r = requests.get("http://www.renren.com/327550029/profile",headers=headers,cookies=cookies)

#保存页面
with open("renren3.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())
    
    
#把cookie对象转化为字典
requests.utils.dict_from_cookiejar(放cookies对象)
#把cookie字典转化为对象
requests.utils.cookiejar_from_dict(放cookies字典)   


#对url进行解码
requests.utils.unquote()
#对url进行编码
requests.utils.quote()


#三元运算
a = 3 if 3>2 else 4
print(a)
 
 
#不进行ssl验证
r = requests.get(url='https://www.12306.cn/index/',verify=False )
print(r) 
-----------------------------------------
import requests

from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}


@retry(stop_max_attempt_number=3)  # 意思是最多可以尝试3次请求，retry 是用来捕获异常的
def _parse_url(url, method, data, proxies):
    print("*" * 10)
    if method == 'POST':
        requests.post(url, proxies, data=data, headers=headers, )
    else:
        response = requests.get(url, proxies, headers=headers, timeout=3)

    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except Exception as e:
        html_str = None

    return html_str


if __name__ == '__main__':
    url = 'www.baidu.com'
    print(parse_url(url))
-----------------------------------------
1.json.loads(response)此操作完全是为了当前显示的时候以字典形式进行显示，否则刚爬取的数据是一堆html字符串，显示杂乱
2.进行json.dumps是为了写入文件，dict类型无法写入文件
如果要进行写入文件的话，1 和2 必须搭配出现

'''










