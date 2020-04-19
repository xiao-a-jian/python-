# 练习1：对列表进行降序排列：[54,5,5,6,7,87,89]
list01 = [54, 5, 5, 6, 7, 87, 89, 102, -58]
for r in range(0, len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
