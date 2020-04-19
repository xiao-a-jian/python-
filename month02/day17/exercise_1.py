"""
练习: 编写一个程序,将index.html这个网页通过浏览器访问并且展示
"""

from socket import *


def request(c):
    data = c.recv(2048)
    print(data.decode())

    f = open("index.html")
    info = f.read()
    f.close()

    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type:text/html\r\n"
    response += "\r\n"
    response += info

    c.send(response.encode())
    c.close()


def main():
    s = socket()
    s.bind(("0.0.0.0", 8000))
    s.listen(3)

    while True:
        c, addr = s.accept()
        request(c)
        

if __name__ == '__main__':
    main()






















