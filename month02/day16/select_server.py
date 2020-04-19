"""
IO
select
"""
from select import select
from socket import *

# 创建监听套接字作为关注的IO对象
s = socket()
s.bind(('0.0.0.0', 1111))
s.listen(3)

# 设置为非阻塞
s.setblocking(False)

# 设置关注列表
rlist = [s]  # 初始关注监听套接字的读
wlist = []
xlist = []

while True:
    # 对IO进行监控
    rs, ws, xs = select(rlist, wlist, xlist)

    # 遍历列表分情况讨论
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("connect from", addr)
            # 添加客户端链接套接字作为监控对象
            c.setblocking(False)
            rlist.append(c)
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)

    for w in ws:
        w.send(b'OK')
        wlist.remove(w)

    for x in xs:
        pass

