"""
    包
"""
# 方式一：import 路径.模块
# import package01.package02.m02 as m
#
# m.func02()

# 方式二：from 路径.模块 import func02
# from package01.package02.m02 import func02
# func02()

# from 路径 import 模块
# from package01.package02 import m02
# m02.func02()

# 方式三：from 路径.模块 import *
# from package01.package02.m02 import *
# func02()

# from 路径 import *
# 此时必须要在包的__init__.py文件中,设置__all__.
from package01.package02 import *

m02.func02()
# m03.func03()
