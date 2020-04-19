"""
客户端
"""
from socket import *

# 访问服务端需要的地址
server_addr = ('127.0.0.1', 8888)


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    while True:
        word = input("输入查询单词：")
        if not word:
            break
        udp_socket.sendto(word.encode(), server_addr)  # 发送单词

        data, addr = udp_socket.recvfrom(1024)
        print("%s: %s" % (word, data.decode()))

    udp_socket.close()

main()

