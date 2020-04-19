"""
机器人服务端
"""
from socket import *
chat = {
    "你好":"你好！",
    "你叫什么？":"我叫小美！",
    "你几岁了？":"我２岁了！"
}

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
    data = connect_socket.recv(1024).decode()
    if data.encode() == '##':
        break
    elif data in chat:
        connect_socket.send(chat[data].encode())
    else:
        connect_socket.send("人家还小，听不懂啦！".encode())


connect_socket.close()
tcp_socket.close()
