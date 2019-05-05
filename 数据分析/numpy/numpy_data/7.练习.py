import numpy as np

from matplotlib import pyplot as plt
import random,matplotlib
from pylab import mpl



mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

gb_file_path = "GB_video_data_numbers.csv"
us_file_path = "US_video_data_numbers.csv"

gb_file = np.loadtxt(gb_file_path,delimiter=",",dtype="int")
us_file = np.loadtxt(us_file_path,delimiter=",",dtype="int")


#获取评论数的一列
us_file_comments = us_file[:,-1]

#第一次绘图之后，发现评论数到 比 5000 大的数据很少，几乎没有，所以就去掉5000以后的数据
#然后再调整组距，从10000 调整为 50
us_file_comments = us_file_comments[us_file_comments<=5000]

# print(us_file_comments.max(),us_file_comments.min())

#组距
d = 50

num_bins = (us_file_comments.max() - us_file_comments.min()) // d

plt.figure(figsize=(20,8),dpi=80)

plt.hist(us_file_comments,num_bins)

plt.show()







