# 参照上述代码,定义生成器函数,将3个列表中对应的元素形成元组.
def my_zip(list01_target, list02_target, list03_target):
    for i in range(len(list01_target)):
        yield (list01_target[i], list02_target[i], list03_target[i])


list01 = ["张无忌", "赵敏", "小昭"]
list02 = [201, 105, 302]
list03 = [500, 8000, 300]
for item in my_zip(list01, list02, list03):
    print(item)  # ('张无忌', 201, 500)
