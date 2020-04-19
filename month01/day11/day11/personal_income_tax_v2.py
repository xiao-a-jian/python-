"""
    工资计算器

        使用函数,屏蔽实现方式,彰显执行过程
"""

list_salary_before_tax = [30000] * 12

special_deduction = 1000

free_income = 5000

base_pay = 30000

social_insurance = 0

list_tax = None

salary_after_tax = None


def calculate_personal_income_tax():
    """
        计算个人所得税
    """
    global list_tax
    list_tax = []
    for i in range(len(list_salary_before_tax)):
        month = i + 1
        salary_pay_tax = get_salary_pay_tax(social_insurance, month)
        tax = get_tax(salary_pay_tax, list_tax)
        list_tax.append(tax)


def get_salary_pay_tax(social_insurance, month):
    """
        获取需要纳税工资
    :param social_insurance:社保
    :param month:月份
    :return:该月份需要纳税的工资
    """
    # 纳税工资 = 累计税前工资 -累计起征点- 累计专项扣除数- 累计社保
    return sum(
        list_salary_before_tax[:month]) - free_income * month - social_insurance * month - special_deduction * month


def get_tax(salary_pay_tax, list_tax):
    """
        获取当月个税
    :param salary_pay_tax:获取需要纳税工资
    :param list_tax:已缴纳税额列表
    :return:当月个税
    """
    # 个税 = （累计纳税工资 * 预扣率 - 速算扣除数）-累计已缴纳税额
    deduction, tax_rate = get_tax_rate_and_deduction(salary_pay_tax)
    tax = round(salary_pay_tax * tax_rate - deduction - sum(list_tax), 2)
    if tax < 0: tax = 0
    return tax


def get_tax_rate_and_deduction(salary_pay_tax):
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
    return deduction, tax_rate


def calculate_salary_after_tax():
    """
        计算税后工资
    """
    # 税前工资 - 个税 - 社保
    global salary_after_tax
    salary_after_tax = [round(list_salary_before_tax[i] - list_tax[i] - social_insurance, 2)
                        for i in range(len(list_salary_before_tax))]


def calculate_social_insurance():
    """
        获取社保
    """
    # 养老保险：8%；医疗保险：2% 加三元；失业保险：0.2%;公积金：12%。
    global social_insurance
    social_insurance = 3 + base_pay * (0.08 + 0.002 + 0.02 + 0.12)


def get_salary():
    """
        获取工资
    :return:税后工资
    """
    calculate_social_insurance()
    calculate_personal_income_tax()
    calculate_salary_after_tax()
    return salary_after_tax

# 测试
print("税前工资：", list_salary_before_tax)
print("税后工资：", get_salary())
