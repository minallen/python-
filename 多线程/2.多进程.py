"""
可以实现并发
但是，请求发送出去后和返回之前，中间时期进程空闲
编写方式：
    - 直接返回处理
    - 通过回调函数处理
"""

########### 编写方式一 ###########

#导入进程
from concurrent.futures import ProcessPoolExecutor
import requests



def task(url):
    response = requests.get(url)
    print(url,response)

#声明线程池：5个
pool = ProcessPoolExecutor(7)


url_list = [
    'http://www.cnblogs.com/wupeiqi',
    'http://huaban.com/favorite/beauty/',
    'http://www.bing.com',
    'http://www.zhihu.com',
    'http://www.sina.com',
    'http://www.baidu.com',
    'http://www.autohome.com.cn',
]

for url in url_list:
    #把url添加到线程池里面
    pool.submit(task,url)

#1、shutdown() 方法在终止前允许执行以前提交的任务，
# 而 shutdownNow() 方法阻止等待任务启动并试图停止当前正在执行的任务。
pool.shutdown(wait = True)

######################




########### 编写方式二 ###########

# #导入进程
# from concurrent.futures import ProcessPoolExecutor
# import requests
#
#
#
# def task(url):
#     '''
#     下载页面
#     :param url:
#     :return:
#     '''
#     response = requests.get(url)
#     #print(url,response)
#     return response
#
#
#
#
# def done(future,*args,**kwargs):
#
#     #future.result()  就是response对象
#     response = future.result()
#     print(response.status_code,response.content)
#
#
#
#
#
#
# #声明进程池：5个
# pool = ProcessPoolExecutor(7)
#
#
# url_list = [
#     'http://www.cnblogs.com/wupeiqi',
#     'http://huaban.com/favorite/beauty/',
#     'http://www.bing.com',
#     'http://www.zhihu.com',
#     'http://www.sina.com',
#     'http://www.baidu.com',
#     'http://www.autohome.com.cn',
# ]
#
# for url in url_list:
#     #把url添加到进程池里面
#     #拿到返回值
#     v = pool.submit(task,url)
#
#     #请求页面执行完之后，会去执行done方法
#     v.add_done_callback(done)
#
# #1、shutdown() 方法在终止前允许执行以前提交的任务，
# # 而 shutdownNow() 方法阻止等待任务启动并试图停止当前正在执行的任务。
# pool.shutdown(wait = True)

######################