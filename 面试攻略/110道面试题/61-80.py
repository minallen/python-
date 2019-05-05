import time

#61、简述同源策略
'''
同源策略需要同时满足以下三点要求： 
1）协议相同 
2）域名相同 
3）端口相同 

http:www.test.com与https:www.test.com 不同源——协议不同 

http:www.test.com与http:www.admin.com 不同源——域名不同 

http:www.test.com与http:www.test.com:8081 不同源——端口不同

只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”

'''

#62、简述cookie和session的区别
'''
1，session 在服务器端，cookie 在客户端（浏览器）
2、session 的运行依赖 session id，而 session id 是存在 cookie 中的
也就是说，如果浏览器禁用了 cookie ，同时 session 也会失效
3、cookie安全性比session差

'''

#63、简述多线程、多进程
'''
进程：
    1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
    2、稳定性好，如果一个进程崩溃，不影响其他进程
    3、进程消耗资源大，开启的进程数量有限制
    
线程：
    1、CPU进行资源分配和调度的基本单位
    2、线程是进程的一部分，是比进程更小的能独立运行的基本单位
    3、一个进程下的多个线程可以共享该进程的所有资源
    4、如果IO操作密集，则可以多线程运行效率高        
    5、缺点是如果一个线程崩溃，都会造成进程的崩溃
    
应用：
    1、IO密集的用多线程，在用户输入，sleep 时候，
    可以切换到其他线程执行，减少等待的时间

    2、CPU密集的用多进程，因为假如IO操作少，用多线程的话，
    因为线程共享一个全局解释器锁，
    当前运行的线程会霸占GIL，其他线程没有GIL，
    就不能充分利用多核CPU的优势
'''


#64、简述any()和all()方法
'''
any():只要迭代器中有一个元素为真就为真
all():迭代器中所有的判断项返回都是真，结果才为真
python中什么元素为假？
    0，空字符串，空列表、空字典、空元组、None, False
    
'''

#65
'''
IOError、AttributeError、ImportError、IndentationError、

IndexError、KeyError、SyntaxError、NameError分别代表什么异常?

答：
    IOError：输入输出异常

    AttributeError：试图访问一个对象没有的属性
    
    ImportError：无法引入模块或包，基本是路径问题
    
    IndentationError：语法错误，代码没有正确的对齐
    
    IndexError：下标索引超出序列边界
    
    KeyError:试图访问你字典里不存在的键
    
    SyntaxError:Python代码逻辑语法出错，不能执行
    
    NameError:使用一个还未赋予对象的变量

'''

#66、python中copy和deepcopy区别
'''
    1、复制不可变数据类型，不管copy还是deepcopy,都是同一个地址
    2、复制的值是可变对象（列表和字典）:
        浅拷贝copy有两种情况：
            1.复制的对象中无 复杂 子对象, 原来值的改变并不会影响浅复制的值
            同时浅复制的值改变也并不会影响原来的值(也就是互不影响)
            
            2.复制的对象中有 复杂 子对象，（例如列表中的一个子元素是一个列表），
            改变原来的值 中的复杂子对象的值  ，会影响浅复制的值。
            
        深拷贝deepcopy：完全复制独立，包括内层列表和字典    
            
'''

#67、列出几种魔法方法并简要介绍用途

'''
__init__:对象初始化方法

__new__:创建对象时候执行的方法，单列模式会用到

__str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

__del__:删除对象执行的方法

class f:
    def __str__(self):
        return 'ok'
f = f()
print(f.__str__())

'''

#68、C:Users y-wu.junyaDesktop>python 1.py 22 33命令行启动程序并传参，
# print(sys.argv)会输出什么数据？
'''
输出文件名和参数构成的列表
['1.py','22','33']
'''

#69、请将[i for i in range(3)]改成生成器
'''
a = (i for i in range(3))
print(list(a))
print(type(a))

'''

#70、a = "  hehheh  ",去除收尾空格
'''
a = "  hehheh  "
a = a.strip()
print(a)

'''

#71、举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
'''
list=[0,-1,3,-10,5,9]
list.sort(reverse=False)
print('从小到大的顺序：',list)

ret = sorted(list,reverse=False)
print(ret)

总结：
    1.sort是在原基础上修改，没有返回值
    2.sorted有返回值，是个新的列表
'''

#72、对list排序
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
'''
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
fo = sorted(foo,key=lambda x:x,reverse=False)
print(fo)       #[-20, -5, -4, -4, -2, 0, 2, 4, 8, 8, 9]

'''

#73、使用lambda函数对list排序
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为
#[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小

'''
传两个条件，x<0和abs(x)
当i<0的时候，按照绝对值大小进行排序，i>0的时候，正常排序

foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
fo = sorted(foo,key=lambda i:(i<0,abs(i)))
print(fo)
'''

#74、列表嵌套字典的排序，分别根据年龄和姓名排序

'''
foo = [
    {"name":"zs","age":19},
    {"name":"ll","age":54},
    {"name":"wa","age":17},
    {"name":"df","age":23}
]

#年龄
f1 = sorted(foo,key=lambda x:x["age"])
print('按照年龄排序',f1)

#姓名
f2 = sorted(foo,key=lambda x:x["name"])
print('按照姓名排序',f2)

'''


#75、列表嵌套元组，分别按字母和数字排序

'''
foo = [
    ("zs",19),
    ("ls",54),
    ("wa",17),
    ("df",23),

]

#按字母
f1 = sorted(foo,key=lambda i:i[0])
print(f1)

#按数字
f2 = sorted(foo,key=lambda i:i[1])
print(f2)

'''


#76、列表嵌套列表排序，年龄数字相同怎么办？
'''
foo = [
    ["zs",19],
    ["ls",54],
    ["wa",17],
    ["df",19],
]

f = sorted(foo,key=lambda x:(x[1],x[0]))
print(f)        #[['wa', 17], ['df', 19], ['zs', 19], ['ls', 54]]

注意：lambda函数中，如果发生了相同的条件，则根据后面的条件进行排序

'''

#77、根据键对字典排序（方法一，zip函数）
'''
dic = {"name":"zs","sex":"man","city":"bj"}

#字典转化为列表，并且嵌套元祖
foo = zip(dic.keys(),dic.values())
f = [i for i in foo ]
#print(f)    #[('name', 'zs'), ('sex', 'man'), ('city', 'bj')]
#按照键排序
f_sort = sorted(f,key=lambda i:i[0])    
new_dic = {i[0]:i[1] for i in f_sort}
print('new_dic:',new_dic)   #{'city': 'bj', 'name': 'zs', 'sex': 'man'}

--------------
78.题（方法二）

dic_sort = sorted(dic.items(),key=lambda i:i[0])
# print(dic_sort)     #[('city', 'bj'), ('name', 'zs'), ('sex', 'man')]
new_dic_sort = {i[0]:i[1] for i in dic_sort}
print(new_dic_sort)

这两种方法效果相同！
'''


#79、列表推导式、字典推导式、生成器

'''
import random

list1 = [i for i in range(6)]
print(list)     #[0, 1, 2, 3, 4, 5]

dic = {i:random.randint(1,6) for i in ["a","b","c"]}
print(dic)

a = (i for i in range(6))
print(list(a))      #[0, 1, 2, 3, 4, 5]
print(a)        #<generator object <genexpr> at 0x000001696375C408>

'''

#80、最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
'''
s = ["ab","abc","a","dgdf"]

#第一种方法
s_sort = sorted(s,key=lambda i:len(i))
print(s_sort)

#第二种方法
s.sort(key=len,reverse=True)
print(s)

'''