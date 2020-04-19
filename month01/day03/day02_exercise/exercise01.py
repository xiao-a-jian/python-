"""
3. 温度转换器：
    需求：在终端中录入摄氏度,计算华氏度.
    公式：摄氏度 = (华氏度 - 32) 除以 1.8
"""

# 摄氏度 * 1.8 + 32 = 华氏度

centigrade = float(input("请输入摄氏度："))
fahrenheit = centigrade * 1.8 + 32
print(str(centigrade) + "摄氏度=" + str(fahrenheit) + "华氏度")
