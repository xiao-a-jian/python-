"""
    while 循环
        循环计数
            三大要素：开始值、结束值、增减量
            开始值
            while 对结束值的处理:
                循环体
                增减量
    练习:exercise07~08
"""

# 1. 在循环以前定义计数器
count = 0
# 2. 根据计数器判断循环条件
while count < 5:
    print("跑圈,计数器:" + str(count))
    # 3. 在循环以内更新计数器
    count += 1
print("跑了多少圈：" + str(count))
