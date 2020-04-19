"""
multiprocessing 模块创建进程示例
1.编写进程函数
２.实例化进程对象
３.启动进程
４.回收进程
"""

import multiprocessing as mp
from time import sleep

def fun():
    print("开始一个进程")
    for i in range(5):
        sleep(2)
        print("子进程")
    print("结束一个进程")


p = mp.Process(target=fun)

p.start()

# 父进程会执行这部分代码
for i in range(4):
    sleep(1)
    print("父进程")

p.join()

