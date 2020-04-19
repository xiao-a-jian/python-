"""
    yield -->  生成器
    练习:exercise03
    练习:exercise06
"""

"""
# 生成器 = 可迭代对象 + 迭代器（核心）
class Generator:
    def __iter__(self):
        return self
    
    def __next__(self):
        return ...
"""
# 循环一次  计算一次  返回一次
def my_range(end):
    begin = 0
    while begin < end:
        yield begin
        begin += 1

# 循环一次 计算一次 返回一次 （没有存储所有结果）
# for item in my_range(9):
#     print(item)

mr = my_range(5)
iterator = mr.__iter__()
while True:
    try:
        itme = iterator.__next__()
        print(itme)
    except StopIteration:
        break
