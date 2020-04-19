"""
    while 循环
        重复执行语句

        while 条件:
            循环体
        else:
            不满足条件执行的代码
    练习:exercise06
"""
# 死循环
while True:
    people_number = int(input("请输入人数："))
    money = people_number * 300 if people_number <= 5 else people_number * 280
    if money > 0:
        print(money)
    else:
        print("捣乱呢?")

    if input("请输入y键继续：") != "y" :
        break # 跳出循环
