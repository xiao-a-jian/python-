"""
    封装设计思想
        分而治之、变则疏之

        类  与  类行为不同
        对象与对象数据不同
"""

# 需求：老张开车去东北

#    老李   坦克
#    老王   飞机
#   变化点 --> 创建类

#   东北此时没有行为需要承担(东北会跑)
#         也没有过多数据(名字)

# 类  与  类行为不同

# 写法1：人在去的方法中创建车对象
#       语义：老张每次去一个地区，都开一辆新车.(旧车成为垃圾)
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position):
        print(self.name, "去", position)
        # 创建汽车对象
        car = Car()
        car.run()

class Car:
    def run(self):
        print("汽车行驶")

# 对象与对象数据不同
lz = Person("老张")
ls = Person("老孙")
lq = Person("老祁")

lz.go_to("东北")
"""

"""
# 写法2：人在创建的时候,创建车对象
#       语义：老张开车自己的车去一个地区
class Person:
    def __init__(self, name=""):
        self.name = name
        # 创建汽车对象
        self.car = Car()

    def go_to(self, position):
        print(self.name, "去", position)
        self.car.run()

class Car:
    def run(self):
        print("汽车行驶")

# 对象与对象数据不同
lz = Person("老张")

lz.go_to("东北")
lz.go_to("武汉")
"""

# 写法3：人类与车类没有固定关联关系，在人去东北时走到了一起。
#       语义：老张依赖传入的工具去一个地区
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, car):
        print(self.name, "去", position)
        car.run()


class Car:
    def run(self):
        print("汽车行驶")


lz = Person("老张")
car = Car()
# 去东北让人类与车类走到了一起
lz.go_to("东北", car)
