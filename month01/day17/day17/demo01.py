"""
    函数式编程
        核心理论支柱：将函数赋值给变量
"""
# 1. 将函数赋值给变量
def func01():
    print("func01执行喽")

# 只是将函数名称赋值给变量(不调用不执行函数)
a = func01

# 通过变量调用函数
a() # func01()

# 2. 将函数赋值给参数
def func02():
    print("func02执行喽")

# 优势：func03 函数没有固定执行func01或者func02
def func03(func):
    print("func03执行喽")
    func()

func03(func01)
func03(func02)