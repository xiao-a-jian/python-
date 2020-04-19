"""
web server
提供一个服务端使用类
展示自己的简单网页
"""
from socket import *
from select import select
import re


# 主体功能
class HTTPServer:
    def __init__(self, host='0.0.0.0', port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        # 多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 创建套接字和地址绑定工作
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sockfd.bind(self.address)

    # 启动服务 准备接收链接的过程
    def start(self):
        self.sockfd.listen(3)
        print("Listen the port %s" % self.port)
        # select TCP并发服务
        self.rlist.append(self.sockfd)
        while True:
            # 对IO进行监控
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            # 遍历列表分情况讨论
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("connect from", addr)
                    # 添加客户端链接套接字作为监控对象
                    c.setblocking(False)
                    self.rlist.append(c)
                else:
                    self.handle(r)

    #
    def handle(self, connfd):
        # 接收客户端请求
        data = connfd.recv(1024).decode()
        # print(data)
        pattern = r"[A-Z]+\s+(/\S*)"
        try:
            info = re.match(pattern, data).group(1)
        except:
            self.rlist.remove(connfd)
            connfd.close()
            return
        else:
            # 根据请求整理数据，发送给客户端
            self.get_html(connfd, info)

    # 网页处理
    def get_html(self, connfd, info):
        if info == "/":
            filename = self.html + '/index.html'
        else:
            filename = self.html + info
        try:
            f = open(filename, 'rb')
        except:
            response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
            response_headers += "Content-Type:text/html\r\n"
            response_headers += "\r\n"
            response_content = "<h1>Sorry.....</h1>"
            response = response_headers + response_content
        else:
            response_content = f.read()
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers += "Content-Type:text/html\r\n"
            response_headers += "Content-Length:%d\r\n"%len(response_content)
            response_headers += "\r\n"

            response = response_headers.encode() + response_content
        finally:
            connfd.send(response)


if __name__ == '__main__':
    """
    通过HTTPServer类快速搭建服务
    展示static一组网页
    """

    # 需要使用者提供：网络地址 网页位置
    host = "0.0.0.0"
    port = 8000
    dir = "./static"

    # 实例化对象
    httpd = HTTPServer(host=host, port=port, html=dir)

    #调用方法启动服务
    httpd.start()




