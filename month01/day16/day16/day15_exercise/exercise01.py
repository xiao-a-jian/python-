# 练习：定义函数,根据生日(年月日),计算活了多天.
#  公式：现在 - 生日
import time


def life_days(year, month, day):
    time_tuple = time.strptime("%d/%d/%d" % (year, month, day), "%Y/%m/%d")
    life_second = time.time() - time.mktime(time_tuple)
    return life_second / 60 / 60 // 24


print("我活了%d天" % life_days(1999, 1, 1))
