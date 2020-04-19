class EpidemicInformationModel:
    """
        疫情信息模型
    """

    def __init__(self, region="", confirmed=0, dead=0, cure=0, eid=0):
        self.region = region
        self.confirmed = confirmed
        self.dead = dead
        self.cure = cure
        self.eid = eid

    def __str__(self):
        return "%s-%d-%d-%d-%d" % (self.region, self.confirmed, self.dead, self.cure, self.eid)


list_epidemics = [
    EpidemicInformationModel("北京", 410, 20, 300, 101),
    EpidemicInformationModel("上海", 400, 16, 310, 102),
    EpidemicInformationModel("河南", 1200, 50, 800, 103),
    EpidemicInformationModel("湖北", 60000, 3000, 40000, 104),
    EpidemicInformationModel("西藏", 1, 0, 1, 105),
]


# 练习1: 定义函数,查找确诊人数大于500的疫情信息
def find01():
    for item in list_epidemics:
        if item.confirmed > 500:
            yield item  # 返回多个数据使用yield


# 测试
# for item in find01():
#     print(item)
# 练习2: 定义函数,查找上海的疫情信息
def find02():
    for item in list_epidemics:
        if item.region == "上海":
            return item  # 返回单个数据使用return


# 测试
# print(find02())
# 练习3: 定义函数,查找确诊人数小于500,并且没有死亡人数的地区名称
def find03():
    for item in list_epidemics:
        if item.confirmed < 500 and item.dead == 0:
            yield item.region


# 测试
# for item in find03():
#     print(item)

# 练习4: 定义函数,查找所有疫情地区的名称与死亡人数.
def find04():
    for item in list_epidemics:
        yield (item.region, item.dead)


# 测试
for item in find04():
    print(item)
