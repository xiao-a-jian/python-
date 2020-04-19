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

# 写操作
l = [
    ('Dave', 20, 'm', 15000, '1995-6-6'),
    ('Baron', 25, 'm', 16000, '1996-6-6')
]
try:
    sql = "insert into person (name,age,sex,salary,hire_date) values (%s,%s,%s,%s,%s);"
    cur.executemany(sql, l)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()
