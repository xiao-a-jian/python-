"""
    作用域
        局部作用域：函数内部          小功能(一个局部小范围使用),使用局部变量
        全局作用域：.py文件          大功能(好多个局部都要使用),使用全局变量
"""


def func01():
    # 局部作用域：函数内部
    # 局部变量
    a = 10
    # 一个函数希望使用另外一个函数的局部变量,通过参数、返回值传递
    a_b = func02()
    print(a_b)


def func02():
    b = 20
    return b


# 全局作用域：.py文件
g01 = 100

def func03():
    # 可以在局部作用域中读取全局变量
    print(g01)

func03()

g02 = 200


def func04():
    # 局部作用域不能修改全局变量
    # g02 = 2000 # 创建新的局部变量,没有修改全局
    global g02  # 声明全局变量
    g02 = 2000

func04()
print(g02)

# 在局部作用域创建全局变量
# def func05():
#     global g05  # 声明全局变量:如果全局没有,那么创建;如果全局有,那么使用全局的
#     g05 = 2000
#
# func05()
# print(g05)
