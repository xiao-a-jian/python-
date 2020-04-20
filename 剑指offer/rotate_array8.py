"""
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
 例如数组 {3,4,5,1,2} 为 {1,2,3,4,5} 的一个旋转，该数组的最小值为 1。
  NOTE：给出的所有元素都大于 0，若数组大小为 0，请返回 0。
"""


class Solution(object):
    def minNumInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        else:
            left = 0
            right = len(rotateArray) - 1
            minVal = rotateArray[0]

            if rotateArray[left] < rotateArray[right]:
                return rotateArray[0]
            else:
                while right - left > 1:
                    mid = (left + right) // 2
                    if rotateArray[mid] < rotateArray[left]:
                        right = mid
                    elif rotateArray[mid] > rotateArray[right]:
                        left = mid
                    else:
                        for item in rotateArray[left:right+1]:
                            if item < minVal:
                                minVal = item
                            return minVal
                return rotateArray[right]


s = Solution()
ls = [5, 6, 7, 2, 3, 4]
print(s.minNumInRotateArray(ls))






















