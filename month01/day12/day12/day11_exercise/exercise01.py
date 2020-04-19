"""
    定义函数,判断列表中是否存在相同元素
"""


# list01 = [4,5,6,67,6]
# state = False
# for r in range(len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] == list01[c]:
#             print("相同")
#             state = True
#
# if state == False:
#     print("不同")

# 速度慢,省内存
# def is_repetition(list_target):
#     for r in range(len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] == list_target[c]:
#                 return True # 可以直接退出函数
#     return False # 如果之前没有退出,说明没有重复

# 速度快,费内存
def is_repetition(list_target):
    return len(set(list_target)) != len(list_target)


list01 = [4, 5, 6, 67, 4]
print(is_repetition(list01))
