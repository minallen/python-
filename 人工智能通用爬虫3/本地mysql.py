import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='bam940602', db='fitbit_new')

#cursor = conn.cursor()

#-----------------------------------------------------
#返回结果用字典形式表示
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


#sql="create table test(id int,name VARCHAR (20))"

#cursor.execute(sql)

#cursor.execute("insert into test VALUES (1,'alex'),(2,'tom')")

#-----------------------------------------------------
# cursor.execute("select * from test")
# data = cursor.fetchall()
# print(data)

#-----------------------------------------------------
cursor.execute("select * from test")
data = cursor.fetchall()
print(data)


conn.commit()
cursor.close()

conn.close()







