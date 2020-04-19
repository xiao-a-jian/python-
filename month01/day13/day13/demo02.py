"""
    内置可重写函数
        __str__
        练习：exercise01
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 对人友好的（内部返回的字符串没有任何限制）
    def __str__(self):
        return "%s今年%d了" % (self.name, self.age)


p1 = Person("王鹏鹏", 16)
# <__main__.Person object at 0x7f3a14d58ef0>
print(p1)  # print(p1.__str__())
# print(p1.__str__())

# str(10)  #
# print(10.__str__())
