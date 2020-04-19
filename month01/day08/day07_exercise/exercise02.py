'''
存储多个城市的景区与美食
    "北京":
        "景区":"长城","故宫"
        "美食":"烤鸭","豆汁胶圈","炸酱面"
    "四川":
        "景区":"九寨沟","峨眉山"
        "美食":"火锅","兔头"

    1)打印所有城市（一行一个）
    2)打印北京所有美食（一行一个）
    3)打印四川所有景区（一行一个）
    4)打印所有城市的所有景区（一行一个）
    5)为北京添加景区："天坛"
    6)删除四川美食：兔头
'''
"""
list_travel_guide = [
    {
        "北京":{
             "景区": ["长城", "故宫"], 
             "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]
         }
    },
    {
        "四川":{
            "景区": ["九寨沟", "峨眉山"], 
            "美食": ["火锅", "兔头"]
        }
    }
]
for item in list_travel_guide:
    for k_city in item.keys():
        print(k_city)
print()

for item in list_travel_guide:
    if "北京" in item:
        for food in item["北京"]["美食"]:
            print(food)
    print()
    if "四川" in item:
        for scenic_area in item["四川"]["景区"]:
            print(scenic_area)
    print()

for item in list_travel_guide:
    for v_scenic_area in item.values():
        for place in v_scenic_area["景区"]:
            print(place)

for item in list_travel_guide:
    if "北京" in item:
        item["北京"]["景区"].append("天坛")
    elif "四川" in item:
        item["四川"]["美食"].remove("兔头")

for v_scenic_area in list_travel_guide[1][1]:

for item in list_travel_guide:
    print(item)
"""
dict_travel_guide = {
    "北京": {
        "景区": ["长城", "故宫"],
        "美食": ["烤鸭", "豆汁胶圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"],
        "美食": ["火锅", "兔头"]
    }
}
for k_city in dict_travel_guide:
    print(k_city)

for food in dict_travel_guide["北京"]["美食"]:
    print(food)

for scenic_area in dict_travel_guide["四川"]["景区"]:
    print(scenic_area)

for k_city in dict_travel_guide:
    for scenic_area in dict_travel_guide[k_city]["景区"]:
        print(scenic_area)

dict_travel_guide["北京"]["景区"].append("天坛")

dict_travel_guide["四川"]["美食"].remove("兔头")
