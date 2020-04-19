"""
    继承数据
    练习:exercise01
"""


class Person:
    def __init__(self, name=""):
        self.name = name


"""
# 如果子类没有构造函数,创建对象时使用父类的构造函数
class Student(Person):
    pass

s01 = Student("zs")
print(s01.name)
"""


# 如果子类有构造函数,创建对象时使用子类的构造函数（子类覆盖了父类函数,好像它不存在）
# 子类必须通过super()调用父类构造函数(注意：给父类构造函数传递信息)
# 子类构造函数的参数：父类需要的信息,子类需要的信息
class Student(Person):
    def __init__(self, name="", score=0):
        # self.name = name
        super().__init__(name)
        self.score = score
        # 通过 super() 访问父类成员


s01 = Student("王鹏鹏", 59)
print(s01.name)
print(s01.score)
