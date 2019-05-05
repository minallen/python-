import pymysql

'''
连接linux 下的mysql:
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
    FLUSH   PRIVILEGES
'''


conn = pymysql.connect(host='192.16.16.1', port=3306, user='root', passwd='123456', db='test_mysql_to_python')

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
cursor.execute("select * from t1")
data = cursor.fetchall()
print(data)


conn.commit()
cursor.close()

conn.close()









