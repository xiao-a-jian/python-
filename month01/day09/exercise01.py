"""
    画出下列代码内存图
"""

def func01(p1, p2):
    p1 += 1
    p2["铁林"] += 1

int01 = 250
dict01 = {"铁林": 250}
func01(int01, dict01)
print(int01)# 250
print(dict01)# {'铁林': 251}
