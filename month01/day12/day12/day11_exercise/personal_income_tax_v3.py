"""
    工资计算器
"""


class SalaryCalculator:
    """
        工资计算器
    """

    # 免税收入
    free_income = 5000

    def __init__(self, list_salary_before_tax, *, special_deduction=0, base_pay=3613):
        """
            创建工资计算器对象
        :param list_salary_before_tax:税前工资列表
        :param special_deduction:专项扣除
        :param base_pay:社保缴纳基数
        """
        self.list_salary_before_tax = list_salary_before_tax
        self.special_deduction = special_deduction
        self.base_pay = base_pay
        # 社保是根据base_pay计算而来,不应由外部干预(配以只读属性)
        self.__social_insurance = 0
        self.__list_tax = None
        self.__list_salary_after_tax = None
        self.get_salary()

    @property
    def list_salary_before_tax(self):
        """
            税前工资列表
        """
        return self.__list_salary_before_tax

    @list_salary_before_tax.setter
    def list_salary_before_tax(self, value):
        """
            税前工资列表
        """
        # 限制每月薪资都是正数
        for i in range(len(value)):
            if value[i] < 0:
                value[i] = 0
        self.__list_salary_before_tax = value

    @property
    def special_deduction(self):
        """
            专项扣除
        """
        return self.__special_deduction

    @special_deduction.setter
    def special_deduction(self, value):
        """
            专项扣除
        """
        if value < 0: value = 0
        self.__special_deduction = value

    @property
    def base_pay(self):
        """
           社保缴费基数
        """
        return self.__base_pay

    @base_pay.setter
    def base_pay(self, value):
        """
           社保缴费基数
        """
        if 3613 <= value <= 23565:
            self.__base_pay = value
        else:
            raise Exception("社保缴费基数超过国家限制范围")

    @property
    def social_insurance(self):
        """
           个人社保缴纳费用
        """
        return self.__social_insurance

    @property
    def list_tax(self):
        """
           个税列表
        """
        return self.__list_tax

    @property
    def list_salary_after_tax(self):
        """
           税后工资列表
        """
        return self.__list_salary_after_tax

    def __calculate_personal_income_tax(self):
        """
            计算个人所得税
        """
        self.__list_tax = []
        for i in range(len(self.list_salary_before_tax)):
            month = i + 1
            salary_pay_tax = self.__get_salary_pay_tax(self.social_insurance, month)
            tax = self.__get_tax(salary_pay_tax)
            self.__list_tax.append(tax)

    def __get_salary_pay_tax(self, social_insurance, month):
        """
            获取需要纳税工资
        :param social_insurance: 社保
        :param month: 月份
        :return:该月份需要纳税的工资
        """
        # 纳税工资 = 累计税前工资 -累计起征点- 累计专项扣除数- 累计社保
        return sum(
            self.list_salary_before_tax[
            :month]) - SalaryCalculator.free_income * month - social_insurance * month - self.special_deduction * month

    def __get_tax(self, salary_pay_tax):
        """
        获取当月个税
        :param
        salary_pay_tax: 获取需要纳税工资
        :param
        list_tax: 已缴纳税额列表
        :return:当月个税
        """
        # 个税 = （累计纳税工资 * 预扣率 - 速算扣除数）-累计已缴纳税额
        deduction, tax_rate = self.__get_tax_rate_and_deduction(salary_pay_tax)
        tax = round(salary_pay_tax * tax_rate - deduction - sum(self.__list_tax), 2)
        if tax < 0: tax = 0
        return tax

    def __get_tax_rate_and_deduction(self, salary_pay_tax):
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

    def __calculate_salary_after_tax(self):
        """
        计算税后工资
        """
        self.__list_salary_after_tax = [
            round(self.__list_salary_before_tax[i] - self.__list_tax[i] - self.__social_insurance, 2)
            for i in range(len(self.__list_salary_before_tax))]

    def __calculate_social_insurance(self):
        """
        获取社保
        """
        # 养老保险：8%；医疗保险：2% 加三元；失业保险：0.2%;公积金：12%。
        self.__social_insurance = 3 + self.__base_pay * (0.08 + 0.002 + 0.02 + 0.12)

    def get_salary(self):
        """
            获取工资
        :return:税后工资
        """
        self.__calculate_social_insurance()
        self.__calculate_personal_income_tax()
        self.__calculate_salary_after_tax()
        return self.list_salary_after_tax


# ----------------------------测试----------------------------
# 体会面向过程与面向对象的区别:
# 1. 面向过程使用全局变量,在内存中只存在一份
# 2. 面向对象使用实例变量,在内存中每个对象都存在一份
# 3. 面向对象可以表达多个个体的不同

def print_salary_information(calculator):
    print("税前工资：", calculator.list_salary_before_tax)
    print("税后工资：", calculator.list_salary_after_tax)
    print("社保：", calculator.social_insurance)
    print("个税：", calculator.list_tax)


# calculator_of_jh = SalaryCalculator([30000] * 12, 1000, 20000)

calculator_of_jh = SalaryCalculator([30000] * 12, special_deduction=1000, base_pay=20000)

print("金海薪资情况：")
print_salary_information(calculator_of_jh)

calculator_xt = SalaryCalculator([10000] * 12, base_pay=10000)
print("徐天薪资情况：")
print_salary_information(calculator_xt)

print("金海调整社保缴纳基数后薪资情况：")
calculator_of_jh.base_pay = 3613
calculator_of_jh.get_salary()
print_salary_information(calculator_of_jh)
