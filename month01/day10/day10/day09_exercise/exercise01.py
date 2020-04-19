"""
   list01 = [4,435,5,667,875,341]
   定义函数,删除列表中大于10的数字
"""

list01 = [444, 435, 445, 667, 875, 341]


# 从前向后判断
# for itme in list01:
#     if itme > 10:
#         # 删除原理：后往前【挤】
#         list01.remove(itme)
# 错误原因：删除元素时,内部后一个向前移动,我们依然向后判断,会错过一个元素.

# 核心解决方案：判断过程与删除过程相向而行
# for i in range(len(list01)-1,-1,-1):
#     if list01[i] > 10:
#         # list01.remove(list01[i]) # remove内部也会循环判断
#         del list01[i]

def delete_by_condition(list_target):
    """

    :param list_target:
    :return:
    """
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] > 10:
            del list_target[i]


# 测试
delete_by_condition(list01)
print(list01)
