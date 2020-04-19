"""
    装饰器：
        在不改变原函数的调用以及内部代码情况下，为其添加新功能的函数
        核心逻辑：拦截
"""

""" 需求：say_hello 与 say_goodbye不调用但是执行print_func_name
# 新功能
def print_func_name(func):
    print(func.__name__)

# 原(旧)函数
def say_hello():
    # print_func_name(say_hello)
    print("hello")

def say_goodbye(): 
    print("goodbye")

say_hello()
say_goodbye()
"""


# 新功能
def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)  # 执行新功能逻辑
        return func(*args, **kwargs)  # 执行旧功能逻辑

    return wrapper


# 原(旧)函数
# @print_func_name
def say_hello():
    print("hello")


# 调用外部函数(拦截),返回内部函数(包裹了新与旧)
say_hello = print_func_name(say_hello)

@print_func_name
def say_goodbye():
    print("goodbye")


say_hello()  # 调用的是内部函数
say_hello()  # 调用的是内部函数
say_goodbye()
