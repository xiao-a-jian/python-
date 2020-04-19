"""
    运算符
        算数运算符
        增强运算符
    练习:exercise05.py
"""

# 1.算数运算符  + - *
#             幂运算**
#             小数商 /
#             整数商 //  （地板除）
#             取余 %     （取模）
number01 = 10
number02 = 4
# 数字 + 数字 --> 数学运算
# 字符串 + 字符串 --> 字符拼接
# 字符串 + 数字 --> X报错
print(number01 ** number02)  # 10的4次方
print(number01 / number02)
print(number01 // number02)
print(number01 % number02)

# 2. 增强运算符 += -= *=
#             **=
#              /=
#              //=
#              %
number03 = 5

number03 + 5
print(number03)  # 5

# 增强运算符,运算过后增加了给自身赋值的操作
# number03 = number03 + 5
number03 += 5
print(number03)  # 10
