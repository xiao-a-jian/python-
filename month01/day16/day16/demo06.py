"""
    生成器表达式
"""
list01 = ["a", 10, "b", 1.5, True, 20]

# 将list01中所有整数存储在list02中
# list02 = []
# for item in list01:
#     if type(item) == int:
#         list02.append(item)

list02 = [item for item in list01 if type(item) == int]
for item in list02:
    print(item)

# 生成器函数：函数体中有yield
# def find01():
#     for item in list01:
#         if type(item) == int:
#             yield item

# 生成器表达式：以推导式的语法形式,创建生成器对象.
result = (item for item in list01 if type(item) == int)
for item in result:
    print(item)

# 练习：将exercise06中生成器函数,改写为生成器表达式.
# 体会：延迟操作/惰性操作
