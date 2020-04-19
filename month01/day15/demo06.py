"""
    迭代器
        需求：自定义对象,参与for循环
        练习:exercise03
"""


class MyIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        try:
            self.__index += 1
            return self.__data[self.__index]
        except IndexError:
            raise StopIteration()


class InformationController:
    def __init__(self):
        self.__list_infos = []

    def add_info(self, info):
        self.__list_infos.append(info)

    def __iter__(self):
        return MyIterator(self.__list_infos)


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
