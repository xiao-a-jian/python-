"""
双色球彩票
    红球:6个,1--33之间,不能重复
    蓝球:1个,1--16之间
    (1)创建随机彩票（一个列表,前六个是红球,最后一个蓝球）
    (2)在终端中购买彩票(提示:号码已经存在,号码超过范围)
    (3)自由发挥
"""
import random

"""
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
"""

list_Lottery_ball = []
# 循环条件：存储6个球
while len(list_Lottery_ball) < 6:
    red_ball = random.randint(1, 33)
    if red_ball not in list_Lottery_ball:
        list_Lottery_ball.append(red_ball)
list_Lottery_ball.append(random.randint(1, 16))
print(list_Lottery_ball)
