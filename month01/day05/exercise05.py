"""
    在终端中录入疫情省份名称，如果输入空字符串，则停止。
    如果录入的名称已经存在不要再次添加.
    打印所有省份名称(一行一个)
"""
list_provinces = []
count = 0
while True:
    province = input("请输入第%d个省份名称：" % (count + 1))
    if province == "": break
    if province not in list_provinces:
        count += 1
        list_provinces.append(province)

for item in list_provinces:
    print(item)
