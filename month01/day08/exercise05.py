"""
    练习1：定义函数,将一维列表元素以一行打印在终端中
          格式:元素1 元素2 元素3

          测试：
          list01 = [2,3,4,56]
          list02 = ["a","b","c","d"]
"""


def print_list(list_target):
    """
        打印列表
    :param list_target:list类型,需要被打印的列表
    """
    for item in list_target:
        print(item, end=" ")
    print()


list01 = [2, 3, 4, 56]
list02 = ["a", "b", "c", "d"]
print_list(list01)
print_list(list02)

