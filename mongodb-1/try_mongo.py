from pymongo import MongoClient


client = MongoClient(host="192.16.16.1",port=27017)

collection = client["test"]["t2019323"]

#collection.insert({"name":"min","age":19})


# data_list = [{"name":"test{}".format(i)} for i in range(1,10)]
# collection.insert_many(data_list)

#查询r 是个对象
r = collection.find({"name":"min"})
#print(r)
#for i in r:
#    print(i)

print(list(r))

