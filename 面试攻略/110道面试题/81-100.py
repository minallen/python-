import time


#81、举例说明SQL注入和解决办法
'''
当以字符串格式化书写方式的时候，如果用户输入的有;+SQL语句，后面的SQL语句会执行，
比如例子中的SQL注入会删除数据库demo
input_name = "zs;drop database demo"
sql = "select * from demo where name='%s" %input_name
print(sql)

解决方式：通过传参数方式解决SQL注入
params = [input_name]
count = cs1.execute('select * from demo where name="%s",params) 

'''
#82、s="info:xiaoZhang 33 shandong",
# 用正则切分字符串输出
# ['info', 'xiaoZhang', '33', 'shandong']

'''
import re
s="info:xiaoZhang 33 shandong"
s_ret = re.split(r'[:| ]',s)
print(s_ret)

'''
#83、正则匹配以163.com结尾的邮箱
'''
email_list = ["xiaowang@163.com","xiaoming@qq.com","xiaoshuai@163.com"]
import re
for email in email_list:
    email_list_ret = re.findall(r'[\w]{4,20}@163\.com$',email)
    if email_list_ret:
        print(email_list_ret)
    else:
        pass
'''

#84、递归求和,递归完成 1+2+3+4，，，，+10的和
'''
def get_sum(num):
    if num >= 1:
        res = num + get_sum(num-1)
    else:
        res = 0
    return res
res = get_sum(5)
print(res)

# res =  5 + get_sum(4)
# res = 5 + 4 + get_sum(3)
# res = 5 + 4 + 3 + get_sum(2)
# res = 5 + 4 + 3 + 2 + get_sum(1)
# res = 5 + 4 + 3 + 2 + 1 + get_sum(0)

'''
#85、python字典和json字符串相互转化方法
'''
import json
dic = {"name":"zs"}
ret1 = json.dumps(dic)
print(type(ret1))   #<class 'str'>

ret2 = json.loads(ret1)
print(type(ret2))   #<class 'dict'>
'''
#86、MyISAM 与 InnoDB 区别：
'''
1、InnoDB 支持事务，MyISAM 不支持，这一点是非常之重要。事务是一种高

级的处理方式，如在一些列增删改中只要哪个出错还可以回滚还原，而 MyISAM

就不可以了；

2、MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修改以及涉及到

安全性较高的应用；

3、InnoDB 支持外键，MyISAM 不支持；

4、对于自增长的字段，InnoDB 中必须包含只有该字段的索引，但是在 MyISAM

表中可以和其他字段一起建立联合索引；

5、清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重

建表

'''
#87、统计字符串中某字符出现次数
"""
str = "张三 美国 小日本 哈哈 呵呵 张 三"
str_count = str.count("张三")
print(str_count)  # 1

"""
#88、字符串转化大小写
'''
str1 = "allen"
str1 = str1.upper()
print(str1)     #ALLEN

str2 = str1.lower()
print(str2)     #allen

'''
#89、用两种方法去空格
"""
str1 = "hello world haha hehe"
str1 = str1.split(" ")
str1 = "".join(str1)
print(str1)     #helloworldhahahehe

str2 = "hello world haha hehe"
str2 = str2.replace(' ','')
print(str2)     #helloworldhahahehe
"""

#90、正则匹配不是以4和7结尾的手机号

"""
import re
tels = ["332814","332817","332817","332816"]
for tel in tels:
    ret = re.match('1[\d]{9}[0-3,5-6,8-9]',tel)
    if ret:
        print('正确的手机号码',ret.group())
    else:
        print('错误的手机号码',tel)

"""

#91、简述python引用计数机制

"""
python垃圾回收主要以引用计数为主，
标记-清除和分代清除为辅的机制，
其中标记-清除和分代回收主要是为了处理循环引用的难题。

引用计数算法
当有1个变量保存了对象的引用时，此对象的引用计数就会加1

当使用del删除变量指向的对象时，
如果对象的引用计数不为1，比如3，
那么此时只会让这个引用计数减1，即变为2，
当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除

"""

#92、int("1.4"),int(1.4)输出结果？
"""
print(int("1.4"))   #ValueError
print(int(1.4))     #1

"""

#93、列举3条以上PEP8编码规范
"""
1、顶级定义之间空两行，比如函数或者类定义。

2、方法定义、类定义与第一个方法之间，都应该空一行

3、三引号进行注释

4、使用Pycharm、Eclipse一般使用4个空格来缩进代码

"""

#94、正则表达式匹配第一个URL
"""
s = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&rsv_pq=f912242f00000db7&rsv_t=7303ZsYPgxjNvPXiFYC4sw6XnA%2FoEv%2B4FEmxpbfwyXcd9fZ6YFUaAP8XdJc&rqlang=cn&rsv_enter=1&rsv_sug3=3&rsv_sug1=2&rhttps://www.baidu.comsv_sug7=101&rsv_sug2=0&ihttps://www.baidu.comnputT=2342&rsv_sug4=4060&rsv_sug=2"
import re
ret = re.findall(r'https://.*?\.com',s)
print(ret)      #['https://www.baidu.com', 'https://www.baidu.com', 'https://www.baidu.com']

"""

#95、正则匹配中文
"""
import re
title = "你好 ，世界，aaa，我爱北京天安门"
t_obj = re.compile(r'[\u4e00-\u9fa5]+')
ret = re.findall(t_obj,title)
print(ret)

"""

#96、简述乐观锁和悲观锁
"""
悲观锁, 就是很悲观，每次去拿数据的时候都认为别人会修改，
所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会block直到它拿到锁。
传统的关系型数据库里边就用到了很多这种锁机制，
比如行锁，表锁等，读锁，写锁等，都是在做操作之前先上锁。

乐观锁，就是很乐观，每次去拿数据的时候都认为别人不会修改，
所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，
可以使用版本号等机制，乐观锁适用于多读的应用类型，这样可以提高吞吐量

"""

#97 r、r+、rb、rb+文件打开模式区别


#98、Linux命令重定向 > 和 >>
"""
Linux 允许将命令执行结果 重定向到一个 文件

将本应显示在终端上的内容 输出／追加 到指定文件中

> 表示输出，会覆盖文件原有的内容

>> 表示追加，会将内容追加到已有文件的末尾

将 echo 输出的信息保存到 1.txt 里echo Hello Python > 1.txt
将 tree 输出的信息追加到 1.txt 文件的末尾tree >> 1.txt

"""

#99、正则表达式匹配出<html><h1>www.itcast.cn</h1></html>
#前面的<>和后面的<>是对应的，可以用此方法


"""
labels = [
    "<html><h1>www.itcast.cn</h1></html>",
    "<html><h1>www.itcast.cn</h2></html>"
    ]
import re
for label in labels:

    ret = re.match(r'<(\w*)><(\w*)>.*?</\2></\1>',label)
    if ret:
        print(ret.group())
    else:
        print('错误的是',label)


<html><h1>www.itcast.cn</h1></html>
错误的是 <html><h1>www.itcast.cn</h2></html>

"""

#100、python传参数是传值还是传址？
"""
Python中函数参数是引用传递（注意不是值传递）。
对于不可变类型（数值型、字符串、元组），因变量不能修改，
所以运算不会影响到变量自身；而对于可变类型（列表字典）来说，
函数体运算可能会更改传入的参数变量。

"""