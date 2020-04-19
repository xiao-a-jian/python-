"""
re 模块，生成match对象
    一个match对象对应一处匹配内容
    用于获取匹配到内容的详细信息
"""

import re

s = "2020年春，AID 2002 班开课"

pattern = r"\d+"

# it = re.finditer(pattern, s)
#
# for i in it:
#     print(i)  # 得到match对象。  获取结果：print(i.group())

# 匹配开头位置
obj = re.match(pattern, s)
print(obj.group())

# 匹配第一处
obj = re.search(pattern, s)
print(obj.group())








