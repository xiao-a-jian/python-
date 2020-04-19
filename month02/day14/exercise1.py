"""
会场出票系统
"""
from threading import Thread,Lock
from time import sleep
lock = Lock()
ticket = ["T%d" % x for x in range(1, 501)]  # 存储车票


def sell(w):
    """

    :param w: 窗口名称
    :return:
    """
    while True:
        sleep(0.1)
        lock.acquire()
        if not ticket:
            lock.release()
            break
        print("%s窗口卖出：%s" % (w, ticket.pop(0)))
        lock.release()
    print("余票不足")


jobs = []
for i in range(1, 11):
    t = Thread(target=sell, args=('W%d' % i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]
