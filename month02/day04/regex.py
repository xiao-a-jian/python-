"""
re 模块
"""
import re

s = "Alex:1996,Sunny:1998"
# pattern = r"(\w+):\d+"  # ['Alex', 'Sunny']
pattern = r"(\w+):(\d+)"  # [('Alex', '1996'), ('Sunny', '1998')]
# re直接调用
l = re.findall(pattern, s)
print(l)
# 生成正则表达式对象
regex = re.compile(pattern)
l = regex.findall(s, 0, 12)  # 对[('Alex', '1996'), ('Sunny', '1998')]进行s[0:12]切片得到[('Alex', '1996')]
print(l)

# 使用正则表达式匹配内容分割字符串
l = re.split(r"\W+", s, 2)
print(l)

# 替换目标字符串中匹配到的内容
s = re.sub(r"\W+", "##", s, 2)
print(s)
