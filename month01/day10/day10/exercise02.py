# 调用下列函数

def func01(*args, **kwargs):  # 位置实参 + 关键字实参 数量无限
    print(args)
    print(kwargs)


func01()
func01(34, 34, 4, a=1, b=2)


# 位置形参   位置形参+默认形参  命名关键字形参+默认形参
def func02(p1, p2="", *args, p3=0, **kwargs):
    print(p1)
    print(p2)
    print(args)
    print(p3)
    print(kwargs)


func02(1, 2, 3, 4, p3=5, a=1, b=2)
func02(1)
