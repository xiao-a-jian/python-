from socket import *
from time import sleep

s = socket()
s.connect(('127.0.0.1', 8888))

f = open('w.jpg', 'rb')

while True:
    data = f.read(1024)
    # if not data:
    #   break
    if not data:
        # 　文件已经读完
        sleep(0.2)  # 让上一个消息被接收完
        s.send(b'##')
        break
    s.send(data)
f.close()
s.close()

