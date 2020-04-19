#!/usr/bin/python3

import time
import random

time_tuple = time.localtime()

list_Lottery_ball = []
while len(list_Lottery_ball) < 6:
    red_ball = random.randint(1, 33)
    if red_ball not in list_Lottery_ball:
        list_Lottery_ball.append(red_ball)
list_Lottery_ball.sort()
list_Lottery_ball.append(random.randint(1, 16))
print(time.strftime("%Y/%m/%d %H:%M:%S", time_tuple), ":", list_Lottery_ball)

# from time import ctime
# from random import randint
#
# l = []
# while len(l) < 6:
#     num = randint(1, 33)
#     if num not in l:
#         l.append(num)
# l.sort()  # 排序
# l.append(randint(1, 16))
# print(ctime(), ":", l)
