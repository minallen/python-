import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl


#设置中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


file_path = "./911.csv"
df = pd.read_csv(file_path)

# 转化成pandas提供的时间格式
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
# 把timeStamp变成索引,放在第一列的位置  inplace=True 表示在原有数据上进行操作并替换
df.set_index("timeStamp",inplace=True)
# print(df.head(5))


#统计出911数据中不同月份电话次数的变化情况

#pandas提供了一个resample的方法来帮助我们实现频率转化
#df.resample("M").count()  代表按月进行统计
count_by_month = df.resample("M").count()["title"]
print(count_by_month)


#画图（变化情况：用折线图）

_x = count_by_month.index
_x = [i.strftime("%Y-%m-%d") for i in _x]

_y = count_by_month.values


plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)

#rotation=45 旋转45
plt.xticks(range(len(_x)),_x,rotation=45)

plt.show()


