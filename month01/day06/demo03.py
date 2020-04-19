"""
    str -->  list

    列表 = “a-b-c-d”.split(“分隔符”)
"""
# 需求：将一个字符串描述的多个信息分别提取出来(列表)
names = "齐天大圣-猪八戒-唐僧"
list_names = names.split("-")
for item in list_names:
    print(item)

