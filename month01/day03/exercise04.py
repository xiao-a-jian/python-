"""
    智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
    天才：140以上（包含）
    超常：120-139之间（包含）
    聪慧：110-119之间（包含）
    正常：90-109之间（包含）
    迟钝：80-89之间（包含）
    低能：80以下
    根据心理年龄与实际年龄，打印智商等级
"""
# MA = float(input("请输入心理年龄:"))
# CA = float(input("请输入实际年龄:"))
# IQ = MA / CA * 100

# if 0 < IQ < 80:
#     print("弱智")
# elif 80 < IQ <= 89:# 因为有elif,其中el表达以上条件不满足(IQ < 80),所以不用区间判断(80 < IQ)
#     print("迟钝")
# elif 89 < IQ <= 109:
#     print("正常")
# elif 109 < IQ <= 119:
#     print("聪慧")
# elif 119 < IQ <= 139:
#     print("超常")
# elif 139 < IQ:
#     print("天才")

mental_age = int(input("请输入心理年龄"))
physical_age = int(input("请输入实际年龄"))
intelligence_quotient = mental_age / physical_age * 100
if intelligence_quotient >= 140:
    print("天才")
elif intelligence_quotient >= 120:  # 因为有elif,其中el表达以上条件不满足(IQ >=140),所以不用区间判断(IQ <=139)
    print("超常")
elif intelligence_quotient >= 110:
    print("聪慧")
elif intelligence_quotient >= 90:
    print("正常")
elif intelligence_quotient >= 80:
    print("迟钝")
else:
    print("低能")
