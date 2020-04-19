"""
    yield 思想
        旧思想：创建迭代器类,完成需求.
        新思想：yield自动生成迭代器,完成需求.
            循环...
                yield 结果
    练习:exercise02
"""


class InformationController:
    def __init__(self):
        self.__list_infos = []

    def add_info(self, info):
        self.__list_infos.append(info)

    def __iter__(self):
        for item in self.__list_infos:
            # return item# 会退出方法（还能返回一个）
            yield item  # 不会退出方法（暂时离开,下次调用继续执行）


controller = InformationController()
controller.add_info("王鹏鹏")
controller.add_info("田静")
controller.add_info("黄权威")
controller.add_info("佳佳")

print(controller)  # print(   controller.__str__()   )

# for item in controller:
#     print(item)

iterator = controller.__iter__()
while True:
    try:
        itme = iterator.__next__()
        print(itme)
    except StopIteration:
        break
