# 练习1：迭代元组(34,5,6,7)
# 练习2：迭代字典 {"a":1,"b":2,"c":3}
#       不使用for循环,获取字典中所有键值对
dict01 = {"a": 1, "b": 2, "c": 3}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
