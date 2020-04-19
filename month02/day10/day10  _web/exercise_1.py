"""
dict字典查询
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
                                  database="dict",
                                  charset="utf8")

        # 创建游标（调用sql语句，获取执行结果）
        self.cur = self.db.cursor()

    # 关闭游标和数据库
    def close(self):
        self.cur.close()
        self.db.close()

    # 查单词
    def find_word(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        mean = self.cur.fetchone()
        if mean:
            return mean[0]
        else:
            return "not found the word"


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 8888))
    db = Database()
    while True:
        try:
            data, addr = udp_socket.recvfrom(50)

            # 实例化对象
            mean = db.find_word(data.decode())  # 查单词
            udp_socket.sendto(mean.encode(), addr)  # 发送结果
        except:
            break
    db.close()
    udp_socket.close()


if __name__ == '__main__':
    main()
