import time

#21、列出python中可变数据类型和不可变数据类型，并简述原理
'''
不可变数据类型：int型、字符串型str和元组tuple

不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，内存中会有新地址，
而对于相同的值的不同对象，在内存中则只有一个地址

总结：变量的值不变，则内存地址不变
a = 1
b = 1
print(id(a))    140703722169168
print(id(b))    140703722169168
-------------
可变数据类型：列表list和字典dict；

允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，
只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化
不过对于相同的值的不同对象，在内存中都有自己的地址

总结：变量名不变，则内存地址不变

a = [1,2]
b = [1,2]
print(id(a))        1194884883080
print(id(b))        1194884883144
'''

#22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"

'''
s = "ajldjlajfdljfddd"
s = set(s)
s = list(s)
s.sort(reverse=False)
s = "".join(s)
#s = str(s)      #['a', 'd', 'f', 'j', 'l']
print(s)         #adfjl
注意：
    1.字符串去重用set方法
    2.去重之后，必须转化为列表，是因为sort函数只能接收list类型和dict类型的数据
    3.sort方法没有返回值，不要用变量接收
    4.sort之后，用 "".join() 变成字符串
    5.从小到大排列：reverse=False
'''

#23、用lambda函数实现两个数相乘
'''
ret = lambda a,b:a*b
print(ret(3,4))
'''

#24、字典根据键从小到大排序
'''
sort 与 sorted 区别：

    sort 是应用在 list 上的方法，属于列表的成员方法
    sorted 可以对所有可迭代的对象进行排序操作
    list 的 sort 方法返回的是对已经存在的列表进行操作，
    内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
    sort使用方法为ls.sort()，而sorted使用方法为sorted(ls)

    sort(cmp=None, key=None, reverse=False)
    sorted(iterable, cmp=None, key=None, reverse=False)

    reverse：True反序；False 正序
    
print(dic.items())      #[('name', 'zs'), ('age', 18), ('city', '深圳'), ('tel', '1362626627')]

dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
lis = sorted(dic.items(),key=lambda d:d[0],reverse=False)
print(lis)
    
'''

#25、利用collections库的Counter方法统计字符串每个单词出现的次数
# "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
'''
from collections import Counter
s = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
s = Counter(s)
print(s)
'''

#26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，
# 用正则过滤掉英文和数字，最终输出"张三  深圳"
'''
思路：
    1.先用正则找出不符合要求的数据
    2.再根据原始的数据，遍历两个列表，把其中共同的部分删掉
    
import re
a = "not 404 found 张三 99 深圳"
b = a.split(" ")
ret = re.findall('\d+|[a-zA-Z]+',a)
for i in ret:   #['not', '404', 'found', '99']
    if i in b:  #['not', '404', 'found', '张三', '99', '深圳']
        b.remove(i)
bb = " ".join(b)
print(ret)
print(bb)   
--------------------
匹配小数的代码
import re
aa = "not 404 55.66 found 张三 99 深圳"
bb = aa.split(" ")
ret = re.findall('\d+\.?\d*|[a-zA-Z]+',aa)
for i in ret:
    if i in bb:
        bb.remove(i)
cc = " ".join(bb)
print(ret)
print(cc)
 
'''

#27.filter方法求出列表所有奇数并构造新列表，
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = list(filter(lambda x:x%2==1,a))
print(a)        #filter(lambda x:x%2==1,a)
'''

#28、列表推导式求列表所有奇数并构造新列表，
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret = [i for i in a if i%2==1]
print(ret)
'''

#29、正则re.complie作用
'''
re.compile是将正则表达式编译成一个对象，加快速度，并重复使用
text = "apple's price is $9.94,orange's price is $12.5"
#先编译号提取的内容
r_obj = re.compile('\d+\.?\d*')
#直接传入编译内容和文本即可
ret = re.search(r_obj,text)
print(ret.group())
ret2 = re.findall(r_obj,text)
print(ret2)
'''


#30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
'''
a=(1,)
b=(1)
c=("1")
print(type(a))  #typle
print(type(b))  #int
print(type(c))  #str
'''

#31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
'''
l1 = [1,5,7,9]
l2 = [2,2,6,8]
l1.extend(l2)

l1.sort(reverse=False)
print(l1)       #[1, 2, 2, 5, 6, 7, 8, 9]

'''

#32、用python删除文件和用linux命令删除文件方法
'''
python：os.remove(文件名)
linux:       rm  文件名
'''

#33、log日志中，我们需要用时间戳记录error,warning等的发生时间，
# 请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
'''
import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(a)    #2019-04-16 17:27:33

#如果加上星期的话：
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))\
    + '  星期' + str(datetime.datetime.now().isoweekday())
print(a)
'''

#34、数据库优化查询方法
'''
外键，索引，联合查询，选择特定字段等等
'''

#35.请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
'''
pychart、matplotlib
'''

#36、写一段自定义异常代码
'''
def foo():
    try:
        for i in range(6):
            if i > 3:
                raise Exception("数字大于3了")
            print(i)
                
    except Exception as e:
        print(e)
if __name__ == '__main__':
    foo()
'''

#37.正则表达式匹配中，（.*）和（.*?）匹配区别？
'''
（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配

（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
'''

#38.简述Django的orm
'''
ORM，全拼Object-Relation Mapping，意为对象-关系映射
实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，
而不需要修改代码只需要面向对象编程,orm操作本质上会根据对接的数据库引擎，
翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层使用的
是MySQL、Oracle、sqlite....，如果数据库迁移，只需要更换
Django的数据库引擎即可
'''

#39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
'''
l = [[1,2],[3,4],[5,6]]
ll = [j for i in l for j in i]
print(ll)
'''

#40、x="abc",y="def",z=["d","e","f"],
# 分别求出x.join(y)和x.join(z)返回的结果
'''
x="abc"
y="def"
z=["d","e","f"]

m = x.join(y)
print(m)    #dabceabcf

n = x.join(z)
print(n)    #dabceabcf
'''