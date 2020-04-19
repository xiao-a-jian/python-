'''
    录入并输出姓名及爱好
    数据结构
        {
            姓名1:[喜好1,喜好2,喜好3],
            姓名2:[喜好4,喜好5,喜好6]
        }
'''
dict_hobbies = {}
while True:
    name = input("请输入姓名：")
    hobbies = input("请输入爱好：")
    dict_hobbies[name] = hobbies.split(" ")
    if input("按e退出：") == "e":
        break

for k_name, v_hobbies in dict_hobbies.items():
    print("%s的爱好是：" % k_name, end="")
    for item_hobby in v_hobbies:
        print(item_hobby, end="、")
    print()
