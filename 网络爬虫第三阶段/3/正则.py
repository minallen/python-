import re

# text = "-0475-3111212"
# ret = re.match('[\d\-]+',text)
# print(ret.group())


# text = "+a+b+cd"
# ret = re.findall('\w+',text)
# print(ret)
#
# text = "gryt"
# ret = re.findall('\w{3}',text)
#
# ret1 = re.match('\w{2}',text)
# print(ret)
# print(ret1.group())


#
'''
匹配手机号码
以1开头，第二位数字是3578中的一位，后面有9个数字

phone = "15247332714"
phone1 = "15247332714567"

phone_num = re.match('1[3578]\d{9}',phone1)
print(phone_num.group())
'''

'''
匹配邮箱地址
email = "1842972045@qq.com"
ret = re.match('\w+@[a-z0-9]+\.[a-z]+',email)
print(ret.group())
'''

'''
匹配URL
url = "http://www.ujiuye.cn/zt/pythonxxy/?wt.mc_id=ll-bdbc-pc-python-bj-17609913"
url1 = "https://www.ujiuye.cn/zt/pythonxxy/?wt.mc_id=ll-bdbc-pc-python-bj-17609913"
url2 = "ftp://www.ujiuye.cn/zt/pythonxxy/?wt.mc_id=ll-bdbc-pc-python-bj-17609913"

ret = re.match('(http|https|ftp)://[^\s]+',url2)
print(ret.group())
'''

'''
匹配身份证号码
中括号只能匹配一个字符
ID = "152323199406022311"
ID_NUM = re.match('\d{17}[\dxX]',ID)
print(ID_NUM.group())
'''

# text = "hello"
# ret = re.match('^h',text)
# print(ret.group())

# text = "allen@163.com"
# ret =re.match('\w+(@163.com)$',text)
# print(ret.group())
#
# ret =re.match('[a-z]+(@163.com)$',text)
# print(ret.group())

# text = "allen@163.com"
# ret =re.match('\w+@163.com$',text)
# print(ret.group())


# text = "https"
# ret = re.match('(http|https|ftp)$',text)
# print(ret.group())

'''
text = "123456789"
ret = re.match('\d+',text)
print(ret.group())          #   0123456789

text = "123456789"
#? 表示让 + 的匹配次数达到最少，那就是1次，因为 + 的功能是匹配1至多个
ret1 = re.match('\d+?',text)
print(ret1.group())         #   1


text2 = "<h1>标题</h1>"
ret2 = re.match('<.+>',text2)
ret3 = re.match('<.+?>',text2)
print('贪婪：',ret2.group())
print('非贪婪：',ret3.group())

text3 = "<h1>标题</h1>"
ret4 = re.findall('<.*>(.*?)<.*>',text3)
print(ret4)

'''

#匹配0-100之间的数字
# text = "23"
# ret = re.match('0$|[1-9]\d?$|100$',text)
# print(ret.group())
#
# text1 = "apple is $1566.65335"
# ret1 = re.search('\$\d+\.\d+',text1)
#
# text2 = "apple is $16"
# ret2 = re.search('\$\d+',text2)
# print(ret2.group())

#
# text = r"\n"
# print(text)

# text = "\n"
#
# ret = re.search(r'\\n',text)
# print(ret)



# text = "sasdfa\n"
# #ret = re.findall('.',text,re.S)
# ret = re.findall('.',text,re.S)
# print(ret)



# text = "apple's price is $99,orange's price is $12"
#括号中的内容是分组的内容
# ret = re.search('.*(\$\d+).*(\$\d+)',text)

#print(ret.group())        #apple's price is $99,orange's price is $12
#print(ret.group(1))      #$99
#print(ret.group(2))      #$12
#print(ret.group(1,2))      #('$99', '$12')
# print(ret.groups())


# text = "apple's price is $99,orange's price is $12"
# ret = re.findall('\$\d+',text)
# print(ret)

# text = "apple's price is $99,orange's price is $12"
# ret = re.sub('\$\d+','$0',text)         #apple's price is $0,orange's price is $0
# ret1 = re.sub('\$\d+','$0',text,1)      #apple's price is $0,orange's price is $12

# print(ret)
# print(ret1)

#text = "ni hao hello@@world"
#ret = re.split('[^a-zA-Z]+',text)
#ret = re.split(' ',text)
# print(ret)


"""
text = "apple's price is $9.94,orange's price is $12.5"
#先编译号提取的内容
r_obj = re.compile('\d+\.?\d*')
#直接传入编译内容和文本即可
ret = re.search(r_obj,text)
print(ret.group())

ret2 = re.findall(r_obj,text)
print(ret2)

"""

# text = "apple's price is $9.94,orange's price is $12.5"
#
# r = re.compile(r"""
#     \$\d+ #小数点前面的数字
#     \.?   #小数点本身
#     \d*   #小数点后面的数字
# """,re.VERBOSE)
#
# ret = re.findall(r,text)
# print(ret)

# 正常情况下‘.’是不能匹配‘\n’的，但是加上re.DOTALL之后，就能匹配出'\n'
text = """
    你好
    世界

"""
ret = re.findall('.',text,re.DOTALL)
ret1 = re.findall('.',text)
print(ret)
print(ret1)


"""
dic = {"index":0,"name":"allex","age":20}
dic = {"index":0,"name":"allex","age":20}
dic = {"index":0,"name":"allex","age":20}
dic = {"index":0,"name":"allex","age":20}
dic = {"index":0,"name":"allex","age":20}
dic = {"index":0,"name":"allex","age":20}

"""
values = [
        {'username':'张三','age':18,'height':180},
        {'username':'李四','age':19,'height':190},
        {'username':'王五','age':20,'height':160}
    ]
print(type(values))


