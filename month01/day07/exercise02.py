"""
    在终端中循环录入疫情信息(地区,新增确诊,现有确诊,治愈),
    如果地区名称为空字符,停止录入。

    将所有疫情信息的新增确认数量设置为0

    打印所有疫情信息(一行一个)：
        格式：xxx地区,新增确诊xx,现有确诊xx,治愈xx.

    数据结构：
        {
            "湖北":[114,28216,36167],
            "广东":[0,259,1084],
        }
"""
dict_info = {}
while True:
    epidemic_info_area = input("请输入疫情信息地区：")
    if epidemic_info_area == "":
        break
    new_add_diagnosis = int(input("请输入疫情信息地区新增确诊："))
    diagnosis = int(input("请输入疫情信息现有确诊："))
    cure = int(input("请输入疫情信息现有治愈："))
    dict_info[epidemic_info_area] = [new_add_diagnosis, diagnosis, cure]

for v_epidemic_info in dict_info.values():
    v_epidemic_info[0] = 0

for area_name, epidemic_info in dict_info.items():
    print("%s地区,新增确诊%d,现有确诊%d,治愈%d" % (area_name, epidemic_info[0], epidemic_info[1], epidemic_info[2]))
