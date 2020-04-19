"""
    列表内存分配
    练习:exercise06
"""
list01 = [10, 20, 30]
list01.insert(1, "a")
list01.remove("a")
list02 = list01[:]
list01[1:3] = ["a", "b"]
