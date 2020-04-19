import random

money = 0
list_Lottery_ball = []
red_ball01 = random.randint(1, 34)
list_Lottery_ball.append(red_ball01)
for itme in range(4):
    while True:
        red_ball = random.randint(1, 34)
        if red_ball not in list_Lottery_ball:
            list_Lottery_ball.append(red_ball)
            break
list_Lottery_ball.append(random.randint(1, 17))

print("""请输入要购买彩票的号码
前五个号码（1-33）
最后一个号码（1-16）
前五个号码中一个五十元
最后一个号码中100元
""")
buy_number = []
for i in range(1, 6):
    while True:
        number = int(input("请输入第%d个号码:" % i))
        if (number < 0 and number > 34) or number in buy_number:
            print("号码已经存在或号码超过范围请重新输入")
        else:
            buy_number.append(number)
            break
    if number in list_Lottery_ball:
        money += 50
number = int(input("请输入第6个号码:"))
buy_number.append(number)
if number in list_Lottery_ball:
    money += 100
print("开奖号码:")
print(list_Lottery_ball)
print("中了%d元钱！" % money)
