"""
    容器通用操作
    练习:exercise01、exercise02
"""

# 1. 算数运算符 +  *
# + 两个容器拼接
name01 = "大圣"
name01 += "悟空"
print(name01)  # 大圣悟空
# * 容器中元素重复多次
name01 *= 3
print(name01)

# 2. 成员运算 in
print("大圣" in "我是齐天大圣孙悟空")  # True
print("圣孙" in "我是齐天大圣孙悟空")  # True
# 存在但不连续
# 命题："我是孙悟空" 在 "我是齐天大圣孙悟空" 中  结论：假的(不在)
print("我是孙悟空" in "我是齐天大圣孙悟空")  # False
# 命题："我是孙悟空" 不在 "我是齐天大圣孙悟空" 中  结论： 对的(不在)
print("我是孙悟空" not in "我是齐天大圣孙悟空")  # True

message = "我是齐天大圣孙悟空"
# 3. 索引
# 打印第二个字符
print(message[1])
# 打印倒数第三个字符
print(message[-3])
# print(message[99])# IndexError
# print(message[-99])# IndexError

# 4. 切片  [开始:结束:间隔]
# for itme in range(2,5,1):# 生成数字：2 3 4
print(message[2:5:1])  # 齐天大
# for itme in range(5):# 生成数字：01234
print(message[:5])  # 我是齐天大
print(message[:])  # 我是齐天大圣孙悟空
print(message[::2])  # 我齐大孙空
print(message[1:-3])  # 是齐天大圣
print(message[::-1])  # 空悟孙圣大天齐是我
print(message[-4:1:-1])  # 圣大天齐

print(message[:99])  # 我是齐天大圣孙悟空
print(message[:-99:-1])  # 空悟孙圣大天齐是我
print(message[3:1:])  # 空
print(message[1:1])  # 空
