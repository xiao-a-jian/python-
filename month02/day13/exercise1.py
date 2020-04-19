"""
练习：　
求100000以内的质数之和,计算所用时间

分别使用单个进程求解

4个进程同时执行求解 分为4份 1--25000 250001-50000...

10个进程同时执行求解 分为10份 1--10000 10001-20000...
"""

from multiprocessing import Process
from time import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = f(*args, **kwargs)
        end_time = time()
        print("时间：", end_time - start_time)
        return res
    return wrapper

def is_prime(n):
    if n < 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

@timeit
def prime_sum():
    prime = []
    for i in range(100000):
        if is_prime(i):
            prime.append(i)
    print(sum(prime))


# 单进程
prime_sum()


class Prime(Process):
    def __init__(self, begin, end):
        super().__init__()
        self.begin = begin
        self.end = end

    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if is_prime(i):
                prime.append(i)
        print(sum(prime))


@timeit
def process_4():
    jobs = []
    for i in range(1, 100001, 25000):
        p = Prime(i, i+25000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]


process_4()


@timeit
def process_10():
    jobs = []
    for i in range(1, 100001, 10000):
        p = Prime(i, i+10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]


process_10()
