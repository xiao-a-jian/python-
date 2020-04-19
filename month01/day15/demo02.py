"""
    内置模块
        time

   看教程：https://www.runoob.com/python3/python3-tutorial.html
   看文档：https://docs.python.org/zh-cn/3/
"""

import time

# 1. 时间戳（从1970年1月1日 0:0:0  UTC 到现在经过的秒数）
print(time.time())  # 1584156103.0306678

# 2. 时间元组（年、月、日、时、分、秒、星期、这一年的第几天、夏令时）
# 获取当前本地时间元组
time_tuple = time.localtime()
# time.struct_time(tm_year=2020, tm_mon=3, tm_mday=14, tm_hour=11, tm_min=21, tm_sec=43, tm_wday=5, tm_yday=74, tm_isdst=0)
print(time_tuple)
print(time_tuple.tm_year)  # print(time_tuple[0])
print(time_tuple.tm_wday)  # print(time_tuple[-3])  # print(time_tuple[6])

# 3. 时间戳 --> 时间元组
print(time.localtime(1584156103.0306678))
# 4. 时间元组 --> 时间戳
print(time.mktime(time_tuple))  # 1584157476.0

# 5. 时间元组 --> 字符串
print(time.strftime("%y/%m/%d %H:%M:%S", time_tuple))#20/03/14 11:58:26
print(time.strftime("%Y/%m/%d %H:%M:%S", time_tuple))# 2020/03/14 11:58:26

# 6. 字符串 --> 时间元组
print(time.strptime("2020/03/14 11:58:26", "%Y/%m/%d %H:%M:%S"))
print(time.strptime("2020 26", "%Y %S"))









