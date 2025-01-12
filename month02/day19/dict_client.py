"""
客户端
"""

from socket import *
import sys


# 服务器地址
ADDR = ('127.0.0.1', 8888)

# 查单词
def do_query(sockfd, name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        msg = "Q %s %s" % (name, word)
        sockfd.send(msg.encode())

        data = sockfd.recv(2048)
        print(data.decode())


def do_hist(sockfd,name):
    msg = "H %s" % name
    sockfd.send(msg.encode())
    while True:
        data = sockfd.recv(1024).decode()
        if data == '##':
            break
        print(data)


# 二级界面
def login(sockfd, name):
    while True:
        print("""
        =============Query=============
        1.查单词     2.历史记录     3.注销
        =================================
        """)
        cmd = input("请输入选项:")
        if cmd == '1':
            do_query(sockfd, name)
        elif cmd == '2':
            do_hist(sockfd, name)
        elif cmd == '3':
            return
        else:
            print("请输入正确选项(1,2,3)!")


def do_register(sockfd):
    while True:
        name = input("User:")
        passwd = input("Passwd:")

        if (' ' in name) or (' ' in passwd):
            print("用户名密码不能有空格")
            continue
        msg = "R %s %s" % (name, passwd)
        sockfd.send(msg.encode())  # 发送请求
        # 等待结果
        data = sockfd.recv(128).decode()
        if data == 'YES':
            print("注册成功")

        else:
            print("注册失败")
        return


# 登录
def do_login(sockfd):

    while True:
        name = input("User:")
        passwd = input("Passwd:")

        msg = "L %s %s" % (name, passwd)
        sockfd.send(msg.encode())  # 发送请求
        # 等待结果
        data = sockfd.recv(128).decode()
        if data == 'YES':
            print("登录成功")
            login(sockfd, name)
        else:
            print("登录失败")
        return
# 网络搭建
def main():
    sockfd = socket()
    sockfd.connect(ADDR)
    # 进入登录界面
    while True:
        print("""
        =============Welcome=============
        1.注册        2.登录        3.退出
        =================================
        """)
        cmd = input("请输入选项:")
        if cmd == '1':
            do_register(sockfd)
        elif cmd == '2':
            do_login(sockfd)
        elif cmd == '3':
            sockfd.send(b'E')
            sys.exit("谢谢使用")

        else:
            print("请输入正确选项(1,2,3)!")


if __name__ == '__main__':
    main()














