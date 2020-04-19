# 练习1:
# 匀变速直线运动的速度与位移公式：
# 位移 = 初速度 × 时间 + 0.5 * 加速度 * 时间的平方
# 已知(在终端中录入)：位移、时间、初速度
# 计算：加速度
distance = float(input("请输入距离："))
initial_velocity = float(input("请输入初速度："))
time = float(input("请输入时间："))
# (位移 - 初速度 × 时间)  × 2 / 时间的平方 =   加速度
accelerated_speed = (distance - initial_velocity * time) * 2 / time ** 2
print("加速度是：" + str(accelerated_speed))

# 练习2:在控制台中录入一个秒，计算是几小时零几分钟零几秒钟.
total_second = int(input("请输入总秒数："))
second = total_second % 60
hour = total_second / 60 // 60
minute = total_second // 60 % 60
print(str(hour) + "小时零" + str(minute) + "分钟零" + str(second) + "秒钟")

# 练习3：在终端中获取一个月份，年份，打印相应的天数.
year = int(input("请输入年份："))
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("月份有误")
elif month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("29天")
    else:
        print("28天")
elif month == 4 or month == 6 or month == 9 or month == 11:
# elif month == 4 or  bool(6) or 9 or 11:
    print("30天")
else:  # 1 3 5 7 8 10 12
    print("31天")

"""
练习4：
    魏老师很不幸买了一箱有虫子(1)的苹果
    虫子吃完一个苹果再吃另外一个苹果
    在终端中输入苹果数量(个),虫子吃苹果的速度(小时/个),经过时间(小时)
    请打印没有被虫子吃过的苹果数量（最小也是0）
"""
total_count = int(input("请输入苹果总数："))
speed = float(input("虫子吃苹果的速度(小时/个):"))
duration = float(input("请输入经过时间(小时):"))
remain_count = int(total_count - duration / speed)
if remain_count > 0:
    print("没有被虫子吃过的苹果数:" + str(remain_count))
else:
    print("没有苹果啦")

"""
练习5：
    商品优惠
    打折策略：如果vip客户，消费小于500,享受85折
                        否则享受8折
            否则，消费大于800,享受9折
                 否则原价
    根据账户类型和消费金额，计算折扣.
"""
account_type = input("请输入账户类型：")
money = float(input("请输入消费金额："))
if account_type == "vip":
    if money < 500:
        print("享受85折扣")
    else:
        print("享受8折扣")
else:
    if money > 800:
        print("享受9折扣")
    else:
        print("原价购买")

# 练习6：一张纸的厚度是0.01毫米
# 请计算，对折多少次超过珠穆朗玛峰(8844.43米).
# 数据：厚度   珠穆朗玛峰高度
# 算法：厚度 *= 2    比较  珠穆朗玛峰高度

thickness = 1e-5
# thickness = 0.00001
# thickness = 0.01 / 1000
count = 0
while thickness < 8844.43:
    thickness *= 2
    count += 1
    print("第" + str(count) + "次对折,厚度是" + str(thickness) + ".")

print(count)# 30
