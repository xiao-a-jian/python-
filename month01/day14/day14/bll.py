"""
    business logic layer 业务逻辑层
"""
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