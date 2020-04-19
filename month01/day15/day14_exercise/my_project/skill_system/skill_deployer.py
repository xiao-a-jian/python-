# 导入是否成功的唯一条件：
# 导入路径 + 系统路径 = 真实路径
# 第一次执行的模块称之为主模块，所在目录称之为主目录.

import sys
print(sys.path)
sys.path.append("/home/tarena/QTX/month01/day15/day14_exercise/my_project")

from common.list_helper import ListHelper


class SkillDeployer:
    def func02(self):
        print("SkillDeployer -- func02")


ListHelper.func03()
