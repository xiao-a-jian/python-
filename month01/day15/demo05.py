"""
    可迭代对象
"""
list01 = [35, 5, 65, 7, 8]
# for item in list01:
#     print(item)

# 参与for循环的条件：
#   对象具有__iter__方法

# for 循环原理：
# 1. 获取迭代器
iterator = list01.__iter__()
# 2. 获取下一个元素
while True:
    try:
        itme = iterator.__next__()
        print(itme)
    # 3. 异常处理
    except StopIteration:
        break
