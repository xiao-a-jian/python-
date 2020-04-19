"""
存储二进制文件
"""
import pymysql

# 链接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 创建游标（调用sql语句，获取执行结果）
cur = db.cursor()

# 存入文件
# f = open('ww.jpg', 'rb')
# data = f.read()
#
# try:
#     sql = "update person set image=%s where name='Tom';"
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()

# 提取文件
sql = "select image from person where name='Tom';"
cur.execute(sql)
data = cur.fetchone()[0]
f = open("w.jpg",'wb')
f.write(data)

f.close()
# 关闭游标和数据库
cur.close()
db.close()
