import numpy as np


gb_file_path = "GB_video_data_numbers.csv"
us_file_path = "US_video_data_numbers.csv"

# gb_file = np.loadtxt(gb_file_path,delimiter=",",dtype="int")
us_file = np.loadtxt(us_file_path,delimiter=",",dtype="int")

print(us_file)

print("*"*100)

'''
import numpy as np


gb_file_path = "GB_video_data_numbers.csv"
us_file_path = "US_video_data_numbers.csv"

# gb_file = np.loadtxt(gb_file_path,delimiter=",",dtype="int")
us_file = np.loadtxt(us_file_path,delimiter=",",dtype="int")

print(us_file)

print("*"*100)


# 取第三行
print(us_file[2])


# 取第三行之后的所有行
print(us_file[2:])


# 取不连续的多行
print(us_file[[0,1,4]])

# 逗号前面写行，逗号后面写列，
#用冒号代替的话，表示行或者列都要
print(us_file[1,:])


#第三行以后的所有数据
print(us_file[2:,:])

#不连续的多行数据
print(us_file[[0,1,3],:])


获取第一列
print(us_file[:,0])

获取连续的多列
print(us_file[:,2:])

获取不连续的多列
print(us_file[:,[0,2]])

获取第三行，第四列的值
print(us_file[2,3])

获取多行和多列的值，比如取第三行到第五行，第二列到第四列的结果
本质：取到的是行和列交叉点的位置
print(us_file[2:5,1:4])


获取多个不相邻的点
[0,2] 表述行号
[0,1] 对应行号表示列号
就是 0,0  2,1  对应的数字
print(us_file[[0,2],[0,1]])

'''

























