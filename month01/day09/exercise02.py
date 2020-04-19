# 定义函数,对列表进行升序排列

# def order_by(list_target):
#     for r in range(0, len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] > list_target[c]:
#                 list_target[r], list_target[c] = list_target[c], list_target[r]
#     return list_target
#
# list01 = [54, 5, 5, 6, 7, 87, 89, 102, -58]
# result = order_by(list01)
# print(result)

def order_by(list_target):
    # 2. 修改可变对象  变量名[?] = ?
    # list_target = list_target[:]  创建新列表，所有没有修改传入的可变对象
    for r in range(0, len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    # 3. 无需通过return 返回结果
    # return list_target
# 1. 传入可变对象
list01 = [54, 5, 5, 6, 7, 87, 89, 102, -58]
order_by(list01)
print(list01)
# list01 = (54, 5, 5, 6, 7, 87, 89, 102, -58)   传入元组，函数内部不能修改
# order_by(list01)
