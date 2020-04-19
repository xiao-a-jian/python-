"""
    老张开车去东北3.0
    练习:exercise02
"""

# 多态
# 咔嚓
# 疯了?   人传人?     断片了?
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        # 1. 调用父类(交通工具)
        vehicle.transport()


class Vehicle:
    """
        抽象的交通工具,统一概念,隔离变化
    """

    def transport(self):
        pass


class Car(Vehicle):
    # 2. 重写
    def transport(self):
        print("汽车行驶")


class Airplane(Vehicle):
    def transprt(self):
        print("起飞喽")


# 测试..
zl = Person("老张")
c01 = Car()
a01 = Airplane()
# 3. 创建子类对象
zl.go_to(c01)
