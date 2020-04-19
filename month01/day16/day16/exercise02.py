"""
    创建MyRange类,实现下列效果。
    mr = MyRange(5)
    for number in mr:
        print(number)
"""


class MyRange:
    def __init__(self, end):
        self.__end = end

    def __iter__(self):
        begin = 0
        while begin < self.__end:
            yield begin
            begin += 1


# 循环一次 计算一次 返回一次 （没有存储所有结果）
# for item in MyRange(5):
#     print(item)

mr = MyRange(5)
iterator = mr.__iter__()
while True:
    try:
        itme = iterator.__next__()
        print(itme)
    except StopIteration:
        break
