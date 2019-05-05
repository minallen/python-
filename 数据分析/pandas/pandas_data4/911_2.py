import pandas as pd
import numpy as np

file_path = "./911.csv"
df = pd.read_csv(file_path)

# 不同类型的紧急情况title字段中
# print(df["title"])      #EMS: BACK PAINS/INJURY
# print(df["title"].str.split(": "))    #[EMS, BACK PAINS/INJURY]

tmp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in tmp_list]
#print(cate_list)
#print(np.array(cate_list),len(np.array(cate_list))) #['EMS' 'EMS' 'Fire' ... 'EMS' 'Fire' 'Traffic'] 249737

#构造DataFrame,并且df增加一列 df["cate"]
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))
print(df.head(6))

# print(df.groupby(by="cate").count()["title"])










