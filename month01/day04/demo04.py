"""
    continue 跳过

    break 跳出
    练习:exericse04
"""
# 需求：累加1--100之间所有能被3整除的数字的整数
# sum_value = 0
# for number in range(1, 101):
#     # 如果满足条件 则 累加
#     if number % 3 == 0:
#         sum_value += number
# print(sum_value)

sum_value = 0
for number in range(1, 101):
    # 如果不满足条件 则 不跳过
    if number % 3 != 0:
        continue
    sum_value += number
print(sum_value)
