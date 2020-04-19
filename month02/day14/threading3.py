"""
线程属性
"""
from threading import Thread
from time import sleep
import time


def fun():
    sleep(3)
    print("属性")


t = Thread(target=fun)
t.setDaemon(True)  # 该线程会随主线程退出
t.start()

t.setName("Tarena")
print(t.getName())

print(t.is_alive())


# 自定义线程类
class mythread(Thread):
    def __init__(self, song, sec):
        super().__init__()
        self.song = song
        self.sec = sec

    def run(self):
        for i in range(3):
            print("播放")
            time.sleep(self.sec)


t = mythread('凉凉', 2)
t.start()
t.join()
