"""
    装饰器 语法细节：

"""

# 新功能
def print_func_name(func):
    def wrapper(*args,**kwargs):# 合并  ("A",)   ("B","C")
        print(func.__name__)
        return func(*args,**kwargs)  #  拆分
    return wrapper


def say_hello(a):
    print("hello")
    return 10

say_hello = print_func_name(say_hello)

@print_func_name
def say_goodbye(b,c):
    print("goodbye")
    return 20

result = say_hello(a = "A")
print(result)
print(say_goodbye("B","C"))
