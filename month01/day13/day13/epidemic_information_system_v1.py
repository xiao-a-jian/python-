"""
    疫情信息系统
    需求：
        输入1,循环获取疫情信息.
    练习1：
        需求：
            输入2,显示所有疫情信息.
        步骤：
            在View中判断是否输入"2"
            在Controller中定义__list_epidemics的只读属性
            在View中显示信息
"""


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


class EpidemicInformationController:
    """
        疫情信息逻辑控制器：负责处理业务逻辑
    """

    def __init__(self):
        self.__list_epidemics = []
        self.__eid_begin = 1000

    @property
    def list_epidemics(self):
        return self.__list_epidemics

    def add_epidemic(self, info):
        """
            添加疫情信息
        :param info: 需要添加的信息
        """
        # 设置信息的编号
        info.eid = self.__eid_begin
        self.__eid_begin += 1
        # 存储列表
        self.__list_epidemics.append(info)

    def get_epidemic_by_region(self, region):
        """
            根据地区获取疫情信息
        :param region:
        :return:
        """
        for epidemic in self.__list_epidemics:
            if epidemic.region == region:
                return epidemic

    def remove_epidemic_by_id(self, eid):
        """
            根据编号删除疫情信息
        :param eid:
        :return:是否删除成功
        """
        for i in range(len(self.__list_epidemics)):
            if self.__list_epidemics[i].eid == eid:
                # 使用del删除,后面必须索引或者切片定位的列表元素
                del self.__list_epidemics[i]
                return True
        return False


# 入口
view = EpidemicInformationView()
view.main()
