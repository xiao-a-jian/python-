"""
    练习：
        创建父类:
            汽车(品牌,价格)
        创建子类：
            电动车(充电时间,电池容量)
        创建子类对象
"""


class Car:
    def __init__(self, brand="", price=0):
        self.brand = brand
        self.price = price

    def __str__(self):
        return "%s -- %d" % (self.brand, self.price)


class ElectricCar(Car):
    def __init__(self, brand="", price=0, power_time=0, battery=0):
        super().__init__(brand, price)
        self.power_time = power_time
        self.battery = battery

    def __str__(self):
        return "%s -- %d -- %d -- %d" % (self.brand, self.price, self.power_time, self.battery)

    def __repr__(self):
        return 'ElectricCar("%s", %d, %d, %d)' % (self.brand, self.price, self.power_time, self.battery)


c01 = Car("奥迪", 300000)
print(c01)

# 为了展示：重写__str__
TSL = ElectricCar("特斯拉", 200000, 5, 2000000)
print(TSL)

# 为了克隆：重写__repr__
tsl = eval(TSL.__repr__())
TSL.price = 1000000
print(tsl)
