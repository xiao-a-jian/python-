# 练习2：请排列出3个色子可以组合的所有数字(1,1,1)   (1,1,2) ...
#       第一个色子数字：1--6
#       第二个色子数字：1--6
#       第二个色子数字：1--6
list_result = [(a, b, c)
               for a in range(1, 7) for b in range(1, 7) for c in range(1, 7)]
print(list_result)
