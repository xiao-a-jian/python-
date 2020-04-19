"""
    user show layer 用户显示层
"""
from bll import EpidemicInformationController
from model import EpidemicInformationModel


class EpidemicInformationView:
    """
        疫情信息界面视图：负责处理界面逻辑
    """

    def __init__(self):
        self.__controller = EpidemicInformationController()

    def __show_menu(self):
        print("输入1键盘录入疫情信息")
        print("输入2键盘显示疫情信息")
        print("输入3键盘查找疫情信息")
        print("输入4键盘删除疫情信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_epidemics()
        elif item == "2":
            self.__print_epidemics()
        elif item == "3":
            self.__select_epidemic()
        elif item == "4":
            self.__delete_epidemic()

    def main(self):
        while True:
            self.__show_menu()
            self.__select_menu()

    def __input_epidemics(self):
        while True:
            region = input("请输入地区,如需退出输入空字符：")
            if region == "":
                break
            model = EpidemicInformationModel(region)
            model.confirmed = int(input("请输入确诊人数："))
            model.dead = int(input("请输入死亡人数："))
            model.cure = int(input("请输入治愈人数："))
            # 存储当前数据...
            self.__controller.add_epidemic(model)

    def __print_epidemics(self):
        for info in self.__controller.list_epidemics:
            self.__print_epidemic(info)

    def __print_epidemic(self, info):
        print("%s的确诊人数%d,死亡人数%d,治愈人数%d" % (info.region, info.confirmed, info.dead, info.cure))

    def __select_epidemic(self):
        region = input("请输入地区：")
        epidemic = self.__controller.get_epidemic_by_region(region)
        if epidemic:
            self.__print_epidemic(epidemic)
        else:
            print("您输入的地区没有疫情")

    def __delete_epidemic(self):
        eid = int(input("请输入需要删除的疫情信息编号："))
        if self.__controller.remove_epidemic_by_id(eid):
            print("删除成功")
        else:
            print("删除失败")
