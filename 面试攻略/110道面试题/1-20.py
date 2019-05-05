#1、一行代码实现1--100之和
'''
#print(sum(range(1,101)))
#注意：range(n,m) 能取n,但是不能取m
'''

#2、如何在一个函数内部修改全局变量
'''
a = 1
def change():
    global a
    a = 2
    print(a)
change()
print(a)
注意：用global关键字修改全局变量
'''

#3、列出5个python标准库
"""
1.os 和操作相关的函数
2.sys 用于命令行参数
3.math 数学运算
4.datetime 处理日期时间
5.re 正则
"""

#4、字典如何删除键和合并两个字典
'''
dic1 = {"name":"allen","age":20,"gender":"male"}
dic2 = {"age":22}
删除键"gender"
del dic1["gender"]
print(dic1)
并两个字典
dic1.update(dic2)
print(dic1)
'''

#5.谈下python的GIL
#谈下多线程
#谈下多进程
'''
    1.GIL是什么？
        GIL是python的全局解释器锁。
    2.用来干什么的？
        举个例子：假如一个进程当中有多个线程在执行，当一个线程运行程序的时候
    会霸占python解释器，相当于加了一把锁，GIL。使得该进程内的其他
    线程无法运行，等到该线程运行完才可以运行。
    3.有特殊情况吗？
        如果该线程运行过程中遇到了耗时操作，则解释器解开，使其他线程
    运行。所以在多线程中，线程的运行是有先后顺序的，不是同时运行。
    4.补充：多进程
        多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个
    python解释器，所以多进程可以实现多个进程的同时运行。缺点是
    进程系统资源开销大。                    
'''

#6、python实现列表去重的方法
'''
list1 = [1,2,3,2,1]
s = list(set(list1))
print(s)
注意：set内不能有重复
'''


#7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
'''
都是用来接收函数的参数的
*args:接收非键值对形式的可变数量的参数列表给函数
*kwargs:接不定长度的键值对形式的参数给函数
'''

#8、python2和python3的range（100）的区别
'''
python2 返回的是列表
python3 返回的是迭代器
'''

#9、一句话解释什么样的语言能够用装饰器?
'''
函数能作为参数传递的语言能使用装饰器

# 时间装饰器
def cal_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        # print("%s running time: %s secs." % (func.__name__, start_time - end_time))
        print("%s 函数执行时间是: %s 秒" % (func.__name__, start_time - end_time))
        return result

    return wrapper
'''

#10、python内建数据类型有哪些
'''
int
bool
str
list
dict
tuple
'''

#11、简述面向对象中__new__和__init__区别
'''
__init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数
__init__有一个参数self
__init__不需要返回值

__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别
__new__必须要有返回值，返回实例化出来的实例，
如果__new__创建的是当前类的实例，会自动调用__init__函数

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print('我家的%s,今年%s了,现在在奔跑'%(self.name,self.age))
if __name__ == '__main__':
    dog = Dog('软糖',4)
    dog.run()
'''

#12、简述with方法打开处理文件帮我我们做了什么？
'''
帮我们做finally中f.close()
'''

#13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
'''
list1 = [1,2,3,4,5]
print(list(map(lambda x: x**2 ,list1 )))    #[1, 4, 9, 16, 25]
list2 = list(map(lambda x: x**2 ,list1 ))
list3 = [i for i in list2 if i>10]          #[16, 25]
print(list3)
'''

#14、python中生成随机整数、随机小数、0--1之间小数方法
'''
#随机整数
import random
r1 = random.randint(5,15)
print(r1)
#生成5个随机小数
import numpy as np
r2 = np.random.randn(5)
print(r2)
#0--1之间小数方法
r3 = random.random()
print(r3)
#random.random()不能传递值
'''

#15.避免转义给字符串加哪个字母表示原始字符串？
'''
r , 表示需要原始字符串，不转义特殊字符
'''

#16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
'''
import re
str1 = """<div class="nam">中国</div>"""
ret = re.findall('<div class=".*">(.*?)</div>',str1)
print(ret)
'''

#17、python中断言方法举例
"""
a = 2
assert(a > 1)
print('ok')     #ok
b = 2
assert(b > 3)
print('ok')
"""

#18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
#select distinct name from student

#10个Linux常用命令
'''
ls  cd  pwd  ps  rm  mkdir  gzip  grep  du  df  touch  mv  more tail   
'''

#20、python2和python3区别？列举5个
'''
1.python2 range(1,5) 返回的是列表，python3 返回的是迭代器
2.python2 使用print 既可以用小括号，也可以空格
  python3必须使用小括号
3.python2中使用ascii编码，python3使用utf-8编码
4.python2中如果显示正常中文，引入coding声明，python3不需要
5.python2中是raw_imput函数，python3中是input函数
6.python2中unicode表示字符串序列，str表示字节序列
  python3中str表示字符串序列，byte表示字节序列
'''