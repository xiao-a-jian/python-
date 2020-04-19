"""
    练习:
        定义函数,计算收费标准
            5人以内按照散客标准，300元/人
            超过5人按照团体标准，280元/人
        根据人数,计算旅游费用.
        day03/exercise01
"""


def calculate_charging_standard(tourist_number):
    """

    :param tourist_number:
    :return:
    """
    return tourist_number * 300 if tourist_number <= 5 else tourist_number * 280


print(calculate_charging_standard(10))
