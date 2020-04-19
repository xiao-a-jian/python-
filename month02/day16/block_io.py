"""
非阻塞IO演示
套接字io
"""

from socket import *
from time import ctime, sleep

f = open("net.log", 'a+')
sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(3)

# sockfd.setblocking(False)

sockfd.settimeout(2)

while True:
    print("wait...")
    try:
        connfd, addr = sockfd.accept()
        print("from", addr)
    except timeout as e:
        f.write("%s : %s\n" % (ctime(), e))
        f.flush()
    except BlockingIOError as e:
        sleep(3)
        f.write("%s : %s\n" % (ctime(), e))
        f.flush()
    else:
        data = connfd.recv(1024)
        print(data)
