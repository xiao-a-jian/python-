from multiprocessing import Process
from time import sleep
import os
import sys


def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), '---', os.getppid())

def th2():
    sleep(2)
    sys.exit("结束睡觉进程")  # 进程结束
    print("睡觉")
    print(os.getppid(), '---', os.getppid())


def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(), '---', os.getppid())


things = [th1, th2, th3]
jobs = []

for th in things:
    p = Process(target=th)
    jobs.append(p)
    p.start()


for i in jobs:
    i.join()









