"""
    运算符重载
        ==
    练习：让自定义的类，通过内置sort方法实现排序.
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x:%d,y:%d" % (self.x, self.y)

    # ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

list01 = [
    Vector2(1, 1),
    Vector2(3, 3),
    Vector2(2, 2),
    Vector2(1, 1),
    Vector2(5, 5),
    Vector2(4, 4),
]

v1 = Vector2(1, 1)
print(v1)# v1.__str__()

v2 = Vector2(1, 1)
# id(v1) == id(v2)
print(v1 is v2)  # False

print(v1 == v2)
print(Vector2(1, 1) == Vector2(1, 1))
print(Vector2(1, 1) in list01)  # ?
print(list01.count(Vector2(1, 1)))
list01.sort()
for item in list01:
    print(item)

