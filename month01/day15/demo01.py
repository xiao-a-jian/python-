"""
    模块变量
"""
# 如果当前是主模块(第一次执行的模块),显示 __main__
# 否则(当前是被导入的),显示真实模块名
print(__name__)

# 执行被导入模块的代码（只执行一次）
import day14_exercise.skill_system
import day14_exercise.skill_system
