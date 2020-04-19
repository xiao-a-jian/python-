"""
数据处理模块
与数据库交互
"""

from socket import *
import pymysql


# 数据库功能类
class Database:
    def __init__(self):
        # 链接数据库
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password='123456',
                                  database="dict",
                                  charset="utf8")

    def cursor(self):
        # 创建游标 (调用sql语句,获取执行结果)
        self.cur = self.db.cursor()

    # 关闭数据库
    def close(self):
        # 关闭游标和数据库
        self.cur.close()
        self.db.close()

    # 注册
    def register(self, name, passwd):
        sql = "select name from user where name=%s;"
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()  # 获取结果看是否查到了
        # 查询带结果不允许注册
        if r:
            return False

        sql = "insert into user (name,passwd) values (%s,%s);"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    # 登录
    def login(self,name,passwd):
        sql = "select name from user where name=%s and passwd=%s;"
        self.cur.execute(sql,[name,passwd])

        # 获取结果
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    def insert_history(self,name,word):
        sql = "select id from user where name=%s;"
        self.cur.execute(sql,[name])
        user_id = self.cur.fetchone()[0]

        sql = "insert into hist (word,user_id) values (%s,%s);"
        try:
            self.cur.execute(sql,[word,user_id])
            self.db.commit()
        except:
            self.db.rollback()


    def query(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        r = self.cur.fetchone()
        if r:
            return r[0]

    def history(self, name):
        sql = "select name,word,time from user inner join hist on user.id=hist.user_id where name=%s order by time desc limit 10;"
        self.cur.execute(sql, [name])

        return self.cur.fetchone()


