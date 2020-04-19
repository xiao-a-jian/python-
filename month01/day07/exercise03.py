"""
    在终端中循环录入疫情信息(地区,新增确诊,现有确诊,治愈),
    如果地区名称为空字符,停止录入。

    打印所有疫情信息(一行一个)：
        格式：xxx地区,新增确诊xx,现有确诊xx,治愈xx.

    数据结构：
        [
            {"area":"湖北","new_diagnosis":114,"diagnosis":28216,"cure":36167},
            {"area":"广东","new_diagnosis":0,"diagnosis":259,"cure":1084},
        ]

    总结：
        列表：
            优点：因为根据索引获取元素,所以查找更为灵活(第一个、最后一个...)
            缺点：查找速度不如字典快,根据索引查找代码可读性不高
            适用性：存储单一维度的数据(疫情信息)
        字典：
            优点：因为根据键获取元素,所以查找速度快、代码可读性高.
            缺点：获取元素不如列表灵活
            适用性：存储多个维度的数据(地区、新增、确诊、治愈)

"""

list_information = []
while True:
    area = input("请输入地区名称:")
    if not area:
        break
    else:
        definite = int(input("请输入新增确诊人数:"))
        existing = int(input("请输入现有确诊人数:"))
        healing = int(input("请输入治愈人数:"))
        epidemic_information = {}
        epidemic_information["area"] = area
        epidemic_information["new_diagnosis"] = definite
        epidemic_information["diagnosis"] = existing
        epidemic_information["cure"] = healing
        list_information.append(epidemic_information)

for dict_info in list_information:
    print("%s地区,新增确诊%d,现有确诊%d,治愈%d" %
          (dict_info["area"], dict_info["new_diagnosis"],
           dict_info["diagnosis"], dict_info["cure"]))
