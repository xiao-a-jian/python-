"""
    在终端中循环录入商品信息(名称,价格),如果商品名称为空字符,停止录入。
    判断如果录入了"口罩",那么打印其价格.
    判断如果录入了"屠龙刀",那么将其删除.
    计算所有商品的总价格
    打印所有商品信息(一行一个)：
        格式：xxx的价格是xx.
"""
dict_commodity_information = {}
while True:
    name = input("请输入商品名称：")
    if not name:
        break
    price = input("请输入商品价格：")
    dict_commodity_information[name] = float(price)

if "口罩" in dict_commodity_information:
    print("口罩的价格是：%.2f" % dict_commodity_information["口罩"])
if "屠龙刀" in dict_commodity_information:
    del dict_commodity_information["屠龙刀"]
print("商品总价格为：%.2f" % sum(dict_commodity_information.values()))
for k_name, v_price in dict_commodity_information.items():
    print("%s的价格是%.2f" % (k_name, v_price))
