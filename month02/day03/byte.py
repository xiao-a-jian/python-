"""
字节串类型
 注意：所有的字符串都能转换为字节串
      字节串不一定都能转换为字符串
"""
s = "Hello world"
print(type(s))
print(s)
# 定义字节串
s = b"Hello world"  # 表示在内存中存储一个二进制数据，这个二进制数据是 Hello world
print(type(s))
print(s)
# 中文或者变量
a = "你好"
s = a.encode()
print(type(s))
print(s)

# 字节串转换为字符串
print(s.decode())
