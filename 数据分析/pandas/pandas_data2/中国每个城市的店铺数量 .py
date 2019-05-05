import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from pylab import mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


file_path = "./starbucks_store_worldwide.csv"

#读取文件
df = pd.read_csv(file_path)

#读取字段
df = df[df["Country"] == "CN"]

#问题：使用matplotlib呈现出店铺总数排名前10的国家

#准备数据   ascending=False :使得排序为降序
data1 = df.groupby(by="City")["Brand"].count().sort_values(ascending=False)[:25]

_x = data1.index
_y = data1.values

#画图
# plt.figure(figsize=(20,8),dpi=80)
plt.figure(figsize=(20,12),dpi=80)

#先画图，然后再调整x轴或y轴刻度
# plt.bar(range(len(_x)),_y,width=0.4,color="orange")

plt.barh(range(len(_x)),_y,height=0.4,color="orange")

# _x 是真正在刻度上显示的内容；range(len(_x)) 是显示的范围
# plt.xticks(range(len(_x)),_x)

plt.yticks(range(len(_x)),_x)

plt.show()


