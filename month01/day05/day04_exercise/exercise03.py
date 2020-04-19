"""
    一个小球从100m的高度落下,每次都弹回原高度一半
    (1)计算弹起多少次,最终落地.(最小弹起高度0.01m)
    (2)全过程经历多少米
    数据:高度heigh
    算法：heigh /=2
"""
# heigh=100
# count=0
# meter=0
# while True:
#     count+=1
#     heigh/=2
#     meter+=heigh
#     if heigh<0.01:
#         break
# print(heigh)
# print('一共弹起了'+str(count)+'次')
# print('全过程一共经历了'+str(meter*2+100)+'米')

heigh = 100
count = 0
distance = heigh
# 弹起前的高度 heigh
# 弹起后的高度 heigh /2
while heigh / 2 >= 0.01:
    # 模拟弹起
    count += 1
    heigh /= 2
    distance += heigh * 2  # 累加起、落高度
    # print("第%d次弹起来的高度是%f"%(count,heigh))

print('一共弹起了%d次' % count)
print('全过程一共经历了%.2f米' % distance)
