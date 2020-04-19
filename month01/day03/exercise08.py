"""
    练习:在终端中循环录入年龄,
        如果录入空,则退出循环.
        打印平均年龄(总年龄除以人数)
"""
person_count = 0
sum_of_age = 0
while True:
    str_age = input("请输入年龄：")
    if str_age == "":
        break
    age = int(str_age)
    person_count += 1
    sum_of_age += age
print(sum_of_age / person_count)
