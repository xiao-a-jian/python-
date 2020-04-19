"""
    练习1:在终端中录入一个疫情确诊人数,再录入一个治愈人数,
        打印治愈比例
        格式：治愈比例为xx%
"""
confirmed_number = int(input("请输入确诊人数："))
cure_number = int(input("请输入治愈人数："))
cure_rate = cure_number / confirmed_number * 100
print("治愈比例为：" + str(round(cure_rate, 2)) + "%")

confirmed_number = int(input("请输入确诊人数："))
cure_number = int(input("请输入治愈人数："))
cure_rate = cure_number / confirmed_number * 100
print("治愈比例为：" + str(round(cure_rate, 2) + "%"))

confirmed_number = int(input("请输入确诊人数："))
cure_number = int(input("请输入治愈人数："))
cure_rate = cure_number / confirmed_number * 100
print("治愈比例为：" + str(round(cure_rate, 2) + "%"))
"""
    练习2:在终端中录入一个4位整数, 打印每位相加和
        例如：1234 -->  1 + 2+ 3 + 4 
"""
number = int(input("请输入一个四位数："))
result = number % 10 + number // 10 % 10 + number // 100 % 10 + number // 1000
print("各位相加：" + str(result))
