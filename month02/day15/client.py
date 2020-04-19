"""
客户端
"""
from socket import *

server_addr = ("192.168.89.142", 8888)

# 创建tcp套接字  默认参数就是创建tcp套接字
tcp_scoket = socket()

#　发起链接
tcp_scoket.connect(server_addr)

# 发送消息
while True:
    msg = input(">>")
    tcp_scoket.send(msg.encode())
    if msg == '##':
        break

    data = tcp_scoket.recv(20)
    print("从服务器收到：", data.decode())

tcp_scoket.close()

