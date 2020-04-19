"""
    函数：功能
        制作
            def 函数名称(变量):
                函数体
        使用
            函数名称(数据)

        参数（变量）： 函数调用者 给 函数定义者 传递的信息

    程序运行过程：
        自上而下
        将函数加载到内存,但不执行函数体
    练习：exercise05/06
"""


# 重复使用，重复编写（万恶之源）
# print("直拳")
# print("直拳")
# print("勾拳")
# # ....
# print("直拳")
# print("直拳")
# print("勾拳")

# 制作函数
# 形式参数：表面上是一个攻击次数,实际没有数
def attack_repeat(count):
    """
        重复攻击
    :param count: int类型,攻击次数
    """
    for __ in range(count):
        attack()

def attack():
    """
        单次攻击
    """
    print("直拳")
    print("直拳")
    print("勾拳")
    print("临门一脚")


# 使用
attack()
# 　实际参数：真实具体的数据
attack_repeat(3)
attack_repeat(5)
