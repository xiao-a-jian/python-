# 商品列表
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 2},
]
# 1. （5分）打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
for cid, c_info in dict_commodity_infos.items():
    print("商品编号%d,商品名称%s,商品单价%d." % (cid, c_info["name"], c_info["price"]))

# 2. （5分）打印所有订单信息,格式：订单编号xx,数量:xx.
for order in list_orders:
    print("订单编号%d,数量:%d." % (order["cid"], order["count"]))

# 3. （15分）打印所有订单中的商品信息,格式：商品名称xx,商品单价:xx,数量xx.
for order in list_orders:
    commodity = dict_commodity_infos[order["cid"]]
    print("商品名称%s,商品单价:%d,数量%d." % (commodity["name"], commodity["price"], order["count"]))

# 4. （20分）计算订单总价格：累加商品单价 * 数量
total_price = 0
for dict_order in list_orders:
    commodity = dict_commodity_infos[dict_order["cid"]]
    total_price += commodity["price"] * dict_order["count"]
print("总价格：" + str(total_price))

# 5.（20分）查找数量最少的订单(使用自定义算法,不使用内置函数)
min_order = list_orders[0]
for r in range(1, len(list_orders)):
    if min_order["count"] > list_orders[r]["count"]:
        min_order = list_orders[r]
print(min_order)

# 6. （25分）根据单价,升序排列商品信息(使用自定义算法,不使用内置函数)
# list01 = [(k, v) for k, v in dict_commodity_infos.items()]
# list01 = [a for a in dict_commodity_infos.items()]
list_commodity_infos = list(dict_commodity_infos.items())
for r in range(len(list_commodity_infos) - 1):
    for c in range(r + 1, len(list_commodity_infos)):
        if list_commodity_infos[r][1]["price"] > list_commodity_infos[c][1]["price"]:
            list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
dict_commodity_infos = dict(list_commodity_infos)
print(dict_commodity_infos)
