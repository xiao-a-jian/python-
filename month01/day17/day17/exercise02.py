"""
    使用内置高阶函数实现
    1. 在老婆列表中获取所有老婆的身高与体重
    2. 在老婆列表中获取财产小于10000的所有老婆
    3. 获取所有身高大于160的老婆名称与身高
    4. 将所有老婆的姓名与财产形成字典
    5. 将练习4的字典，根据值进行降序排列
    6. 找出列表中元素长度最小的元素[(1,1),(2,2,2),(3,3,3,3)]
"""


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

# 1. 在老婆列表中获取所有老婆的身高与体重
for item in map(lambda wife: (wife.height, wife.weight), list_wifes):
    print(item)
# 2. 在老婆列表中获取财产小于10000的所有老婆
for item in filter(lambda wife: wife.money < 10000, list_wifes):
    print(item)
# 3.获取所有身高大于160的老婆名称与身高
for item in map(lambda wife: (wife.name, wife.height),
                filter(lambda item: item.height > 160, list_wifes)):
    print(item)
# 4. 将所有老婆的姓名与财产形成字典
dict_info = dict(map(lambda item: (item.name, item.money), list_wifes))
# 5. 将练习4的字典，根据值进行降序排列
print(dict(sorted(dict_info.items(), key=lambda item: item[1], reverse=True)))
# 6. 找出列表中元素长度最小的元素[(1,1),(2,2,2),(3,3,3,3)]
list01 = [(1, 1), (2, 2, 2), (3, 3, 3, 3)]
print(min(list01, key=lambda item: len(item)))
