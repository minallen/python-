from matplotlib import pyplot as plt
import random,matplotlib
from pylab import mpl


'''
如果列表a表示10点到12点的每一分钟的气温,如何绘制折线图观察每分钟气温的变化情况?


y = [random.randint(20,35) for i in range(120)]

x = range(0,120)

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)



#调整步长为10
_x = list(x)[::10]

xticks = ["hello,{}".format(i) for i in _x]

plt.xticks(_x,xticks)



windows linux下用matplotlib时显示中文：

第一种：
import matplotlib

font = {'family' : 'MicroSoft YaHei',
  'weight' : 'bold',
  'size'   : 'larger'}

matplotlib.rc("font",**font)


第二种：
    #对于linux，在fname='' 的位置上写：fc-list 查看到的中文的字体的名字
    # my_font = font_manager.FontProperties(fname=r"C:\Windows\Fonts\MicrosoftYaHei")
'''



y = [random.randint(20,35) for i in range(120)]
x = range(0,120)

plt.figure(figsize=(20,8),dpi=80)



mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

plt.plot(x,y)


_x = list(x)[::3]
xticks = ["10点{}分".format(i) for i in range(60)]
xticks += ["11点{}分".format(i) for i in range(60)]

#_x,xticks[::3] 的步长要保持一直才行
#plt.xticks(_x,xticks[::3])

#rotation=45 ,旋转45度
plt.xticks(_x,xticks[::3],rotation=45)


#添加注释
plt.xlabel("时间")
plt.ylabel("温度 单位(°C)")
plt.title("温度-时间折线图")




plt.show()

















