"""

"""

list01 = ["金海", "铁林", "徐天"]
list02 = list01  # 将list01存储的列表地址赋值给list02(列表只有一个)
list01.insert(1, "大英子")  #
list02.remove("金海")
print(list01)  # ['大英子', '铁林', '徐天']
print(list02)  # ['大英子', '铁林', '徐天']

list03 = ["金海", "铁林", "徐天"]
list04 = list03[:]
list03[0] = "狱长"
list04[-2:] = ["少将", "警察"]
print(list03)
print(list04)
