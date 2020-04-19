"""
    列表推导式嵌套
        从第一个列表中取出第一个元素,与第二个列表所有元素进行比较
        从第一个列表中取出第二个元素,与第二个列表所有元素进行比较
        从第一个列表中取出第三个元素,与第二个列表所有元素进行比较
    练习:exercise03~04
"""
# 需求
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["雪碧", "可乐", "牛奶", "咖啡"]

# list_result = []
# # 取数据
# for r in list01:
#     # 作比较
#     for c in list02:
#         list_result.append((r, c))

list_result = [(r, c) for r in list01 for c in list02]
print(list_result)
