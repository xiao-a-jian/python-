"""
    练习
"""
# 练习1
list01 = ["北京",["上海","深圳"]]
list02 = list01# 赋值
list01[0] = "首都"# 修改其一
print(list02)# 查看其二
# 练习2
list01 = ["北京",["上海","深圳"]]
# list02 = list01[:]# 切片
list02 = list01.copy()# 浅拷贝
list01[0] = "首都"
list01[1][0] = "天津"
print(list02)
# 练习3
import copy
list01 = ["北京",["上海","深圳"]]
list02 = copy.deepcopy(list01)# 深拷贝
list01[0] = "首都"
list01[1][0] = "天津"
print(list02)

