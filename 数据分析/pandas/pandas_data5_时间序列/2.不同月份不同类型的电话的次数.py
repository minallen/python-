import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl


#设置中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

#设置图片
plt.figure(figsize=(20, 8), dpi=80)

file_path = "./911.csv"
df = pd.read_csv(file_path)
#转化成pandas提供的时间格式
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

#注意：不同类型的电话是在title字段中的
tmp_list = df["title"].str.split(": ").tolist()  #切割数据
cate_list = [i[0] for i in tmp_list]        #遍历数据获取电话类型放入列表中
#根据电话类型 构造DataFrame,并且在原数据中增加一列 df["cate"]
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))
#把timeStamp变成索引,放在第一列的位置
df.set_index("timeStamp",inplace=True)


#对某一字段进行分组【这里按照 'cate' 字段进行分组】
for group_name,group_data in  df.groupby(by="cate"):

    # pandas提供了一个resample的方法来帮助我们实现频率转化
    # df.resample("M").count()  代表按月进行统计
    count_by_month = group_data.resample("M").count()["title"]

    # 画图（变化情况：用折线图）
    _x = count_by_month.index
    _x = [i.strftime("%Y-%m-%d") for i in _x]
    _y = count_by_month.values

    plt.plot(range(len(_x)), _y, label=group_name)


# rotation=45 旋转45
plt.xticks(range(len(_x)), _x, rotation=45)
#调用图例
plt.legend(loc="best")
plt.show()
