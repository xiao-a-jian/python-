"""
数据库查询示例
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

# 查询数据操作
name = input(">>")
sql = "select salary from person where name='%s';" % name
cur.execute(sql)

# sql = "select score from student where name=%s;"
# cur.execute(sql,[name])

# sql = "select name,score from student where name=%s or score>%s;"
# cur.execute(sql,[name,85])

print(cur.fetchone())

# 关闭游标和数据库
cur.close()
db.close()
