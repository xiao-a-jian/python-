"""
    字典推导式
     练习:exercise04
"""

# 需求：1-10之间的数字存储字典
#      key :数字    value:数字的平方
# dict_numbers = {}
# for number in range(1,11):
#     dict_numbers[number] = number ** 2
dict_numbers = {number: number ** 2 for number in range(1, 11)}
print(dict_numbers)

# 需求：1-10之间的奇数存储字典
#      key :数字    value:数字的平方
dict_numbers = {number: number ** 2 for number in range(1, 11) if number % 2}
print(dict_numbers)
