"""
    变量
        程序运行在哪里？ -- 内存
        程序在处理什么？ -- 数据
        价值：在内存中操作数据的技术
        语法：
            变量名称 = 数据
            变量名称1,变量名称2 = 数据1,数据2
            变量名称1 = 变量名称2 = 数据
        赋值号=: 将右边的结果复制一份给左边

        删除变量：
            del 变量名称
            del 变量名称1,变量名称2
    练习:exercise03.py

"""

# 创建单个变量
person_name01 = "金海"
# 用多个数据，创建多个变量
person_name02, person_name03 = "铁林", "徐天"
# 用单个数据，创建多个变量
person_name04 = person_name05 = "柳如丝"

del person_name04
del person_name01,person_name02

person_name06 = person_name05 + person_name05