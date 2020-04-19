"""
poll
"""
from select import *
from socket import *

# 创建监听套接字作为关注的IO对象
s = socket()
s.bind(('0.0.0.0', 1111))
s.listen(3)

# 设置为非阻塞
s.setblocking(False)
# 查找字典
fdmap = {s.fileno(): s}

p = poll()

p.register(s, POLLIN)


while True:
    # 对IO进行监控
    events = p.poll
    # 遍历列表分情况讨论
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connect from", addr)
            # 添加客户端链接套接字作为监控对象
            c.setblocking(False)
            p.register(c, POLLIN)
            fdmap[c.fileno()] = c
        else:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'OK')




