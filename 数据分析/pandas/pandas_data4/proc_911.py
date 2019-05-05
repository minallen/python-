import pandas as pd
import numpy as np

file_path = "./911.csv"
df = pd.read_csv(file_path)

# 问题：统计出出这些数据中不同类型的紧急情况的次数

# print(df.info())
# print("="*100)
# print(df.head(1))

# 不同类型的紧急情况title字段中
# print(df["title"])      #EMS: BACK PAINS/INJURY
# print(df["title"].str.split(": "))    #[EMS, BACK PAINS/INJURY]

tmp_list = df["title"].str.split(": ").tolist()
cate_list = list(set([i[0] for i in tmp_list]))
print(cate_list)        #['EMS', 'Traffic', 'Fire']

# 构造全为 0 的数组
# df.shape[0]         代表构建数组的总共的行数
# len(cate_list)      代表列的个数
# columns=cate_list   代表构建的数组的列的名字的集合
# pd.DataFrame()      表示最终显示类型是二维数组
# zero_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)
# print(zero_df)


