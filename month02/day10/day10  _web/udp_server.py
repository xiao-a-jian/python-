"""
udp　服务端
"""

from socket import *

# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("127.0.0.1", 8888))


# 消息传输
while True:
    print("等待接收...")
    data, addr = udp_socket.recvfrom(20)
    print("接收到：", addr, data.decode())
    # 给客户端回发
    udp_socket.sendto("收到请求".encode(), addr)



udp_socket.close()
