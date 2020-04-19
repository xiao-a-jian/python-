"""
    解题步骤：
        1. 根据需求写出函数
        2. 将变化与稳定的代码单独定义在函数中
        3. 在稳定代码中定义参数隔离变化
        4. 将稳定与变化的函数组合在一起实现需求
"""
from common.iterable_tools import IterableHelper


class Wife:
    total_money = 1000

    def __init__(self, name="", height=0, weight=0, face_score=0, money=0):
        self.name = name
        self.height = height
        self.weight = weight
        self.face_score = face_score
        self.money = money


list_wifes = [
    Wife("双儿", 171, 100, 96, 6000),
    Wife("小郡主", 162, 90, 86, 20000),
    Wife("建宁", 168, 95, 95, 30000),
    Wife("方怡", 173, 108, 96, 5000),
    Wife("凤姐", 150, 180, 30, 10000),
    Wife("沐剑屏", 161, 100, 90, 6000),
    Wife("阿珂", 181, 88, 100, 6000),
]


# 练习1：
#     需求1：在老婆列表中查找高度大于170的所有老婆
# def find01():
#     for item in list_wifes:
#         if item.height > 170:
#             yield item

#     需求2：在老婆列表中查找颜值小小于90的所有老婆
# def find02():
#     for item in list_wifes:
#         if item.face_score < 90:
#             yield item


def condition01(item):
    return item.height > 170


def condition02(item):
    return item.face_score < 90


def find(func):
    for item in list_wifes:
        # if item.face_score < 90:
        # if condition02(item):
        if func(item):
            yield item


for item in find(condition01):
    print(item.__dict__)


# 练习2：
#     需求1：在老婆列表中查找“双儿”老婆
#     需求2：在老婆列表中查找工资大于10000的老婆(满足条件的第一个)
# def find01():
#     for item in list_wifes:
#         if item.name == "双儿":
#             return item
#
# def find02():
#     for item in list_wifes:
#         if item.money > 10000:
#             return item


def condition03(item):
    return item.name == "双儿"


def condition04(item):
    return item.money > 10000


def find_single(func):
    for item in list_wifes:
        if func(item):
            return item


print(find_single(condition03).__dict__)


# 练习3：
#     需求1：在老婆列表中查找高度小于170的老婆数量
#     需求2：在老婆列表中查找颜值大于90的老婆数量

def condition05(item):
    return item.height < 170


def condition06(item):
    return item.face_score > 90


def get_count(func):
    count = 0
    for item in list_wifes:
        if func(item):
            count += 1
    return count


print(get_count(condition05))

# 调用静态方法
for itme in IterableHelper.find(list_wifes, condition01):
    print(itme.__dict__)

print(IterableHelper.get_count(list_wifes, condition05))

# 使用lambda表达式
for itme in IterableHelper.find(list_wifes, lambda item:item.height > 170):
    print(itme.__dict__)

print(IterableHelper.find_single(list_wifes,lambda item:item.name == "双儿").__dict__)

print(IterableHelper.get_count(list_wifes, lambda item:item.face_score > 90))

# 练习4：
#     需求1：在老婆列表中查找所有老婆的姓名与颜值
for item in IterableHelper.select(list_wifes,lambda wife:(wife.name,wife.face_score)):
    print(item)
#     需求2：在老婆列表中查找所有老婆的身高、体重、颜值
for item in IterableHelper.select(list_wifes,lambda wife:(wife.height,wife.weight,wife.face_score)):
    print(item)

# 练习5：
#     需求1：在老婆列表中查找颜值最高的老婆
print(IterableHelper.get_max(list_wifes, lambda element: element.face_score).__dict__)
#     需求2：在老婆列表中查找财产最大的老婆
print(IterableHelper.get_max(list_wifes, lambda element: element.money).__dict__)

# 练习6：
#     需求1：根据身高对老婆列表进行升序排列
#     需求2：根据体重对老婆列表进行升序排列
IterableHelper.order_by(list_wifes,lambda w:w.height)
IterableHelper.order_by(list_wifes,lambda w:w.weight)
for item in list_wifes:
    print(item.__dict__)

# 练习7：
#     需求1：累加老婆们的体重
#     需求2：累加老婆们的财产
print(IterableHelper.sum_value(list_wifes, lambda w: w.money))