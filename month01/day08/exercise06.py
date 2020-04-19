"""
    练习2：定义函数,在终端中打印矩形
      格式:
        * * * * *
        * * * * *
        * * * * *
      测试：
          3行5列
          8行9列
"""


def print_form(count_r, count_c, char):
    """
        打印矩形
    :param count_r:int类型,行数
    :param count_c:int类型,列数
    :param char:str类型,填充的字符
    """
    for r in range(count_r):
        for c in range(count_c):
            print(char, end=" ")
        print()


print_form(3, 5, "*")
print_form(8, 9, "#")
