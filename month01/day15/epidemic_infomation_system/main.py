"""
    入口
"""
# import usl
#
# view = usl.EpidemicInformationView()
# view.main()
from usl import EpidemicInformationView

# 入口代码,当前模块只有是主模块,才满足条件。
if __name__ == '__main__':
    # 全局异常处理机制
    # try:
    #     view = EpidemicInformationView()
    #     view.main()
    # except:
    #     print("出错啦")
    view = EpidemicInformationView()
    view.main()
