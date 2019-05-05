

import random
import numpy as np

#保留小数
# print(round(random.random(),2))
# print("%.2f"%random.random())
# print("%.3f"%random.random())

t1 = np.zeros((2,3))
# print(t1)

t2 = np.ones((2,5))
# print(t2)

t3 = np.eye(6)
# print(t3)

t4 = np.arange(8).reshape(2,4)
# print(t4.max())

# print("*"*10)

# axis=0  一列一列的看，然后竖着相互比较
# t5 = np.argmax(t4,axis=0)
# print(t5)

# axis=1 一行一行的看，然后横着相互比较
# t5 = np.argmax(t4,axis=1)
# print(t5)

np.random.seed(1)
tt = np.random.randint(0,20,(3,4))
print(tt)