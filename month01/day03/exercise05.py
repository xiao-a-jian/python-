# 练习1：在终端中录入一个整数,如果奇数为变量state赋值"奇数"
#       否则赋值"偶数"
state = "奇数" if int(input("输入一个整数")) % 2 else "偶数"
print(state)

# 练习2：在终端中录入一个年份,如果闰年为变量day赋值29
#       否则赋值"28
year = int(input("输入年份"))
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# 可读性太差
# day = 29 if not year % 4 and year % 100 or not year % 400 else 28
print(day)
