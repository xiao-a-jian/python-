"""
    封装行为
        属性的各种写法
            读写
            只读
            只写
"""


# 没有属性,调用者可以随意设置实例变量
# class MyClass:
#     def __init__(self, data=0):
#         self.data = data
#
# mc = MyClass(100)
# mc.data = 200
# print(mc.data)

# 使用属性,保护(限制数值范围)实例变量
# # 写法1：读写属性
# # 快捷键 props + 回车
# class MyClass:
#     def __init__(self, data=0):
#         self.data = data
#
#     @property
#     def data(self):
#         print("在读取数据前进行逻辑处理")
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         print("在设置数据前进行逻辑处理")
#         self.__data = value
#
#
# mc = MyClass(100)
# mc.data = 200
# print(mc.data)

# # 写法2：只读属性
# # 快捷键:prop
# class MyClass:
#     def __init__(self):
#         # 私有变量
#         self.__data = 100
#
#     @property
#     def data(self):
#         print("在读取数据前进行逻辑处理")
#         return self.__data
#
# mc = MyClass()
# # mc.data = 200 # 不修改
# print(mc.data)

# 写法3：只写属性
class MyClass:
    def __init__(self, data=0):
        self.data = data

    data = property()

    @data.setter
    def data(self, value):
        print("在设置数据前进行逻辑处理")
        self.__data = value

    # def set_data(self, value):
    #     print("在设置数据前进行逻辑处理")
    #     self.__data = value
    #
    # data = property(None,set_data)


mc = MyClass(100)
mc.data = 200
print(mc.__dict__)
# print(mc.data)
