"""
    类和对象
        现实事物  -抽象化->  类  -实例化->  对象
"""


# 需求：创造老婆

# 1. 抽象化
class Wife:
    # 数据：姓名 身高  颜值
    def __init__(self, name, height, face_score=30):
        # print(id(self))
        self.name = name
        self.height = height
        self.face_score = face_score

    # 行为(函数 = 方法)：工作
    def work(self):
        print(self.name, "工作")


# 2. 实例化
tc = Wife("铁锤", 180, 25)  # 自动调用构造函数__init__
# print(id(tc))
tc.work()  # 通过对象地址,调用方法,会自动传递对象地址 work(tc)
ch = Wife("翠花", 160, 26)  # 自动调用构造函数__init__
ch.work()
