"""
    zip
    练习:exercise05
"""
list01 = ["张无忌", "赵敏", "小昭"]
list02 = [201, 105, 302]
list03 = [500, 8000, 300]
for item in zip(list01, list02, list03):
    print(item)  # ('张无忌', 201, 500)
# 参照上述代码,定义生成器函数,将3个列表中对应的元素形成元组.
