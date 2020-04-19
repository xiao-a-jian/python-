"""
    个人所得税 版本1
"""

list_salary_before_tax = [30000] * 12  # 税前收入列表
free_income = 5000  # 免税收入(起征点)
special_deduction = 1000  # 专项扣除数
base_pay = 30000
social_insurance = 3 + base_pay * (0.08 + 0.002 + 0.02 + 0.12)
list_tax = []  # 个税列表

for i in range(len(list_salary_before_tax)):
    i += 1
    # 公式一：累计纳税工资 = 累计税前工资 -累计起征点- 累计专项扣除数- 累计社保
    salary_pay_tax = sum(list_salary_before_tax[:i]) - free_income * i - special_deduction * i - social_insurance * i
    # 计算税率和速算扣除数
    if salary_pay_tax < 36000:
        tax_rate = 0.03
        deduction = 0
    elif salary_pay_tax <= 144000:
        tax_rate = 0.1
        deduction = 2520
    elif salary_pay_tax <= 300000:
        tax_rate = 0.2
        deduction = 16920
    elif salary_pay_tax <= 420000:
        tax_rate = 0.25
        deduction = 31920
    elif salary_pay_tax <= 660000:
        tax_rate = 0.3
        deduction = 52920
    elif salary_pay_tax <= 960000:
        tax_rate = 0.35
        deduction = 85920
    else:
        tax_rate = 0.45
        deduction = 181920
    # 公式二：个税 = （累计纳税工资*税率-速算扣除数）-累计已缴纳税额
    tax = round(salary_pay_tax * tax_rate - deduction - sum(list_tax), 2)
    # 如果本月应预扣缴纳额为负,暂不扣税.
    if tax < 0: tax = 0
    list_tax.append(tax)

print(list_tax)
