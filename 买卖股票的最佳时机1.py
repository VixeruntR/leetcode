# coding=utf-8
"""
给定一个数组,它的第 i个元素是一支给定股票第 i天的价格.
如果最多只允许完成一笔交易(即仅买入和卖出一支股票一次),设计一个算法来计算你所能获取的最大利润,不能在买入股票前卖出股票.

示例 1: 输入: [7,1,5,3,6,4]
       输出: 5
       解释: 在第2天(股票价格=1)的时候买入,在第5天(股票价格 = 6)的时候卖出,最大利润为 6-1 = 5.
            注意利润不能是 7-1 = 6,因为卖出价格需要大于买入价格,同时不能在买入前卖出股票.
示例 2: 输入: [7,6,4,3,1]
       输出: 0
       解释: 在这种情况下没有交易完成,所以最大利润为0.
"""


class Solution(object):
    def maxProfit_force(self, prices):
        res = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])
        return res

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        res = 0
        for price in prices:
            res = max(res, price - min_price)
            min_price = min(min_price, price)
        return res

    def maxProfit_dp(self, prices):
        # 定义dp[i]表示前i天的最大利润
        # dp[i] = max(dp[i−1], prices[i] − min_price)
        n = len(prices)
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)

        return dp[-1]


s = Solution()
r = s.maxProfit_dp([2, 1, 2, 0, 1])
print(r)
