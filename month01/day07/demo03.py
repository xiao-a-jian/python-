"""
    集合set
        相当于只有key没有value的字典
        作用：
            去重复
            数学运算
    练习:exercise05
"""

# 创建
set01 = {"张无忌", "赵敏", "周芷若"}
# 备注：{ } 是字典不是集合
set02 = set()
list_name = ["张无忌", "赵敏", "周芷若", "张无忌", "周芷若"]
set02 = set(list_name)
print(set02)  # {'周芷若', '赵敏', '张无忌'}  去重复

# 添加
set01.add("小昭")
set01.add("赵敏")  # 存储相同元素无效

# 定位（没有）

# 删除
set01.remove("赵敏")  # 删除没有的元素会报错KeyError
print(set01)

# 循环
for item in set01:
    print(item)

# 数学运算
set03 = {1, 2, 3}
set04 = {2, 3, 4}
# 交集
print(set03 & set04)  # {2, 3}
# 并集
print(set03 | set04)  # {1, 2, 3, 4}
# 补集
print(set03 ^ set04)  # {1, 4}
print(set03 - set04)  # {1}
print(set04 - set03)  # {4}
# 子集  超集
set05 = {2, 3}
print(set05 < set03)  # True
print(set03 > set05)  # True
