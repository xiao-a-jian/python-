"""
    太阳系
    太阳 "水星" "金星" "地球" "火星" "木星" "土星" "天王星" "海王星"
    练习1:定义列表存储4个行星 "水星" "金星"  "火星" "木星"
    练习2:插入"地球"、追加"土星" "天王星" "海王星"
    练习3:打印距离太阳最近、最远的行星(第一个和最后一个元素)
    练习4:打印太阳到地球之间的行星(前两个行星)
    练习5:删除"海王星",删除第四个行星
    练习6:倒序打印所有行星(一行一个)
"""
list_solar_system = ["水星", "金星", "火星", "木星"]
list_solar_system.insert(2, "地球")
# list_solar_system.append("土星")
# list_solar_system.append("海王星")
# list_solar_system.append("天王星")
# list_solar_system.extend(["土星", "海王星", "天王星"])
list_solar_system[len(list_solar_system):] = ["土星", "海王星", "天王星"]
print(list_solar_system)
print(list_solar_system[0])
print(list_solar_system[-1])
print(list_solar_system[0:2])
list_solar_system.remove("海王星")
del list_solar_system[3]
for i in range(len(list_solar_system) - 1, - 1, - 1):
    print(list_solar_system[i])
