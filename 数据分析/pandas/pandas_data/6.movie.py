import numpy as np
import pandas as pd

file_path = "IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)


# print(df.info())

# print(df.head(1))

#获取平均分
print(df["Rating"].mean())

#获取导演人数
# print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))

#获取演员的人数
actors_lists = df["Actors"].str.split(", ").tolist() #两层列表
actors_list = [j for i in actors_lists for j in i]
actors_num = len(set(actors_list))
print(actors_num)



