# 练习1：累加0 1 2 3 4 5 6 7 8
# 练习2：累加3 4 5 6 7 8 9 10
# 练习3：累加2 4 6 8 10 12
# 练习4：累加8 7 6 5 4 3
# 练习5：累加-1 -2 -3 -4 -5 -6
sum = 0
for item in range(9):
    sum += item
print(sum)

sum = 0
for item in range(3, 11):
    sum += item
print(sum)

sum = 0
for item in range(2, 13, 2):
    sum += item
print(sum)

sum = 0
for item in range(8, 2, -1):
    sum += item
print(sum)

sum = 0
for item in range(-1, -7, -1):
    sum += item
print(sum)
