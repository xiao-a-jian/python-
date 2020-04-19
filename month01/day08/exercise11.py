# 练习： 改造day04/exercise02
# 创建函数,计算整数每位相加和
def sum_of_each_unit(int_number):
    """

    :param int_number:
    :return:
    """
    value = 0
    for item in str(int_number):
        value += int(item)
    return value


print(sum_of_each_unit(1233))


# 练习: 定义函数,翻转英文语句.
# 改造day06/exercise04
def rollback(message):
    list_temp = message.split(" ")
    return " ".join(list_temp[::-1])


print(rollback("How are you"))
