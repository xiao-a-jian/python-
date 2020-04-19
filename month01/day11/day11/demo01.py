"""
    类成员
        类变量
        类方法
        类名.成员名

"""


class ICBC:
    """
        工商银行
    """
    # 类变量：总行的钱
    total_money = 1000000

    # 类方法：对类变量的操作
    @classmethod
    def print_total_money(cls):
        # print("工商银行的钱:", ICBC.total_money)
        print("工商银行的钱:", cls.total_money)

    def __init__(self, name, money=0):
        # 实例变量：每个银行的信息
        self.name = name
        self.money = money
        ICBC.total_money -= money


xd = ICBC("西单支行", 500000)
trt = ICBC("陶然亭支行", 400000)
# print("总行的钱,还有:", ICBC.total_money)  # 建议通过类访问
ICBC.print_total_money()# print_total_money(ICBC)

# print("总行的钱,还有:",xd.total_money) # 不建议通过对象访问
# print("总行的钱,还有:",trt.total_money)
