"""
    Python程序完整结构
    包(文件夹)
        模块(文件)
            类
                函数
                    语句
    练习:改造信息管理系统day13/epidemic_information_system_v1.py
        将XXXModel,定义到model.py中.
        将XXXView,定义到usl.py中.
             user show layer 用户显示层
        将XXXController,定义到bll.py中.
            business logic layer 业务逻辑层
        将入口代码,定义到main.py中.

"""
# 导入方式一： import 模块名称
# 使用： 模块名称.成员
# 适用性：面向过程(全局变量、函数)
# import module01
#
# module01.func01()

# c01 = module01.MyCalss()
# c01.func03()

# import module01 as m
# m.func01()

# 导入方式二：from 模块 import 成员
# 使用： 直接使用成员名称
# 适用性：面向对象(类)

from module01 import func01
from module02 import func02

func01()
func02()

# 导入方式三：from 模块 import  *
# 使用： 直接使用成员名称
# 适用性：面向对象(类)/导入多个更方便
# 注意：导入的多个模块成员容易发生冲突

# from module01 import *
# from module02 import *
#
# func01()
# func02()
# c01 = MyCalss()
# c01.func03()
