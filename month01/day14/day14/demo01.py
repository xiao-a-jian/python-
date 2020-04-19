"""
    组合复用
        使用变量复用
"""


class A:
    def func01(self):
        pass

class B:
    def __init__(self):
        self.a = A()

    def func02(self):
        self.a.func01()

# class A:
#     def func01(self):
#         pass

# class B:
#     def func02(self, a):
#         a.func01()



