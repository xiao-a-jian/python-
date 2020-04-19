"""
    for 循环
        for 变量名 in 容器:
            循环体

    while：根据条件重复
        经典案例：折纸到珠穆朗玛峰的高度

    for：适合获取容器中的元素
        for + range：根据次数重复
        经典案例：累加1到100之间的整数

    练习:exercise02
"""
message = "我是齐天大圣孙悟空"
for item in message:
    print(item)

for item in message:
    item = "圣"  # 修改循环变量,没有修改字符串中的字符
print(message)

# 在字符串中查找某个文字,如果存在打印该文字,不存在提示"没找到"
name = "我是齐天大圣孙悟空"
for item in name:
    if item == "圣":
        print(item)
        break
else:
    print("没找到")
