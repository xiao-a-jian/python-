"""
    if 真值表达式
        if 变量:
            如果有值则执行当前代码
        作用：可以简洁的判断变量是否有值

    条件表达式
        变量 = 满足条件的值 if 条件 else 不满足条件的值
        根据条件对某个变量进行赋值
    练习:exercise05
"""
# 1.
# 为False的转换： bool(0)  bool(0.0)  bool("")   bool(None)
# 有值为True
content = input("请输入：")
if content:  # content != ""
    print("您输入了内容")

# 2.
# if input("请输入性别：") == "男":
#     sex_value = 1
# else:
#     sex_value = 0

sex_value = 1 if input("请输入性别：") == "男" else 0
