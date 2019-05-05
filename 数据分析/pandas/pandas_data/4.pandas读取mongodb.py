import pandas as pd
import numpy as np
from pymongo import MongoClient
import json

client = MongoClient(host="192.16.16.1",port=27017)

collection = client["douban"]["tv1"]

data = collection.find()

data_list = []

for i in data:
    temp = {}
    temp["info"] = i["info"]
    temp["rating_count"] = i["rating"]["count"]
    temp["rating_value"] = i["rating"]["value"]
    temp["title"] = i["title"]
    temp["country"] = i["tv_category"]
    temp["directors"] = i["directors"]
    temp["actors"] = i["actors"]
    data_list.append(temp)


# print(data_list)

# with open("d.csv","a",encoding="utf-8") as f:
#     for i in data_list:
#         f.write(json.dumps(i,ensure_ascii=False))
#         f.write("\n")
#     print("ok")

# df = pd.DataFrame(data_list)
# print(df)

#显示前两行
# print(df.head(1))

# print("*"*30)

#显示后两行
# print(df.tail(1))


#显示df 的概览
# print(df.info())
# print(df.describe())        #只能统计数字
