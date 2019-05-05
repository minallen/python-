import numpy as np

from matplotlib import pyplot as plt
import random,matplotlib
from pylab import mpl


mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


gb_file_path = "GB_video_data_numbers.csv"
# us_file_path = "US_video_data_numbers.csv"

gb_file = np.loadtxt(gb_file_path,delimiter=",",dtype="int")
# us_file = np.loadtxt(us_file_path,delimiter=",",dtype="int")

#喜欢数大于50万的点非常少，所以不需要进行统计
#所以，从原始的数据当中选择喜欢数小于 50万的数
#这里要注意：喜欢数和评论数要一致的选择
gb_file = gb_file[gb_file[:,1]<=500000]


gb_file_comments = gb_file[:,-1]
gb_file_like = gb_file[:,1]

plt.figure(figsize=(20,8),dpi=80)

#x轴为喜欢
#y轴为评论
plt.scatter(gb_file_like,gb_file_comments)

plt.show()






