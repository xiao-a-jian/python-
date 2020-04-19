"""
    定义函数,获取成绩.如果输入有误,重新输入,直到输入正确。
"""


def get_score():
    while True:
        try:
            # score = float(input("请输入你的成绩"))
            # return score
            return float(input("请输入你的成绩"))
        except:
            print("输入错误重新输入")


print("成绩是:", get_score())
