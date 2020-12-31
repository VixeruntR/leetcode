# coding=utf-8
"""
数组的每个索引作为一个阶梯, 第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始).
每当爬上一个阶都要花费对应的体力花费值, 然后可以选择继续爬一个阶梯或者爬两个阶梯.
需要找到达到楼层顶部的最低花费. 在开始时可以选择索引为 0或 1的元素作为初始阶梯.

示例 1: 输入: cost = [10, 15, 20]
       输出: 15
       解释: 最低花费是从cost[1]开始,然后走两步即可到阶梯顶,一共花费15.
示例 2: 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
       输出: 6
       解释: 最低花费方式是从cost[0]开始,逐个经过那些1,跳过cost[3],一共花费6.
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 创建长度为(n+1)的数组dp, 其中dp[i]表示达到下标i的最小花费
        # 由于可以选择下标0或1作为初始阶梯, 因此dp[0]=dp[1]=0
        # 当2 <= i <= n 时, 可以从下标(i−1)使用 cost[i−1]的花费达到下标i,
        # 或者从下标(i−2)使用 cost[i−2]的花费达到下标i. 为了使总花费最小, dp[i]应取上述两项的较小值
        # 因此状态转移方程: dp[i] = min(dp[i−1] + cost[i−1], dp[i−2] + cost[i−2])
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]


s = Solution()
r = s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(r)
