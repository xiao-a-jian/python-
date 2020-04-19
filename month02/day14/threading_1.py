"""
线程基础
"""
from threading import Thread
from time import sleep
import os

a = 1


# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getppid(), "播放：风")
    global a
    a = 1000


# 创建线程对象
t = Thread(target=music)
t.start()  # 启动线程，执行music

for i in range(4):
    sleep(1)
    print(os.getppid(), "播放:光")

t.join()  # 回收线程

print(a)  # 1000
