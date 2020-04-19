"""
写文件
"""

# f = open("file", "w")
f = open("file", "a")  # 追加
# f = open("file", "wb")  # 二进制方式写

# 写入内容
# n = f.write("死亡如风\n".encode())  # 二进制方式写字节串
# print("写入了%d个字符" % n)
#
# f.write("常伴吾身".encode())

# 写入列表内容
l = ["亚索\n", "劫\n"]
f.writelines(l)

f.close()
