"""
    实例成员: 对象.成员名
        实例变量
            对象.变量名

        实例方法
            对象.方法名称()
"""
# 全局变量
a = 10


def func01():
    # 局部变量
    b = 20


class MyClass:
    def __init__(self, c):
        # 实例变量
        self.c = c

    def func02(self):
        pass


mc01 = MyClass(30)
print(mc01.c)
print(mc01.__dict__)  # 系统提供的，可以获取对象所有实例变量 {'c': 30}
# mc01.d = 40  # 实例变量(不可取)
mc01.func02()  # 通过对象地址访问实例方法
# MyClass.func02(mc01) # 不建议
