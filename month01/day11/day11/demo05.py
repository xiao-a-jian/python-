"""
    封装行为
        标准属性
            保护实例变量
"""


# 1. 创建属性对象(绑定读取方法,None)
# 2. 将属性对象赋值给变量age(方法名)
# 3. 为属性对象绑定写入方法

# 结论：拦截
#      如果没有以上步骤,操作的是实例变量
#      如果具有以上步骤,操作的是属性(property对象)

class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 1. 创建属性对象(绑定下面方法,None) 2. 将属性对象赋值给变量age(方法名)
    @property  # age = property(age,写入)
    def age(self):
        # 返回私有变量
        return self.__age

    @age.setter  # 3. 调用属性对象的setter方法,传入下面方法 [为属性对象绑定写入方法]
    def age(self, value):
        if 16 < value <= 30:
            # 设置私有变量
            self.__age = value
        else:
            raise Exception("我不要")


w01 = Wife("双儿", 20)
print(w01.name)
w01.age = 30
print(w01.age)
