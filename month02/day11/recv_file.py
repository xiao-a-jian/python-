
from socket import *

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

# 接收数据 -->写入文件
c, addr = s.accept()

f = open("a.jpg", 'wb')

# 循环接收，写入文件
while True:
    data = c.recv(1024)
    # if not data:
    #   break
    if data == b"##":
        break
    f.write(data)
f.close()
c.close()
s.close()





