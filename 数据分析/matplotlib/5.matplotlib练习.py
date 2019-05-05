from matplotlib import pyplot as plt
import random,matplotlib
from pylab import mpl



mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False



y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1,32)
x_10 = range(51,82)


#设置图片大小和清晰度
plt.figure(figsize=(20,8),dpi=80)


#绘制散点图,添加图例
plt.scatter(x_3,y_3,label="3月份")
plt.scatter(x_10,y_10,label="10月份")




#调整x轴刻度
x_tz = list(x_3) + list(x_10)
xticks_tz = ["3月{}日".format(i) for i in x_3]
xticks_tz += ["10月{}日".format(i) for i in x_10]
plt.xticks(x_tz[::3],xticks_tz[::3],rotation=45)


#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("北京2016年3,10月份每天白天的最高气温")

#调出图例
plt.legend()

#绘制网格 alpha=0.1用来设置透明度
# plt.grid(alpha=0.7)

plt.show()











