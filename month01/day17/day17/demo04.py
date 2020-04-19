"""
    内置高阶函数
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
# 1. 过滤:查找满足条件的元素
# for itme in IterableHelper.find(list_wifes, lambda item:item.height > 170):
#     print(itme.__dict__)
for itme in filter(lambda item: item.height > 170, list_wifes):
    print(itme.__dict__)

# 2. 映射:根据逻辑将元素对应的信息返回出来
# for item in IterableHelper.select(list_wifes,lambda wife:(wife.name,wife.face_score)):
#     print(item)
for item in map(lambda wife: (wife.name, wife.face_score), list_wifes):
    print(item)

# 3. 排序：返回一个新列表,通过reverse=True指定降序
# IterableHelper.order_by(list_wifes,lambda w:w.height)
# 升序
# resutl = sorted(list_wifes,key = lambda w:w.height)
# 降序
resutl = sorted(list_wifes, key=lambda w: w.height, reverse=True)
for item in resutl:
    print(item.__dict__)

# 4. 获取最大/最小
# print(IterableHelper.get_max(list_wifes, lambda element: element.face_score).__dict__)
print(max(list_wifes, key=lambda element: element.face_score).__dict__)
