"""
    字典dict
    练习:exercise01~03
"""
# 创建
dict01 = {10001: "金海", 10002: "铁林", 10003: "徐天"}

# 序列 --> 字典:一分为二
# dict02 = dict([(10001,"金海"), [10002, "铁林"], "徐天"])
list01 = [(10001, "金海"), (10002, "铁林"), (10003, "徐天")]
dict02 = dict(list01)

# 添加(字典不存在该key)
if 10004 not in dict01:
    dict01[10004] = "田丹"

# 定位  根据key
# -- 读取
print(dict01[10004])
# -- 修改(字典存在该key)
if 10004 in dict01:
    dict01[10004] = "丹丹"

# 删除
del dict01[10002]

# 循环
# -- 遍历所有key
for key in dict01:
    print(key)
    print(dict01[key])

# -- 遍历所有value
for value in dict01.values():
    print(value)

# -- 遍历所有key,value
# for item in dict01.items():
#     print(item[0])
#     print(item[1])
for k,v in dict01.items():
    print(k)
    print(v)



