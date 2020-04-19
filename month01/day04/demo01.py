"""
    while 循环的else语句作用：
        判断while循环退出原因,是在循环条件还是在循环体

    猜数字2.0
        最多才3次,猜中提示猜对啦,
        超过3次,游戏失败
"""
# 准备随机数工具
import random
# 产生随机数
random_number = random.randint(1, 100)
count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入要猜的数字（1-100）："))
    if input_number > random_number:
        print("猜大了！")
    elif input_number < random_number:
        print("猜小了！")
    else:
        print("猜对了猜了" + str(count) + "！")
        break
else:
    # 超过3次才执行（通过break退出不执行）
    print("游戏失败")
