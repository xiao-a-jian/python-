# 练习:累加10 -- 60 之间,个位不是3/5/8的整数和。
sum = 0
for item in range(10, 61):
    value = item % 10
    # 如果个位是3或者5或者8则跳过
    if value == 3 or value == 5 or value == 8:
        continue
    sum += item
print(sum)
