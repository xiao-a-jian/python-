"""
    练习:
        北京一日游的收费标准：
            5人以内按照散客标准，300元/人
            超过5人按照团体标准，280元/人
        根据人数,计算旅游费用.
"""
# person_count = int(input("请输入人数"))
# if person_count <= 5:
#     print("旅游费用为：" + str(person_count * 300))
# else:
#     print("旅游费用为：" + str(person_count * 280))

# 有基础的王棚棚同学答案：
people_number = int(input("请输入人数："))
if 0 < people_number <= 5:
    print(people_number * 300)
elif people_number > 5:
    print(people_number * 280)
else:
    print("人数输入错误！")

# money = people_number * 300 if people_number <= 5 else people_number * 280
# if money > 0:
#     print(money)
# else:
#     print("捣乱呢?")
