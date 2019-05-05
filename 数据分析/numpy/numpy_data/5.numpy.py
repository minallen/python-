import numpy as np


gb_file_path = "GB_video_data_numbers.csv"
us_file_path = "US_video_data_numbers.csv"

# gb_file = np.loadtxt(gb_file_path,delimiter=",",dtype="int")
us_file = np.loadtxt(us_file_path,delimiter=",",dtype="int")


t1 = np.arange(12).reshape(3,4).astype("float")


# 第二行，第三列及之后的列 赋值为nan
t1[1,2:] = np.nan
# print(t1)



def fill_ndarray(t1):
    '''
    :param t1:  最初的数组
    :return:    经过处理的数组，对nan进行赋平均值
    '''
    #一列一列的数
    for i in range(t1.shape(1)):
        #当前的列
        temp_col = t1[:,i]
        #在当前列中统计nan的个数
        nan_num = np.count_nonzero(temp_col!=temp_col)

        #不为0，说明当前这一列中有nan
        if nan_num != 0:                        #有nan的情况
            #把当前这一列不为nan的数据组成数组，temp_not_nan_col
            temp_not_nan_col = temp_col[temp_col==temp_col]
            #计算出当前这一列不为nan的数据的平均值
            # temp_not_nan_col.mean()

            #选中当前为nan的位置，把上面的平均值进行赋值
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()

    return t1








































