"""
学生信息录取
服务端
"""
from socket import *
import pymysql


class Database:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="stu",
                                  charset="utf8")

        # 创建游标（调用sql语句，获取执行结果）
        self.cur = self.db.cursor()

    # 关闭游标和数据库
    def close(self):
        self.cur.close()
        self.db.close()

    def insert_data(self, list_):
        sql = "insert into cls (name,age,sex,score)value(%s,%s,%s,%s)"
        try:
            self.cur.execute(sql, list_)
            self.db.commit()
        except:
            self.db.rollback()


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 8888))
    db = Database()  # 实例化对象
    while True:
        try:
            data, addr = udp_socket.recvfrom(200)
            info = data.decode().split(' ')
            db.insert_data(info)

        except KeyboardInterrupt:
            break
    db.close()
    udp_socket.close()
    print("服务结束")

main()
