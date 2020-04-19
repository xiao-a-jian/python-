"""
4. 工资计算器：
    需求：在终端中录入税前工资和个税,计算税后工资
    公式：税后工资 = 税前工资 - 社保 - 个税
         社保 = 养老保险8% + 医疗保险2% 加3元 + 失业保险0.2% + 公积金12%
"""
# 获取数据
salary_before_tax = float(input("请输入税前工资："))
personal_tax = float(input("请输入个人所得税："))

# 逻辑计算
# social_insurance = salary_before_tax * 0.08 + salary_before_tax * 0.02 + 3 + salary_before_tax * 0.002 + salary_before_tax * 0.12
social_insurance = 3 + salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12)
salary_after_tax = salary_before_tax - personal_tax - social_insurance

# 显示结果
print("税后工资：" + str(salary_after_tax))
