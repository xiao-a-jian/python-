# 练习1:
# 使用列表推导式生成1--50之间能被3或者5整除的数字
list01 = [item for item in range(1, 51) if item % 5 == 0 or item % 3 == 0]
print(list01)

# 练习2：
# 使用列表推导式生成5 -- 100 之间的数字平方
list02 = [item ** 2 for item in range(5, 101)]
print(list02)
