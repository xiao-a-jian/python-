"""
    定义函数,找出列表中大于10的数字。
        1)传统方法：创建列表存储所有结果,再返回列表.
        2)yield方法：将满足条件的数据返回

    结论：
        函数返回一个数据,使用return
        函数返回多个数据,使用yield
"""


# 方式一：使用容器存储函数结果
# 优势1：可以重复使用结果
# 优势2：获取数据灵活(使用索引、切片)
# 缺点：占用内存过多.
def find_numbers01(list_target):
    list_result = []
    for item in list_target:
        if item > 10:
            list_result.append(item)
    return list_result


list_numbers = [4, 65, 76, 87, 9, 99]
# 传统：立即操作 积极操作
result = find_numbers01(list_numbers)  # 返回数据(列表)

for item in result:
    print(item)


# 方式二：使用生成器返回结果,
# 优势：占用内存过小.
def find_numbers02(list_target):
    for item in list_target:
        if item > 10:
            yield item


# 生成器：延迟操作  惰性操作
result = find_numbers02(list_numbers)  # 返回数据的推算(生成器对象)
# for item in result:
#     print(item)

# 缺点1：一个生成器只能使用一次
# for item in result:
#     print(item)

# 缺点2：获取数据不灵活(不能使用索引、切片)
# print(result[-1])

# 解决： 延迟操作 -> 立即操作
result = tuple(result)

for item in result:
    print(item)
for item in result:
    print(item)
print(result[-1])
