"""
进程池
"""
from multiprocessing import Pool
from time import sleep,ctime


# 进程池函数 (在进程池创建之前声明)
def worker(msg):
    sleep(2)
    print(ctime(), '---', msg)


# 创建进程池
pool = Pool()


# 向进程池等待队列加入事件
for i in range(10):
    msg = "Tedu%d"%i
    pool.apply_async(func=worker, args=(msg,))

# 关闭进程池
pool.close()

# 阻塞等待回收进程池
pool.join()


