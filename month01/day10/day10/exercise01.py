# 练习：定义数值累乘函数
# 2,3,5,6 -->  2*3*5*6
# 2,3     -->  2*3

def sum_mult(*args):
    sum = 1
    for item in args:
        sum *= item
    return sum

print(sum_mult(23,43,43,5,6,76))

