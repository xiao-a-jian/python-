"""
首先要打乱序列顺序 ，以防算法陷入最坏时间复杂度。快速排序使用“分而治之”的方法。
对于一串序列，首先从中选取一个数，凡是小于这个数的值就被放在左边一摞，
凡是大于这个数的值就被放在右边一摞。然后，继续对左右两摞进行快速排序。
直到进行快速排序的序列长度小于 2 （即序列中只有一个值或者空值）。
"""

import random


def quicksort(seq):
    if len(seq) < 2:
        return seq
    else:
        base = seq[0]
        left = [elem for elem in seq[1:] if elem < base]
        right = [elem for elem in seq[1:] if elem > base]
        return quicksort(left) + [base] + quicksort(right)


seq = [8, 9, 6, 7, 2, 5, 4, 3, 1]
random.shuffle(seq)
print(quicksort(seq))
