"""
    老张开车去东北2.0

    设计原则
        开闭原则：允许增加新功能，不能修改客户端代码.
        依赖倒置：使用抽象(父类),不使用实现(子类)
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("汽车行驶")

class Airplane:
    def fly(self):
        print("起飞喽")

# 测试..
zl = Person("老张")
c01 = Car()
a01 = Airplane()
zl.go_to(a01)
