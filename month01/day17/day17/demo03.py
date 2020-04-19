"""
    lambda 表达式
        匿名方法
"""

# 1. 有参数有返回值
# def func01(p1, p2):
#     return p1 + p2
#
#
# print(func01(1, 2))


func01 = lambda p1, p2: p1 + p2

print(func01(1, 2))

# 2. 无参数有返回值
# def func02():
#     return 1000
#
# print(func02())


func02 = lambda: 1000
print(func02())

# 3. 有参数无返回值
# def func03(p1, p2):
#     print(p1 + p2)
#
# func03(1, 2)

func03 = lambda p1, p2: print(p1 + p2)

func03(1, 2)

# 4. 无参数无返回值
# def func04():
#     print("中国加油,武汉加油")
#
# func04()


func04 = lambda: print("中国加油,武汉加油")

func04()


# 5. lambda 表达式不能赋值
def func05(list_target):
    list_target[0] = 10


list01 = [1]
func05(list01)
print(list01[0])  # ?

# func05 = lambda list_target:list_target[0] = 10

# 6.lambda 表达式只能有一句话
def func06():
    for item in range(3):
        print(item)

func06()

# func06 = lambda:for item in range(3): print(item)
