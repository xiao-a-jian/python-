"""
    创建狗类
            实例变量：品种、爱称、年龄、体重
            实例方法：吃、叫
    实例化两个对象、调用其方法.
"""


class Dog:
    """
        抽象的狗
        创建对象的模板
    """

    def __init__(self, breed, pet_name, age=0, weight=0.0):
        # 数据
        self.breed = breed
        self.pet_name = pet_name
        self.age = age
        self.weight = weight

    # 行为
    def shout(self):
        """
            叫
        """
        print(self.pet_name, "叫")

    def eat(self):
        """
            吃
        """
        self.shout()
        print(self.pet_name, "吃")


# 测试
mx = Dog("拉布拉多", "米咻", 4, 80)
hm = Dog("拉布拉多", "黑米", 3)

mx.shout()  # 自动传递对象地址  shout(mx)

hm.shout()
