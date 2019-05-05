import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from pylab import mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

file_path = "./books.csv"

df = pd.read_csv(file_path)
# print(df.head(1))
# print("*"*50)
# print(df.info())

# 根据 info 里面的信息得知，original_publication_year    9979 是有缺失的，
# 所以，用 notnull 筛选没有缺失的值(即筛选非NAN的数据)

data1 = df[pd.notnull(df["original_publication_year"])]

data1_grouped = data1.groupby(by="original_publication_year").count()["title"]

_x = data1_grouped.index
_y = data1_grouped.values


#画图
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y)
print(len(_x))

plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation=45)

plt.show()

'''
不同年份书的平均评分情况


grouped = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()

# print(grouped)

_x = grouped.index
_y = grouped.values

#画图
plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
print(len(_x))

plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation=45)
plt.show()

'''





