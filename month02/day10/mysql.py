"""
pymysql 基本流程
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

# 各种数据操作


# 关闭游标和数据库
cur.close()
db.close()
