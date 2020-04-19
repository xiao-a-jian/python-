"""
event 线程同步互斥
"""
from threading import Thread, Event

s = None
e = Event()


# 线程函数
def yzr():
    print("前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()


t = Thread(target=yzr)
t.start()

e.wait()
if s == "天王盖地虎":
    print("宝塔镇河妖")
else:
    print("打死")

t.join()
