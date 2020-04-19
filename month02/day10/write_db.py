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
try:
    # sql = "update person set salary=70 where name='lily';"
    # cur.execute(sql)

    sql = "update person set salary=%s where name=%s"
    cur.execute(sql, [13000, "lily"])
    db.commit()
except Exception as e:
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()
