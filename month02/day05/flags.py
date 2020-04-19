import re

s = """Hello
北京"""

l = re.findall(r"\w+",s,flags=re.A)
print(l)




