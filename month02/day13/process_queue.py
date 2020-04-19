"""
消息队列
"""

from multiprocessing import Process, Queue

q = Queue()


def request():
    name = "lj"
    passwd = "123"
    q.put(name)
    q.put(passwd)


def handle():
    name = q.get()
    passwd = q.get()
    print("获取用户：", name, passwd)


p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()
