"""
    函数：
        制作
            def 函数名称(参数):
                函数体
                return 数据
        使用
            变量 = 函数名称(数据)

        返回值：函数定义着 给 函数调用者 传递的结果
"""


# 写法1
def func01():
    print("func01执行喽")
    return 100  # return 数据
    print("func01又执行喽")  # return 可以退出函数

re = func01()
print(re)


# 写法2
def func02():
    print("func02执行喽")
    # return # 相当于 return  None
    # 没有return关键字,也相当于 return  None

re = func02()
print(re)
