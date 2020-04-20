"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
思路：
由题目可知，一定会有一个答案，所有可以遍历一下数组，
并在遍历的过程中将当前值及其所在的索引位置作为k、v存入字典中，
并判断目标值target减去当前值是否在字典里，如果存在，即可找到满足题意的索引值。
"""


class Solution(object):
    def towSum(self, nums, target):
        dt = {}
        for index, item in enumerate(nums):
            if target - item in dt:
                return [index, dt[target-item]]
            dt[item] = index


a = Solution()
nums = [11, 15, 6, 3]
b = a.towSum(nums, target=9)
print(b)






