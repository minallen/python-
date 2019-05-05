from pymongo import MongoClient
'''
连接mongodb数据库之后，不用断开操作，还有redis数据库页不用断开操作
'''

client = MongoClient(host="192.16.16.1",port=27017)

collection = client["test"]["try_mongo2"]

# data_list = [{"_id":i,"name":"py{}".format(i)} for i in range(100)]
#
# collection.insert_many(data_list)

ret = collection.find()
ret = list(ret)

ret = [i for i in ret if i["_id"]%10==0 and i["_id"]!=0]
print(ret)

