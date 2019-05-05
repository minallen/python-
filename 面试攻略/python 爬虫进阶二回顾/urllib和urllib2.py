import time


'''
一、爬虫简介

    1.什么是爬虫？
        爬虫：就是抓取网页数据的程序。
    
    2.HTTP和HTTPS？
        HTTP协议（HyperText Transfer Protocol，超文本传输协议），
    是一种发布和接收 HTML页面的方法。
        HTTPS（Hypertext Transfer Protocol over Secure Socket Layer），
    简单讲是HTTP的安全版，在HTTP下加入SSL层。
        SSL（Secure Sockets Layer 安全套接层）主要用于Web的安全传输协议，
    在传输层对网络连接进行加密，保障在Internet上数据传输的安全。
    
    3.浏览器发送HTTP请求的过程?
        1.当用户在浏览器的地址栏中输入一个URL并按回车键之后，浏览器会向HTTP服务器发送HTTP请求。
    HTTP请求主要分为“Get”和“Post”两种方法。    
        2.之后浏览器发送一个Request请求去获取url对应的html文件，
    服务器把Response文件对象发送回给浏览器。
        3.浏览器分析Response中的 HTML，并下载对应的文件   
        4.当所有的文件都下载成功后，网页会根据HTML语法结构，完整的显示出来
    
    4.URL
        定义：统一资源定位符，是用于完整地描述Internet上网页和其他资源的地址的一种标识方法。
        基本格式：scheme://host[:port#]/path/…/[?query-string][#anchor]
        scheme：协议(例如：http, https, ftp)
        host：服务器的IP地址或者域名
        port#：服务器的端口（如果是走协议默认端口，缺省端口80）
        path：访问资源的路径
        query-string：参数，发送给http服务器的数据
        anchor：锚（跳转到网页的指定锚点位置）
    
    5.客户端HTTP请求        
        URL只是标识资源的位置，而HTTP是用来提交和获取资源。
        客户端发送一个HTTP请求到服务器的请求消息，包括以下格式：
            请求行、请求头部、空行、请求数据
        
        常见请求报头：
            Host (主机和端口号)   
            User-Agent：是客户浏览器的名称
            Referer：表明产生请求的网页来自于哪个URL，
            Cookie：浏览器用这个属性向服务器发送Cookie。
    
        cookie 和session：
            http是无状态请求
            服务器和客户端的交互仅限于请求/响应过程，结束之后便断开，在下一次请求时，
            服务器会认为新的客户端。
            为了维护他们之间的链接，让服务器知道这是前一个用户发送的请求，
            必须在一个地方保存客户端的信息。
            Cookie：通过在客户端记录的信息确定用户的身份。
            Session：通过在服务器端记录的信息确定用户的身份。   
            
    6.HTTP请求方法
        序号   方法      描述
        1     GET       请求指定的页面信息，并返回实体主体。
        2     HEAD      类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
        3     POST      向指定资源提交数据进行处理请求（例如提交表单或者上传文件），数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
        4     PUT       从客户端向服务器传送的数据取代指定的文档的内容。
        5     DELETE    请求服务器删除指定的页面。
        6     CONNECT   HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
        7     OPTIONS   允许客户端查看服务器的性能。
        8     TRACE     回显服务器收到的请求，主要用于测试或诊断。
    
    7.主要方法get和post请求
        GET是从服务器上获取数据，POST是向服务器传送数据
        GET请求参数显示，都显示在浏览器网址上，
    HTTP服务器根据该请求所包含URL中的参数来产生响应内容，    
    即“Get”请求的参数是URL的一部分        
    例如： http://www.baidu.com/s?wd=Chinese
        
        POST请求参数在请求体当中，消息长度没有限制而且以隐式的方式进行发送，
    通常用来向HTTP服务器提交量比较大的数据，
    请求的参数包含在“Content-Type”消息头里，指明该消息体的媒体类型和编码.
    
    8.HTTP响应状态码
        200：请求成功（其后是对GET和POST请求的应答文档）
        303；所请求的页面可在别的url下被找到。
        304：服务器告诉客户，原来缓冲的文档还可以继续使用
        403：对被请求页面的访问被禁止。
        404：没有找到文件或目录
        500：请求未完成。服务器遇到不可预知的情况。
    
    9.HTTP代理工具Fiddler（抓包工具）
    
    
二、urllib2
    urllib2模块直接导入就可以用，在python3中urllib2被改为urllib.request
    
    随机选择一个Use-Agent:
        为了防止封IP，先生成一个user-agent列表，然后从中随机选择一个
        user-Agents = [...]
        user_agent = random.choice(user-Agents)      
   
'''