"""
     练习:循环测试智商(exercise04.py),如果输入e则退出
"""
while True:
    mental_age = int(input("请输入心理年龄"))
    physical_age = int(input("请输入实际年龄"))
    intelligence_quotient = mental_age / physical_age * 100
    if intelligence_quotient >= 140:
        print("天才")
    elif intelligence_quotient >= 120:
        print("超常")
    elif intelligence_quotient >= 110:
        print("聪慧")
    elif intelligence_quotient >= 90:
        print("正常")
    elif intelligence_quotient >= 80:
        print("迟钝")
    else:
        print("低能")

    if input("请输入e则退出：") == "e":
        break
