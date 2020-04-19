"""
    定义函数,判断二维列表中是否包含某个元素
    例如：list01 中是否包含10
"""


def is_exist(double_list, element):
    """

    :param double_list:
    :param element:
    :return:
    """
    for line in double_list:
        if element in line:
            return True
    return False


list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
print(is_exist(list01, 33))
