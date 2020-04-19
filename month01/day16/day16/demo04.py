"""
    内置生成器enumerate
    练习:exercise04
"""

list01 = [45, 5, 65, 7, 8]
# 需求：根据条件修改列表中的元素

# for item in list01:
#     if item > 10:
#         item = 0# 修改的是变量item(没有修改列列表)
# print(list01)

for index, element in enumerate(list01):
    if element > 10:
        list01[index] = 0
print(list01)
