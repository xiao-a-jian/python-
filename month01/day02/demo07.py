"""
    bool 运算
        int 类型: 10  20 -5 ...
     1. bool 类型:真True  假False
            命题：带有判断性质的陈述句
                 我是男人

        比较运算符：>  <  >=  <=   等于==   不等于!=
            结论就是bool类型
    练习:exercise06.py
        exercise07.py
"""
# 2. 比较运算符
# sex = input("请输入你的性别：")
# result = sex == "男人"
# print("结论是：" + str(result))

number01 = 10
number02 = 20
result = number01 > number02  # 变量number01 大于 变量number02
print(result)
print(0 <= number01 <= 100)  # 变量number01在10到100之间

# 3. 逻辑运算符
#  判断2个命题之间关系
#  1) 与(并且) and
# 　　总结：一假俱假　表达：必须都得满足
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False
# 条件：天黑了　and　完成作业
# 那么：看电视
# 2) 或(或者)　or
# 　 总结：一真俱真　表达：有一个满足就行
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False
# 条件：体重超重　or  血脂高　
# 那么：去运动
# 3) 非 not
#    总结：取反
print(not True)

