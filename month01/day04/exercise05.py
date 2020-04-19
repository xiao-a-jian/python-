"""
    练习1：在终端中录入一个内容,循环打印每个文字的编码.
    练习2：循环录入编码,打印文字.直到输入空字符串,停止。
"""
name = input('请输入你的名字:')
for letter in name:
    number = ord(letter)
    # 缩进决定的是执行时机
    print(number)

while True:
    code = input("输入编码：")
    if code:
        print(chr(int(code)))
    else:
        break
