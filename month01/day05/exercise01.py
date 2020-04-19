"""
    练习
"""
# 1. 打印第一个字符、打印最后一个字符、打印中间字符
# 2. 打印字前三个符、打印后三个字符
# 3. 命题：金海在字符串content中
# 4. 命题：京师监狱不在字符串content中
# 5. 通过切片打印“京师监狱狱长”
# 6. 通过切片打印“长狱狱监师京”
# 7. 通过切片打印“我师狱海”
# 8. 倒序打印字符

content = "我是京师监狱狱长金海。"
print(content[0])
print(content[-1])
print(content[len(content) // 2])
print(content[:3])
print(content[-3:])
print("金海" in content)
print("京师监狱" not in content)
print(content[2:-3])
print(content[-4:1:-1])
print(content[::3])
print(content[::-1])
