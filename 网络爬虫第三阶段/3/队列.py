from queue import Queue


q = Queue(5)

# for i in range(3):  #0,1,2
#     q.put(i)
#     print(q.get())      #q.get() 获取到的是先进到队列里的值


q.put('a')
q.put('b')

print(q.get())