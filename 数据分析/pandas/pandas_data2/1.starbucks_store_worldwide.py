import pandas as pd
import numpy as np


file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)

# print(df.info())
# print("*"*50)
# print(df.head(3))


#统计中国每个省店铺的数量
'''
china_data = df[df["Country"]=="CN"]
groupd = china_data.groupby(by="State/Province")["Brand"].count()
print(groupd)

'''


#数据按照多个条件进行分组（结果是series类型，但是会有两个索引）
grouped1 = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped1)
# print(type(grouped1))        #<class 'pandas.core.series.Series'>


#获取上面分组之后的数据
# print(df.groupby(by=["Country","State/Province"])["Country"].count())


#数据按照多个条件进行分组（让返回结果是 dataframe 类型）
grouped2 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped2)
print(type(grouped2))       #<class 'pandas.core.frame.DataFrame'>













