# 练习3：定义函数,将二维列表以表格状打印在终端中

def print_2d_list(list_target):
    """

    :param list_target:
    :return:
    """
    for line in list_target:
        for item in line:
            print(item, end="\t")
        print()


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print_2d_list(list01)
