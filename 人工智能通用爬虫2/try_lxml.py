

from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-1"><a></a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>
        <li class="item-1"><a href="link6.html"></a></li>      
        </ul> </div> '''




html = etree.HTML(text)     #修复补全html,然后用xpath方法,这里html是个对象
#print(etree.tostring(html).decode())   #利用etree.tostring方法变成字符串,然后判断输出的html格式是否正确，再去写xpath代码

'''
    1.获取class="item-1"  li 下的 a 的href
    r1 = html.xpath("//div//li[@class='item-1']/a/@href")
    
    2.获取class="item-1"  li下的 a 的 文本   
    r2 = html.xpath("//li[@class='item-1']/a/text()")


'''
r1 = html.xpath("//div//li[@class='item-1']/a/@href")
r2 = html.xpath("//li[@class='item-1']/a/text()")

#每个li 是一条新闻，把url和文本组成字典

#如果每个url标签对应一个文本的话，取出url对应的文本的位置（注意：每个href 对应的索引的位置就是对应的文本的位置）
# for href in r1:
#     item = {}
#     item["href"] = href
#     item["title"] = r2[r1.index(href)]
#     print(item)


'''取出url对应的文本的位置，这里有url标签缺失的情况出现'''

#1.先取出所有的li标签,返回结果是列表
r3 = html.xpath("//li[@class='item-1']")
#2.遍历取出每个li标签
for i in r3:
    item = {}
#3.在当前li标签下面取出url,返回结果可能是多个值，这里只有一个，所以取第0个,但是如果是空的话，会报错，所以判断一下长度
    item['href'] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href"))>0 else None
#4.继续在当前li标签下面取出title,返回结果可能是多个值，这里只有一个，所以取第0个,但是如果是空的话，会报错，所以判断一下长度
    item['title'] = i.xpath("./a/text()")[0] if len(i.xpath("./a/text()"))>0 else None
    print(item)









