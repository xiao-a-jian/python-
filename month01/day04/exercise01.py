"""
    猜数字
        程序产生1个,1--100之间的随机数.
        让玩家重复猜测,直到猜对为止
        每次提示：大了   小了   恭喜猜对了,总共猜了?次.

# 准备随机数工具
import random

# 产生随机数
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
"""
# 准备随机数工具
import random

# 产生随机数
random_number = random.randint(1, 100)

count = 0
while True:
    count += 1
    input_number = int(input("请输入要猜的数字（1-100）："))
    if input_number > random_number:
        print("猜大了！")
    elif input_number < random_number:
        print("猜小了！")
    else:
        print("猜对了猜了" + str(count) + "！")
        break
