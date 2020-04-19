"""
    练习：
        在终端中录入4个同学身高,打印最高的值.
        算法：
            170    160    180    165
            假设第一个就是最大值
            使用假设的和第二个进行比较,如果发现更大的,则替换假设的
            使用假设的和第三个进行比较,如果发现更大的,则替换假设的
            使用假设的和第四个进行比较,如果发现更大的,则替换假设的
            最后，假设的就是最大的.
"""
height01 = float(input("请输入第1个同学身高："))
height02 = float(input("请输入第2个同学身高："))
height03 = float(input("请输入第3个同学身高："))
height04 = float(input("请输入第4个同学身高："))
max = height01
# 用假设的和后面进行比较
if max < height02:
    max = height02
if max < height03:
    max = height03
if max < height04:
    max = height04
print(max)
