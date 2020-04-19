"""
僵尸进程
"""

"""
包含参数的进程函数
"""

from multiprocessing import Process
from time import sleep

from signal import *
signal(SIGCHLD, SIG_IGN)


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("i'm %s" % name)
        print("i'm working")


p = Process(target=worker, args=(2,), kwargs={'name': 'tom'})
p.start()

# p.join(5)  # 回收子进程

while True:
    pass
