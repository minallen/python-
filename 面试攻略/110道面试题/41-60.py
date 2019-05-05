import time

#41、举例说明异常模块中try except else finally的相关意义
'''
try..except..else没有捕获到异常，执行else语句
try..except..finally不管是否捕获到异常，都执行finally语句

'''

#42、python中交换两个数值
'''
a=1
b=2
a,b = b,a
print(a)    #2
print(b)    #1

'''

#43、举例说明zip（）函数用法
'''
zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，
返回一个元组的列表。同时将这些序列中并排的元素配对。
zip()参数可以接受任何类型的序列

a = [1,2]
b = [3,4]
ret = [i for i in zip(a,b)]
print(ret)      #[(1, 3), (2, 4)]

A = "ab"
B = "xyz"
ret2 = [i for i in zip(A,B)]
print(ret2)     #[('a', 'x'), ('b', 'y')]

'''

#44、a="张明 98分"，用re.sub，将98替换为100
'''
import re
a="张明 98分"
a = re.sub('\d+','100',a)
print(a)

'''

#45、写5条常用sql语句
'''
#select * from 表名
#show databases
#show tables
#update 表名 set 字段 where id=6
#delete from 表名 where id=6
 
'''

#46、a="hello"和b="你好"编码成bytes类型
'''
a=b"hello"
b="你好".encode()
print(a,b)
print(type(a),type(b))

英文字母直接加上b即可
中文用encode()
'''

#47.[1,2,3]+[4,5,6]的结果是多少？
'''
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)    #[1, 2, 3, 4, 5, 6]
两个列表相加，等价于extend
'''

#48、提高python运行效率的方法
'''
1、使用生成器，因为可以节约大量内存
2、循环代码优化，避免过多重复代码的执行
3、核心模块用Cython  PyPy等，提高效率
4、多进程、多线程、协程
5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，
这样可以减少程序判断的次数，提高效率

'''

#49、简述mysql和redis区别
"""
redis： 内存型非关系数据库，数据保存在内存中，速度快
mysql： 关系型数据库，数据保存在磁盘中，检索的话，
会有一定的Io操作，访问速度相对慢

"""

#50、遇到bug如何处理
'''
1.通过print（）打印,分段检测程序是否有问题
2.如果涉及一些第三方框架，会去查官方文档
3、对于bug的管理与归类总结
4、导包问题、

'''

#51、正则匹配，匹配日期2018-03-20
'''
url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
import re
ret1 = re.findall('\d{4}-\d{2}-\d+',url)
print(ret1)

ret2 = re.findall('dateRange=(.*?)%7C(.*?)&date',url)
print(ret2)

'''

#52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
'''
list=[2,3,5,4,9,6]

def buble_sort(data_list):
    for i in range(len(data_list)-1):
        exchange = False
        for j in range(len(data_list)-1-i):
            if data_list[j] > data_list[j+1]:
                data_list[j],data_list[j+1] = data_list[j+1],data_list[j]
        if not exchange:
            break

if __name__ == '__main__':
    data_list = list
    buble_sort(data_list)
    print(data_list)    #[2, 3, 4, 5, 6, 9]

'''

#53、写一个单列模式
'''
还没有搞设计模式
'''

#54、保留两位小数
'''
待解决

'''

#55、求三个方法打印结果

#56、列出常见的状态码和意义
'''
200 OK 
请求正常处理完毕

303 See Other 
临时重定向，期望使用GET定向获取

403 Forbidden 
请求资源被拒绝

404 Not Found 
无法找到请求资源（服务器无理由拒绝）

500 Internal Server Error 
服务器故障或Web应用故障

'''

#57、分别从前端、后端、数据库阐述web项目的性能优化
'''
前端优化：

1、减少http请求、例如制作精灵图

2、html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差


后端优化：

1、缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。

2、异步方式，如果有耗时操作，可以采用异步，比如celery

3、代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况



数据库优化：

1、如有条件，数据可以存放于redis，读取速度快

2、建立索引、外键等

'''

#58、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}

'''
dic = {"name":"zs","age":18}

del dic["name"]
print(dic)      #{'age': 18}

v = dic.pop("name")
print(v)        #zs
print(dic)      #{'age': 18}  

'''

#59、列出常见MYSQL数据存储引擎
'''
InnoDB：
    支持事务处理，支持外键,支持崩溃修复能力和并发控制。
    如果需要对事务的完整性要求比较高（比如银行），要求实现并发控制（比如售票），
    那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，
    因为支持事务的提交（commit）和回滚（rollback）。 
    
MyISAM：
     插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，
     那么选择MyISAM能实现处理高效率。
     如果应用的完整性、并发性要求比 较低，也可以使用。
     
MEMORY： 
       所有的数据都在内存中，数据的处理速度快，但是安全性不高。
       如果需要很快的读写速度，对数据的安全性要求较低，可以选择MEMOEY。
       它对表的大小有要求，不能建立太大的表。
       所以，这类数据库只使用在相对较小的数据库表。    
'''

#60、计算代码运行结果，zip函数历史文章已经说了，
# 得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]

'''

A = zip(("a","b","c","d","e"),(1,2,3,4,5))
A0 = dict(A)    #A0 {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = range(10)
A2 = [i for i in A1 if i in A0]     # []
A3 = [A0[s] for s in A0]        # [1, 2, 3, 4, 5]

print("A0",A0)

print(list(zip(("a","b","c","d","e"),(1,2,3,4,5))))

print(A2)

print(A3)


ret1 = dict([["name","zs"],["age",18]])
print(ret1)

ret2 = dict([("name","zs"),("age",18)])
print(ret2)

'''
