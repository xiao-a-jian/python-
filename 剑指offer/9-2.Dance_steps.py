"""
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路：青蛙跳n级台阶的跳法相当于青蛙跳n-1级台阶后再跳1级，
或者青蛙跳n-2级台阶后再跳2级，
因此 f(x) = f(x-1) + f(x-2) , n>=2，当n<2时的情况易得。
"""


class Solution:
    def jumpFloor(self, number):
        dp = [0, 1, 2]

        for i in range(3, number+1):
            dp.append(dp[i-1]+dp[i-2])

        return dp[number]


s = Solution()
print(s.jumpFloor(10))


"""
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路：青蛙跳n级台阶的跳法相当于青蛙跳青蛙跳n-1级台阶后再跳1级，或者青蛙跳n-2级台阶后再跳2级，
因此 f(x) = f(x-1) + f(x-2) , n>=2，当n<2时的情况易得。
"""


class Solution:
    def jumpFloorII(self, number):
        dp = [0, 1, 2]

        for floor in range(3, number+1):
            dp.append(0)
            for i in range(floor):
                dp[floor] += dp[i]
            dp[floor] += 1

        return dp[number]


s = Solution()
print(s.jumpFloorII(10))

