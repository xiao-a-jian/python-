"""
    Enclosing  外部嵌套作用域
        函数嵌套的情况下,内部函数可以访问外部嵌套变量,但是不能修改.
        如果修改必须通过 nonlocal 声明
"""


def func01():
    # 局部变量：相对于文件
    # 外部嵌套变量：相对于内部函数
    a = 10

    def func02():
        # print(a) # 内部函数可以访问外部嵌套变量
        # 创建了局部变量,没有修改外部嵌套变量
        # a = 20
        # 声明外部嵌套变量
        nonlocal a
        a = 20
        print(a)

    return func02


# func01()# 只能执行外部函数
# func01.func02() # 语法错误:外部函数不执行,内部函数更不能执行
result = func01()
result()  # 执行内部函数
result()  # 执行内部函数
