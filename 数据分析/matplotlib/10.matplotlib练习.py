from matplotlib import pyplot as plt
import random,matplotlib
from pylab import mpl


'''
根据条形图绘制直方图
'''


mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#x轴刻度
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
#组距
width = [5,5,5,5,5,5,5,5,5,15,30,60]
#y轴刻度
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]


# print(len(interval),len(width),len(quantity))   #12 12 12


plt.figure(figsize=(20,8),dpi=80)

#width默认是0.8，设置成1变成直方图
plt.bar(range(12),quantity,width=1)

#设置x轴刻度
x_tz = [i-0.5 for i in range(13)]

# 这里 + [150] 是因为让 x轴最后一个刻度 + 组距
xticks_labels = interval + [150]

#设置x轴刻度
plt.xticks(x_tz,xticks_labels)

plt.grid()

plt.show()

