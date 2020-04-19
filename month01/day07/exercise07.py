"""

"""
# 二维列表
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# 1. 通过二维列表打印7/10/12
print(list01[1][2])
print(list01[2][1])
print(list01[2][3])
# 2. 循环打印第一行数据(一行一个)
# for c in range(len(list01[0])):
#     print(list01[0][c])
for item in list01[0]:
    print(item)
# 3. 循环打印第三列数据(一行一个)
for r in range(len(list01)):
    print(list01[r][2])
# 4. 从右到左打印第二行数据(一行一个)
for c in range(len(list01[1]) - 1, -1, -1):  # 3210
    print(list01[1][c])
# 5. 从下到上打印第四列数据(一行一个)
for r in range(len(list01) - 1, - 1, - 1):
    print(list01[r][3])
# 6. 将二维列表以表格形状打印到终端中
# for r in range(len(list01)):
#     for c in range(len(list01[r])):
#         print(list01[r][c], end=" ")
#     print()
for line in list01:
    for element in line:
        print(element, end=" ")
    print()
