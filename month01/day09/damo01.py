"""
    函数内存分配
"""


# 1. 程序自上而下执行,将函数定义,存储到代码区(函数内部语句不执行).
def func01():
    a = 100

# 2. 调用函数时会在内存中开辟一块空间(栈帧),存储函数内部创建的变量
func01()

# 3. 函数执行后,该空间(栈帧)立即释放

# 结论：
# 不可变类型的数据传参时，函数内部不会改变原数据的值。
# 可变类型的数据传参时，函数内部可以改变原数据。
def func02(p1, p2):
    p1 = "孙悟空"# 修改的是栈帧中变量p1存储的地址（没有修改传入的字符串）
    p2[0] = "猪八戒" # 修改传入容器存储的数据地址

str01 = "悟空"# 不可变
list01 = ["八戒"]# 可变
func02(str01, list01)
print(str01)# 悟空
print(list01)# ['猪八戒']
