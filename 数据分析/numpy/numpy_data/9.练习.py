import numpy as np



gb_file_path = "GB_video_data_numbers.csv"
us_file_path = "US_video_data_numbers.csv"


#加载数据
gb_file = np.loadtxt(gb_file_path,delimiter=",",dtype="int")
us_file = np.loadtxt(us_file_path,delimiter=",",dtype="int")


'''
添加国家信息
shape[0]:表示行
shape[1]:表示列
'''
#给美国添加一列全为 0 的数据 ,后面的 1 代表列数
zero_data = np.zeros((us_file.shape[0],1)).astype(int)
#给英国添加一列全为 1 的数据
ones_data = np.ones((gb_file.shape[0],1)).astype(int)

#左右拼接
us_data = np.hstack((us_file,zero_data))
gb_data = np.hstack((gb_file,ones_data))


#拼接两组数据(上下拼接)
final_data = np.vstack((us_data,gb_data))
# print(final_data)




