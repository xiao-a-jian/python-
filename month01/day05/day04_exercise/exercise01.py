"""
    根据应纳税所得额计算税率与速算扣除数
"""

# money = float(input('请输入应纳税所得额'))
# if money <= 36000:
#     print('税率是%d%%速算扣除数是%d' % (3, 0))
# elif money <= 144000:
#     print('税率是%d%%速算扣除数是%d' % (10, 2520))
# elif money <= 300000:
#     print('税率是%d%%速算扣除数是%d' % (20, 16920))
# elif money <= 420000:
#     print('税率是%d%%速算扣除数是%d' % (25, 31920))
# elif money <= 660000:
#     print('税率是%d%%速算扣除数是%d' % (30, 52920))
# elif money <= 960000:
#     print('税率是%d%%速算扣除数是%d' % (35, 85920))
# else:
#     print('税率是%d%%速算扣除数是%d' % (45, 181920))

money = float(input('请输入应纳税所得额'))
if money <= 36000:
    tax_rate = 0.03
    deduction = 0
elif money <= 144000:
    tax_rate = 0.1
    deduction = 2520
elif money <= 300000:
    tax_rate = 0.2
    deduction = 16920
elif money <= 420000:
    tax_rate = 0.25
    deduction = 31920
elif money <= 660000:
    tax_rate = 0.3
    deduction = 52920
elif money <= 960000:
    tax_rate = 0.35
    deduction = 85920
else:
    tax_rate = 0.45
    deduction = 181920
print('税率是%.0f%%速算扣除数是%d' % (tax_rate * 100, deduction))
