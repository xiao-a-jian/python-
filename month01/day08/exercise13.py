# 改造day07/exercise01,定义函数,获取商品信息.
# dict_commodity_information = {}
# while True:
#     name = input("请输入商品名称：")
#     if not name:
#         break
#     price = input("请输入商品价格：")
#     dict_commodity_information[name] = float(price)

def get_goods_info():
    dict_commodity_information = {}
    while True:
        name = input("请输入商品名称：")
        if not name:
            break
        price = input("请输入商品价格：")
        dict_commodity_information[name] = float(price)
    return dict_commodity_information

print(get_goods_info())