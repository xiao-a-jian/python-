"""
多进程并发模型
服务端
"""
from socket import *
from multiprocessing import Process
from signal import *
import sys
# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


# 应对客户端请求
def handle(connfd):
    # 长期处理
    while True:
        data = connfd.recv(1233)
        if not data:
            break
        print(data)
        connfd.send(b'OK')
    connfd.close()


# tcp套接字
def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(3)

    # 处理僵尸进程
    signal(SIGCHLD, SIG_IGN)

    print("Listen the port 8888")
    # 循环连接客户端
    while True:
        try:
            connfd, addr = sock.accept()
            print("客户端地址：", addr)
        except:
            sys.exit("服务退出")

        # 创建子进程，处理客户端请求
        p = Process(target=handle, args=(connfd,))
        p.daemon = True  # 主服务退出，其他服务也退出
        p.start()


if __name__ == '__main__':
    main()
































