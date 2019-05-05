import pandas as pd


df = pd.read_csv("./dogNames2.csv")

# print(df.head())
# print(df.info())

#排序,默认是按照升序排序的
#sort_values 按照某一列进行排序 by后面是指定的列
# df = df.sort_values(by="Count_AnimalName")

#降序排序 ascending=False
df = df.sort_values(by="Count_AnimalName",ascending=False)
# print(df.head(10))


#获取前20行
# print(df[:20])

#获取指定的列
# print(df["Row_Labels"])

'''
注意：
    方括号内写数字，表示获取行
    方括号内写字符串，表示获取列
'''
#获取前20行，并且获取Row_Labels 这个列
# print(df[:20]["Row_Labels"])


#找到所有的使用次数超过800的狗的名字
# print(df[df["Count_AnimalName"]>800])

#找到所有的使用次数超过800,并且小于1000的狗的名字
# df[()&()]
print(df[(df["Count_AnimalName"]>800)&(df["Count_AnimalName"]<1000)])




