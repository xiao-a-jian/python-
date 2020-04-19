# 练习3：改造 day03/exercise04

# def judge_iq(IQ):
#     if IQ >= 140:
#         resaut = "天才"
#     elif IQ >= 120:
#         resaut = "超常"
#     elif IQ >= 110:
#         resaut = "聪慧"
#     elif IQ >= 90:
#         resaut = "正常"
#     elif IQ >= 80:
#         resaut = "迟钝"
#     else:
#         resaut = "低能"
#     return resaut

def judge_iq(IQ):
    """
        判断智商等级
    :param IQ: int类型,智商
    :return: str类型,等级
    """
    if IQ >= 140:
        return "天才"# 如果满足条件,return 返回数据的同时退出函数
    if IQ >= 120:
        return "超常"
    if IQ >= 110:
        return "聪慧"
    if IQ >= 90:
        return "正常"
    if IQ >= 80:
        return "迟钝"
    return "低能"

print(judge_iq(180))