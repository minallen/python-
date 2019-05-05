# a = 1
#print(id(a))

# a = 2
#print(id(a))
#140730178986832
#140730178986864

# lis1 = [1,2]
# lis1 = [3,4]
# # print(id(lis1))
# # print(id(lis1))
#
# class f:
#     def __str__(self):
#         return 'ok'
# f = f()
# print(f.__str__())
#
# a = (i for i in range(3))
# print(list(a))




# print("\n".join("\t".join(["%s * %s = %s" %(x,y,x*y) for y in range(1,x+1)]) for x in range(1,10)))

import datetime
a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(a)    #2019-04-16 17:27:33
