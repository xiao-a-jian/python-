# 练习1：创建手机类，实例化2个对象
class MobilePhone:
    """
        抽象的手机类
    """
    # 数据：品牌 价格 颜色
    def __init__(self, brand, price, color):
        """
            创建一个新手机对象
        :param brand: 品牌
        :param price: 单价
        :param color: 颜色
        """
        self.brand = brand
        self.price = price
        self.color = color

    # 行为：拍照，砸核桃
    def take_picture(self):
        """

        :return:
        """
        print(self.brand, "拍照")

    def smash_nut(self):
        """

        :return:
        """
        print(self.brand, "砸核桃")

# 2. 具体化
HW = MobilePhone("华为P30", 5000, "green")
HW.take_picture()

iphone = MobilePhone("苹果", 5000, "白色")
iphone.take_picture()

# 练习2：画出下列代码内存图
mp01 = HW
HW.price = 6000
print(mp01.price) # ?

mp02 = iphone
iphone = MobilePhone("苹果",10000,"白色")
print(mp02.price) # ?

# 练习3：画出下列代码内存图
list01 = [
    mp01,
    mp02,
    MobilePhone("三星", 4000, "蓝色")
]
list01[0].color = "红色"
list02 = list01[1:2]
list02[0].color = "粉色"
for item in list01:
    print(item.color)





