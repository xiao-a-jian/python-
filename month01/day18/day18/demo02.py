"""
    闭包：外部函数执行过后，栈帧不释放。为了给内部函数使用.
        三大要素：
            1. 函数嵌套
            2. 内部函数使用外部函数变量
            3. 外部函数返回内部函数
        核心价值：逻辑连续
        应用：装饰器
"""

# 情景：获取压岁钱
def give_gife_money(money):
    print("得到了", money, "元压岁钱")

    def child_buy(target, price):
        nonlocal money
        money -= price
        print("孩子购买了", target, "还剩下", money, "元")

    return child_buy

# 调用一次外部函数
action = give_gife_money(1000)
# 调用多次内部函数            正常外部函数栈帧应该释放
action("仿真枪", 300)
action("芭比娃娃", 200)
action("遥控汽车", 200)
action("遥控飞机", 200)
