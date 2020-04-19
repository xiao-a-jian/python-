"""
    内置可重写函数
         __repr__
    练习：exercise01
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    #  对解释器友好(符合Python代码)
    def __repr__(self):
        return 'Person("%s", %d)' % (self.name, self.age)

p1 = Person("王鹏鹏", 16)
# eval 函数：将字符串作为Python代码执行
print(eval("1+2-3"))
# 拷贝自定义对象
p2 = eval(p1.__repr__())
p1.name = "老王"  # 修改拷贝前的对象,不影响拷贝后的对象
print(p1)
print(p2)
# 练习：拷贝电动汽车对象
