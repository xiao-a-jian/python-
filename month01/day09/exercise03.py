# 练习：创建函数,将整数列表中所有偶数修改为None
def change_even_to_None(list_numbers):
    """

    :param list_numbers:
    :return:
    """
    for i in range(len(list_numbers)):
        if list_numbers[i] % 2 == 0:
            list_numbers[i] = None


list01 = [4, 3, 5, 56, 6, 77, 87]
change_even_to_None(list01)
print(list01)
