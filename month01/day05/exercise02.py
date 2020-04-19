"""
    判断一个字符串是否是回文
        上海自来水来自海上
        打印是回文
             不是回文
"""

# content = "上海自来水来自海上"
content = "山西运煤车煤运西山"
if content == content[::-1]:
    print("是回文")
else:
    print("不是回文")
