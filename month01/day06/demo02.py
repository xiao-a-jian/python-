"""
    list  -->  str

    字符串 = "连接符".join(列表)
"""
# 需求：根据xx逻辑循环拼接一个字符串
# 核心思想：不要使用不可变的字符串+=
#         要可变的列表append
# 启发：再对不可变对象进行频繁修改,就先存储到可变对象中,最后再还原为不可变对象。

str_result = ""   # 不可变
for itme in range(10):
    #             ""   + "0"   -->  "0"
    #             "0"   + "1"   -->  "01"
    #             "01"   + "2"   -->  "012"
    # 每次循环都会产生一个新字符串对象,替换变量存储的地址（垃圾）
    str_result = str_result + str(itme)
print(str_result)


list_result = []  # 可变
for itme in range(10):
    # 像列表中添加当前字符串的地址
    list_result.append(str(itme))
str_result = "".join(list_result)
print(str_result)






