"""
数据库dict
"""
import pymysql
import re

# 链接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

# 创建游标（调用sql语句，获取执行结果）
cur = db.cursor()

# 数据操作
args_list = []
l = open('dict.txt')

for line in l:
    t = re.findall(r"(\w+)\s+(.*)", line)[0]
    args_list.append(t)

sql = "insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql, args_list)
    db.commit()
except:
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()



