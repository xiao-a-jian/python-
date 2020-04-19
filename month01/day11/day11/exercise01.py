"""
    对象计数器
        统计XX类创建了多少对象
        画出内存图
"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print("总共娶了%d个" % cls.count)

    def __init__(self, name=""):
        self.name = name
        Wife.count += 1

# 客户(使用)端代码
w01 = Wife("建宁")
w02 = Wife("双儿")
w03 = Wife()
w04 = Wife()
w05 = Wife()
Wife.print_count()
