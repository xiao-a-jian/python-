"""
    列表推导式
"""
# 需求：在list01中找出xx条件的元素存入list_result
list01 = [34, 5, 65, 7, 87, 9]
# list_result = []
# for item in list01:
#     if item > 10:
#         list_result.append(item)
list_result = [item for item in list01 if item > 10]
print(list_result)

# 需求：在list01中将所有元素增加5之后存入list_result
# list_result = []
# for item in list01:
#         list_result.append(item + 5)
list_result = [item + 5 for item in list01]
print(list_result)
