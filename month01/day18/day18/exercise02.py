"""
    # 新功能：打印函数执行时间
    #        执行前记录时间
    #        执行后用当前时间 - 执行前时间
"""
import time

def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # 旧功能 func01
        stop_time = time.time()
        print("函数执行了%f秒" % (stop_time - start_time))
        return result

    return wrapper

# 旧功能
@print_execute_time
def func01(n):
    sum_value = 0
    for i in range(n):
        sum_value += i
    return sum_value


print(func01(10))# 0.000002
print(func01(100000))# 0.004352
