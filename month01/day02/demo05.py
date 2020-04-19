"""
    类型转换
        结果 = 类型名称(待转换数据)
    练习:exercise04.py
"""
# 字符串 --> 整数
str_number = "250"
int_number = int(str_number)
print(type(int_number))

# 注意：待转换数据必须"长得像"代转类型
# print(int("250+"))#   250+ 不像 整数,所以报错（第三门课程解决）
# print(int("1.23"))

# 小数 --> 整数
print(int(8.93))  # 8

# ？ --> 字符串
print(str(100.444))

# 四舍五入保留指定精度
# 结果 = round(需要计算的小数,精度)
print(round(1.29, 1))  # 1.3
print(round(1.21, 1))  # 1.2
