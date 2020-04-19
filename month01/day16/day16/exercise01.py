"""
    创建MyRange类,实现下列效果。
    mr = MyRange(5)
    for number in mr:
        print(number)
"""


class MyIterator:
    def __init__(self, stop):
        self.__stop = stop
        self.__index = -1

    def __next__(self):
        # -1 0 1 2 3    4 >=  5 - 1
        if self.__index >= self.__stop - 1:
            raise StopIteration()
        self.__index += 1
        return self.__index

class MyRange:
    def __init__(self, end):
        self.__end = end

    def __iter__(self):
        return MyIterator(self.__end)

# 循环一次 计算一次 返回一次 （没有存储所有结果）
for item in MyRange(99999999999999999999999999999999999999999999):
    print(item)

# iterator = controller.__iter__()
# while True:
#     try:
#         itme = iterator.__next__()
#         print(itme)
#     except StopIteration:
#         break
