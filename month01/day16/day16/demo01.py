"""
    迭代器 --> yield
"""

class InformationController:
    def __init__(self):
        self.__list_infos = []

    def add_info(self, info):
        self.__list_infos.append(info)

    def __iter__(self):
        # 原理：自动生成迭代器代码
        # 1. 将yield以前的代码定义到__next__方法体中
        # 2. 将yield以后的数据作为__next__方法返回值

        print("准备数据：")
        yield self.__list_infos[0]# 产生数据

        print("准备数据：")
        yield self.__list_infos[1]# 产生数据

        print("准备数据：")
        yield self.__list_infos[2]# 产生数据

        print("准备数据：")
        yield self.__list_infos[3]# 产生数据

controller = InformationController()
controller.add_info("王鹏鹏")
controller.add_info("田静")
controller.add_info("黄权威")
controller.add_info("佳佳")

print(controller)# print(   controller.__str__()   )

# for item in controller:
#     print(item)

iterator = controller.__iter__()
while True:
    try:
        itme = iterator.__next__()
        print(itme)
    except StopIteration:
        break
