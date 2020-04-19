# 练习:根据年月日,计算是这一年的第几天.
# 2020年5月10日
# 前几个月的天数 + 当月天数
# 31  29  31  30 + 10
year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))
day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
tuple_days_of_month = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# privious_month_days =0
# for i in range(month - 1):
#     privious_month_days += tuple_days_of_month[i]
privious_month_days = sum(tuple_days_of_month[:month - 1])
total_days = privious_month_days + day
print(total_days)
