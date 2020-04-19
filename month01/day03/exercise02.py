"""
    练习:输入课程阶段数,显示课程名称
    一 --> Python语言核心编程
    二 --> Python高级软件技术
    三 --> Web 全栈
    四 --> 网络爬虫
    五 --> 数据分析、人工智能
"""
stage = input("请输入阶段数（大写数字）：")
# 如果前面条件满足,后面条件依然判断
# if stage == "一":
#     print("Python语言核心编程")
# if stage == "二":
#   print("Python高级软件技术")
# if stage == "三":
#   print("web全栈")
# if stage == "四":
#   print("网络爬虫")
# if stage == "五":
#     print("数据分析，人工智能")

if stage == "一":
    print("Python语言核心编程")
elif stage == "二":
    print("Python高级软件技术")
elif stage == "三":
    print("web全栈")
elif stage == "四":
    print("网络爬虫")
elif stage == "五":
    print("数据分析，人工智能")
else:
    print("输入有误！")
