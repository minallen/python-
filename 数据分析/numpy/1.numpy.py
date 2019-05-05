import numpy as np



#使用numpy.array生成数组

t1 = [1,2,3]
t1 = np.array(t1)
print(t1)           #[1 2 3]
print(type(t1))     #<class 'numpy.ndarray'>

t2 = np.array(range(6))
print(t2)           #[0 1 2 3 4 5]


t3 = np.arange(4,10,2)
print(t3)           #[4 6 8]







