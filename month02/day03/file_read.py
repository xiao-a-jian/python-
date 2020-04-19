"""
文件读取示例
"""

f = open("file", "rb")

# 一次性读取文件
# data = f.read()
# print("数据：", data)

# 循环读取文件
# while True:
#     data = f.read(10)  # 每次读取100个字节，读到文件结尾后会返回空字符串
#     if not data:
#         break
#     print(data)

# 行读取
# data=f.readline(5)  # 最多读取5字符
# print(data)
# data=f.readline()
# print(data)

# 读取多行
# data = f.readlines()
# print(data)

# 迭代属性，每次读取一行
for line in f:
    print(line)


f.close()
