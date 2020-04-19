"""
    运算符重载
        +
        +=
    练习：exercise01
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

    # + 返回新数据
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    # += 可变对象在原有基础上累加,不可变再创建新的
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


v01 = Vector2(1, 1)
v02 = Vector2(2, 2)
print(v01 + v02)  # print(  v01.__add__(v02)   )

print(id(v01))
v01 += v02  # v01.__iadd__(v02)
print(id(v01))
print(v01)

list01 = [1]
list01 += [2]  # 在list01列表基础上增加
print(list01)  # [1,2]

tuple01 = (1,)
tuple01 += (2,)  # 创建新元组
print(tuple01)  # (1,2)

# 练习：根据笔记,参照课堂代码,再自行完成2个重载（算数运算符、增强运算符）.


