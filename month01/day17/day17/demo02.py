"""
    函数式编程思想
        分
        隔
        做
"""

list01 = [4,True,65,"76",7,18.6,9,19]
# 需求1：定义函数,找出所有的整数
def find01():
    for item in list01:
        if type(item) == int:
            yield item

# 需求2：定义函数,找出所有的大于10的数字
def find02():
    for item in list01:
        if type(item) != str and item > 10:
            yield item

# 1. “封装”：分 --> 函数
# 变化...
def condition01(item):
    return type(item) == int

def condition02(item):
    return type(item) != str and item > 10

# 不变
# 2. “继承”：隔 --> (函数类型的)形参
def find(func):
    for item in list01:
        # if  type(item) == int  :
        # if  condition01(item)  :
        if  func(item)  :
            yield item

# 3. “多态”：做          1. 调用父  2. 重写  3. 创建子
for item in find(condition01):
    print(item)