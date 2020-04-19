print("""请输入要购买彩票的号码
前五个号码（1-33）
最后一个号码（1-16）
前五个号码中一个五十元
最后一个号码中100元
""")

buy_number = []
while len(buy_number) < 6:
    number = int(input("请输入第%d个号码:" % (len(buy_number) + 1)))
    if number < 0 or number > 34 or number in buy_number:
        print("号码已经存在或号码超过范围请重新输入")
    else:
        buy_number.append(number)

while len(buy_number) < 7:
    number = int(input("请输入第7个号码:"))
    if 1 <= number <= 16:
        buy_number.append(number)

print(buy_number)
