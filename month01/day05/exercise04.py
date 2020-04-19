"""
    在终端中录入10个疫情省份的确诊人数
    最后打印人数最多的、最少的、平均人数.（使用内置函数实现）
"""
list_confirmed = []
for item in range(10):
    number = int(input("请输入第%d个省份的疫情人数：" % (item + 1)))
    list_confirmed.append(number)

print(max(list_confirmed))
print(min(list_confirmed))
print(sum(list_confirmed) / len(list_confirmed))
