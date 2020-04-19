"""
    for for
    练习:exercise06/07
"""

# 3行5列的表格
for r in range(3):  # 外层循环做一次   -----  控制行       0      1      2
    for c in range(5):  # 内层循环做多次  -----  控制列  01234  01234  01234
        print("*", end=" ")  # 在一行打印
    print()  # 换行

