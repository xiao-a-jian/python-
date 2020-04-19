"""
    元组
"""

# 1. 创建
tuple01 = ()
tuple01 = ("悟空", "唐僧")

tuple02 = tuple()
list02 = ["北京", "上海"]
tuple02 = tuple(list02)  # 预留空间 --> 按需分配

tuple03 = (10)  # int
# 如果元组中只有一个元素,必须最后加逗号
tuple03 = (10,)  # tuple
tuple03 = ("a")  # str
print(type(tuple03))  # <class 'str'>

# 2. 定位
print(tuple01[0])
print(tuple01[:])  # 通过切片获取元素,会创建新元组

# 3. for
for item in tuple01:
    print(item)

for i in range(len(tuple01) - 1, -1, -1):
    print(tuple01[i])
