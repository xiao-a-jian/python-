# 练习1:
# cure_rate = 16.2345
# print("治愈比例为：16.23%")
# 练习2:
# print("70秒是1分钟零10秒")
# 练习３:
# print("老魏今年46岁,兜里有17.5元")

# 练习1：
cure_rate = 16.2345
# 两个%%，会显示一个%
print("治愈率为%.2f%%" % (cure_rate))
# 练习2：
time = 70
minute = time // 60
second = time % 60
print("%d秒是%d分钟零%d秒" % (time, minute, second))
# 练习3：
name = "老魏"
age = 46
money = 17.5
print("%s今年%s岁兜里有%.1f元" % (name, age, money))
