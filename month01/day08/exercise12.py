# 改造day06/exercise05,定义函数,根据年月,计算天数.
def is_leap_year(year):
    """

    :param year:
    :return:
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_day_by_month(year, month):
    """

    :param year:
    :param month:
    :return:
    """
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


print(get_day_by_month(2020, 2))
