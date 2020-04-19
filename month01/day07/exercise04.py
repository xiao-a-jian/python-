# 练习1:将两个列表，合并为一个字典
# 姓名列表["张无忌","赵敏","周芷若"]
# 房间列表[101,102,103]
list_name = ["张无忌", "赵敏", "周芷若"]
list_room_number = [101, 102, 103]
dict_info = {list_room_number[i]: list_name[i] for i in range(len(list_name))}
print(dict_info)
# 练习2:将上面的字典，key/value颠倒
dict_info = {v: k for k, v in dict_info.items()}
print(dict_info)