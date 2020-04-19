"""
学生信息录取
客户端
"""
from socket import *

# 访问服务端需要的地址
server_addr = ('127.0.0.1', 8888)


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    while True:
        try:
            print("=========================")
            name = input("名字:")
            age = input('年龄:')
            sex = input('性别:')
            score = input('成绩:')
            data = "%s %s %s %s"%(name,age,sex,score)
            udp_socket.sendto(data.encode(),server_addr)
        except:
            break

    udp_socket.close()

main()

