"""
tcp服务端
"""
from socket import *

# 创建套接字
tcp_socket = socket(AF_INET, SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("192.168.89.142", 8888))

# 将套接字设置为监听套接字
tcp_socket.listen(5)

print("等待客户端链接...")
# 等待客户端链接
connect_socket, addr = tcp_socket.accept()
print("链接了", addr, "客户端")  # 打印地址

# 接收消息
while True:
    data = connect_socket.recv(20)
    if data.decode() == '##':
        break
    print("接收到：", data.decode())
    n = connect_socket.send(b"thanks")  # 发送字节串
    print("发送了%d bytes" % n)

connect_socket.close()
tcp_socket.close()
