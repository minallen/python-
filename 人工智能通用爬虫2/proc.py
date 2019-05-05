'''
正则复习：


一、     re.findall方法:

        1.能匹配出‘\n’:
        ret = re.findall('.','\n',re.S)
        print(ret)
        或者
        ret = re.findall('.','\n',re.DOTALL)
        print(ret)


        2.反斜杠  \
        针对特殊符号：作用是让后面的特殊符号经过前面加上 \ 之后，后面的特殊符号就失去特殊意义了
        ret = re.findall('a\.','a.b')
        print(ret)
        转译的意思是失去特殊意义


        3.中括号 []
        或的意思，只能匹配中括号里的一个值，后面跟上 ‘+’号可以匹配多个
        ret =re.findall('a[bcd]+e','abce')
        print(ret)

        4.问好'?'
        只要出现问号就一个一个的去匹配，返回的结果中有多个逗号隔开
        如果不加问号，返回的结果中只有一个整体，没有逗号隔开


二、
        re.sub方法

        1.把数字用空格替换
        ret = re.sub('\d','','你好11啊！')
        print(ret)



        r的作用：
        只是让'\'失去特殊意义，单纯的作为一个字符，相当于 '\\'
        r的作用就是让一个'\'，变成 '\\'
        a = "a\nb"
        a_len = len(a)
        print(a_len,a[1])

        aa = r"a\nb"
        aa_len = len(aa)
        print(aa_len,aa[1])

        print(r"a\nb"=="a\nb")      #False
        print(r"a\nb"=="a\\nb")     #True


        如何进行非贪婪匹配（就是返回的结果中有多个逗号隔开）：
        .*?   或者  .+?


        ret = re.findall(r"a.*bc",'a\nbc',re.DOTALL)
        print(ret)
        带上括号之后，只是返回括号里匹配的内容
        ret = re.findall(r"a(.*)bc",'a\nbc',re.DOTALL)
        print(ret)


'''


import re

ret = re.findall('.','\n',re.S)
print(ret)
#
# ret = re.findall('.','\n',re.DOTALL)
# print(ret)

# ret = re.findall('a\.','a.b')
# print(ret)


# ret =re.findall('a[bcd]+e','abcde')
# print(ret)

#把数字用空格替换
# ret = re.sub('\d','','你好11啊！')
# print(ret)
#
# a = "a\nb"
# a_len = len(a)
# print(a_len,a[1])
#
# aa = r"a\nb"
# aa_len = len(aa)
# print(aa_len,aa[1])


# print(r"a\nb"=="a\nb")      #False
#print(r"a\nb"=="a\\nb")     #True


# ret = re.findall(r"a.*bc",'a\nbc',re.DOTALL)
# print(ret)
#
#
# ret = re.findall(r"a(.*)bc",'a\nbc',re.DOTALL)
# print(ret)



from lxml import etree


