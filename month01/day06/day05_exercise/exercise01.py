"""
在终端中获取一个整数,作为边长,打印矩形.
    例如:5
    *****   5
    *   *   * 5-2  *
    *   *
    *   *
    *****    5
"""
number = int(input("请输入一个整数："))
for i in range(number):
    if i == 0 or i == number - 1:
        print("*" * number)
    else:
        print("*" + " " * (number - 2) + "*")
