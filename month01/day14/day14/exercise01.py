"""
    定义图形管理器
        记录所有图形
        计算图形总面积

    图形：
        圆形 3.14 × 半径的平方
        矩形 长*宽
        ....

    以后可以还有新图形,但是不能再修改图形管理器。
    $要求：写出三大特征、四大原则的具体体现。
        封装：创建了GraphicManager、Circle、Rectanle
        继承：创建了Graphic
             隔离了GraphicManager与具体图形的变化
        多态：GraphicManager的calculate_total_area调用Graphic的get_area方法
             Circle、Rectanle重写Graphic的get_area方法
             添加到GraphicManager的都是具体图形Circle、Rectanle

        开闭原则：增加三角形,只需要创建新类,图形管理器无需改变。
        单一职责：
            GraphicManager：管理所有图形
            Circle：计算圆形面积
            Rectanle：计算矩形面积
        依赖倒置：GraphicManager 调用 Graphic,没有调用具体图形Circle、Rectanle...
        组合复用：GraphicManager 通过组合关系调用 图形算法(Graphic/Circle/Rectanle)
        何处使用继承？何处使用组合？
            继承：Graphic 统一 Circle、Rectanle
            组合：GraphicManager 连接 图形算法(Graphic/Circle/Rectanle)
"""


class GraphicManager:
    def __init__(self):
        self.__list_graphics = []

    def add_graphics(self, graphic):
        self.__list_graphics.append(graphic)

    def calculate_total_area(self):
        sum_value = 0
        for item in self.__list_graphics:
            # 编码时：调用父
            # 运行时：执行子。
            sum_value += item.get_area()
        return sum_value


class Graphic:
    """
        约束所有图形,在计算面积的功能上达到统一.
    """

    def get_area(self):
        pass


# -----------------------------------

class Circle(Graphic):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        super().get_area()
        return 3.14 * self.r ** 2


class Rectanle(Graphic):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def get_area(self):
        return self.l * self.w


# ----------------------------
# 测试
manager = GraphicManager()
manager.add_graphics(Circle(10))
manager.add_graphics(Rectanle(10, 20))
print(manager.calculate_total_area())
