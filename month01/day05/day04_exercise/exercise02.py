"""
    随机加法考试题
    随机产生２个数字(1-10之间)
    在终端中获取这两个数字的和(请输入2+8=?)
    总共5道题,答对加10分,答错减5分
    最后打印总分
"""

# scoring=0
# count=0
# while count<5:
#     count+=1
#     import random
#     number1 = (random.randint(1, 10))
#     number2 = (random.randint(1, 10))
#     sum_a = number1 + number2
#     print('%d加上%d的答案是什么' % (number1, number2))
#     answer=(input('输入答案'))
#     if answer=='':
#         print('到底输不输')
#         break
#     answer=int(answer)
#     if answer==sum_a:
#         scoring+=10
#         print('加十分')
#     else:
#         scoring-=5
#         print('扣五分')
#     print('你现在有%d分'%(scoring))
# else:
#     print('答题结束，你获得了%d分'%(scoring))
import random

scoring = 0
# 因为在循环体中不用使用for循环的变量,所以命名为__
for __ in range(5):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    sum_value = number1 + number2
    print('%d加上%d的答案是什么' % (number1, number2))
    input_answer = input('输入答案:')
    if input_answer == '':
        print('到底输不输')
        break
    input_answer = int(input_answer)
    scoring += 10 if input_answer == sum_value else -5
    print('你现在有%d分' % scoring)
else:
    print('答题结束，你获得了%d分' % scoring)
