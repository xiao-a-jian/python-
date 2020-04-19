"""
    复习
        封装
            封装数据：XXXModel   疫情信息模型(地区/确认人数/死亡人数/治愈人数/编号)
            封装行为：XXXController/XXXView   隐藏实现细节(私有成员,属性)
            设计思想：分而治之、变则疏之（控制Controller与显示View分离）
"""


# 通过对象访问成员



class XXView:
    def __init__(self):
        self.__controller = XXController()

    def func02(self):
        self.__controller.func01()

class XXController:
    def func01(self):
        pass


view = XXView()
view.func02()
