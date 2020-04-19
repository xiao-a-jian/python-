"""
    多继承
        同名方法解析顺序
        继承在于隔离变化，多继承在于隔离多个变化
        (有多个客户端,需要在业务需求中通过继承统一一个类型的行为).
"""

class A:
    def func01(self):
        print("A -- func01")


class B(A):
    def func01(self):
        print("B -- func01")


class C(A):
    def func01(self):
        print("C -- func01")


class D(B, C):
    def func01(self):
        print("D -- func01")
        super().func01()  # B
        C.func01(self)  # 如果希望调用父类其他同名方法,需要通过类名调用(传递对象)

d = D()
d.func01()

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())
