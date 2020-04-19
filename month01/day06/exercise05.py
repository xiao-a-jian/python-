# 练习：运用容器思想,改造下列代码
# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
# if month < 1 or month > 12:
#     print("月份有误")
# elif month == 2:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("29天")
#     else:
#         print("28天")
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print("30天")
# else:
#     print("31天")

# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
# if month < 1 or month > 12:
#     print("月份有误")
# elif month == 2:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print("29天")
#     else:
#         print("28天")
# # elif month == 4 or month == 6 or month == 9 or month == 11:
# elif month in (4, 6, 9, 11):
#     print("30天")
# else:
#     print("31天")

year = int(input("请输入年份："))
month = int(input("请输入月份："))
# 元组创建后,不能修改(创建之前数据随便)
day_of_month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
tuple_days_of_month = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(tuple_days_of_month[month - 1])
