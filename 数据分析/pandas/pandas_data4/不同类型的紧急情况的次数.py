import pandas as pd
import numpy as np


'''
问题类型：从csv文件中统计 出现某一种情况的次数
'''

def cate_sum():
    '''
    问题：统计出这些数据中不同类型的紧急情况的次数
    思路：
        当title字段中包含cate分类的时候，在全为 0 的数组中 的 对应列的位置上赋值 1 。
        title字段中包含cate分类的时候，即 df["title"].str.contains("cate")
        df["title"].str.contains(cate) 表示 指定zero_df数组的行
        zero_df[cate] 表示指定列

    '''
    file_path = "./911.csv"
    df = pd.read_csv(file_path)
    tmp_list = df["title"].str.split(": ").tolist()
    cate_list = list(set([i[0] for i in tmp_list]))

    # 构造全为 0 的数组
    # df.shape[0]         代表构建数组的总共的行数
    # len(cate_list)      代表列的个数
    # columns=cate_list   代表构建的数组的列的名字的集合
    # pd.DataFrame()      表示最终显示类型是二维数组
    # zero_df.sum(axis=0) 表示一列一列的进行相加
    zero_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
    for cate in cate_list:
        #赋值
        zero_df[cate][df["title"].str.contains(cate)] = 1
    sum_ret = zero_df.sum(axis=0)
    return sum_ret

if __name__ == '__main__':
    ret = cate_sum()
    print(ret)