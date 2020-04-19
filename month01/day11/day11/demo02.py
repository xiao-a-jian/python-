"""
    封装数据
"""
# 面向过程,没有对数据封装.
# dict_commodity_infos = {
#     1001: {"name": "屠龙刀", "price": 10000},
#     1002: {"name": "倚天剑", "price": 10000},
#     1003: {"name": "金箍棒", "price": 52100},
#     1004: {"name": "口罩", "price": 20},
#     1005: {"name": "酒精", "price": 30},
# }

# list_commodity_infos = list(dict_commodity_infos.items())
# for r in range(len(list_commodity_infos) - 1):
#     for c in range(r + 1, len(list_commodity_infos)):
#         if list_commodity_infos[r][1]["price"] > list_commodity_infos[c][1]["price"]:
#             list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
# dict_commodity_infos = dict(list_commodity_infos)
# print(dict_commodity_infos)

# 优势1：将数据与对数据的操作相关联。
class CommodityInfo:
    """
        对商品信息的抽象
    """

    def __init__(self, cid, name="", price=0.0):
        self.cid = cid
        self.name = name
        self.price = price

    def print_self(self):
        print("编号是%d,名称是%s,单价是%f" % (self.cid, self.name, self.price))


list_commoditys = [
    CommodityInfo(1001, "屠龙刀", 10000),
    CommodityInfo(1002, "倚天剑", 30000),
    CommodityInfo(1003, "游戏机", 20000),
]
# 优势2：代码可读性更高（类是对象的模板）。
for r in range(len(list_commoditys) - 1):
    for c in range(r + 1, len(list_commoditys)):
        if list_commoditys[r].price > list_commoditys[c].price:
            list_commoditys[r], list_commoditys[c] = list_commoditys[c], list_commoditys[r]

for item in list_commoditys:
    print(item.price)