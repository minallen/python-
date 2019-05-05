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

#读取数据
tmp_list = df["Genre"].str.split(",").tolist()  # [[],[],[]]
genre_list = list(set([j for i in tmp_list for j in i]))


#构造全为0 的数据
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)


#给每个电影出现分裂的位置赋值1

#遍历每一行
for i in range(df.shape[0]):
    #获取一行多列     zero.df.loc[0,["",""]] = 1
    zero_df.loc[i,tmp_list[i]] = 1

# print(zero_df.head(3))

#统计每个分类电影的数量和
genre_count = zero_df.sum(axis=0)
print(genre_count)

#排序
genre_count = genre_count.sort_values()


# x轴和y轴
_x = genre_count.index
_y = genre_count.values

#画图
plt.figure(figsize=(20,8),dpi=80)
#条形图
plt.bar(range(len(_x)),_y,width=0.4,color="orange")
#调整x轴刻度 两个参数：刻标(用来指定范围) 和 刻度标签(用来显示)
plt.xticks(range(len(_x)),_x)


plt.show()





