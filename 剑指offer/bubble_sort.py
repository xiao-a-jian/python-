"""
冒泡排序（顺序形式），从左向右，两两比较，如果左边元素大于右边，就交换两个元素的位置。
其中，每一轮排序，序列中最大的元素浮动到最右面。也就是说，每一轮排序，至少确保有一个元素在正确的位置。
这样接下来的循环，就不需要考虑已经排好序的元素了，每次内层循环次数都会减一。
其中，如果有一轮循环之后，次序并没有交换，这时我们就可以停止循环，得到我们想要的有序序列了。
"""


def bouble_sort(sequence):
    seq = sequence[:]
    length = len(seq) - 1
    i = j = 0
    flag = 1
    while i < length:
        j = 0
        while j < length - i:
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                flag = 0
            j += 1
        if flag:
            break
        i += 1
    return seq


s = [8, 9, 6, 7, 2, 5, 4, 3, 1]
print(bouble_sort(s))
