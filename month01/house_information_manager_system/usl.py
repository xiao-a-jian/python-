"""
    用户显示层
"""
from bll import HouseManagerController
from model import HouseModel


class HouseManagerView:
    def __init__(self):
        self.__manager = HouseManagerController()

    def __display_menu(self):
        print("1键查看总价最高的房源信息")
        print("2键查看面积最小的房源信息")
        print("3键查看户型种类")
        print("输入4键显示所有信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__output_house_by_max_total_price()
        elif item == "2":
            self.__output_house_by_min_area()
        elif item == "3":
            self.__output_houses_type()
        elif item == "4":
            self.__output_houses_by_all()


    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __output_house_by_max_total_price(self):
        house = self.__manager.get_house_by_max_total_price()
        self.__show_house(house)

    def __output_house_by_min_area(self):
        house = self.__manager.get_house_by_min_area()
        self.__show_house(house)

    def __show_house(self, house: HouseModel):
        print("%d|%s|%s|%s+|%s|%s|%s|%s|%d|%d|%s" % (
            house.id, house.title, house.community, house.years, house.house_type, house.area, house.floor,
            house.description, house.total_price, house.unit_price, house.follow_info))

    def __output_houses_type(self):
        for k, v in self.__manager.get_houses_type().items():
            print(k, "有", v, "个")

    def __output_houses_by_all(self):
        item = input("""a键根据编号升序查看\nb键根据单价降序查看\nc键根据关注人数降序查看""")
        result = None
        if item == "a":
            result = self.__manager.ascending_by_id()
        elif item == "b":
            result = self.__manager.descending_by_unit_price()
        elif item == "c":
            result = self.__manager.descending_by_attention()
        if result:
            for house in result:
                self.__show_house(house)
