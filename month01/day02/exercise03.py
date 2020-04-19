"""
    画出下列代码内存图
"""
# 练习1
province_name01 = "湖北"
province_name02 = "湖南"
province_name02 = "河南"
province_name03 = province_name02
print(province_name03)  # ?河南

# 练习2
city_name01,city_name02 = "北京","上海"
city_name03 = city_name01 + city_name02
del city_name02
city_name01 = "首都"
print(city_name03)  # ? "北京上海"
