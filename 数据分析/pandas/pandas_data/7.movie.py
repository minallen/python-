import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import random,matplotlib
from pylab import mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


#读取文件
file_path = "IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

#先看下数据的整体信息
# print(df.info())
# print("*"*100)
#看下数据的第一行
# print(df.head(1))


#问题：呈现rating，runtime的分布情况
#选择图形：直方图

#准备数据
runtime_data = df["Runtime (Minutes)"].values   # 类型是 ndarray
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()


#组距，分钟
d = 5
#计算组数

print(max_runtime - min_runtime)        # 125

num_bins = (max_runtime - min_runtime) // d


#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.hist(runtime_data,num_bins)

#调整x轴刻度
plt.xticks(range(min_runtime,max_runtime+5,5))

plt.show()


