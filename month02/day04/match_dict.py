import re

s = "jkdsalfdhfk"
pattern = "(kd)sa(?P<dog>lf)"

obj = re.search(pattern, s)  # s[1:7]
print(obj.span())  # (1, 7)
print(obj.groupdict())  # {'dog': 'lf'}
print(obj.groups())  # ('kd', 'lf')
print(obj.group(2))  # lf






