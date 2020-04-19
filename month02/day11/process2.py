"""
包含参数的进程函数
"""

from multiprocessing import Process
from time import sleep


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("i'm %s" % name)
        print("i'm working")


# p = Process(target=worker, args=(2, 'lj'))
# p = Process(target=worker, kwargs={'sec': 1, 'name': 'tom'})
p = Process(target=worker, args=(2,), kwargs={'name': 'tom'})

p.start()
p.join()
