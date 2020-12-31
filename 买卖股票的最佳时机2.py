# coding=utf-8
"""
给定一个数组,它的第 i 个元素是一支给定股票第 i 天的价格.
设计一个算法来计算所能获取的最大利润.可以尽可能地完成更多的交易(多次买卖一支股票).
但不能在买入股票前卖出股票,即必须在再次购买前出售掉之前的股票.

示例 1: 输入: [7,1,5,3,6,4]
       输出: 7
       解释: 在第2天(股票价格=1)的时候买入,在第3天(股票价格=5)的时候卖出,这笔交易所能获得利润为 5-1 = 4
            随后在第4天(股票价格=3)的时候买入,在第5天(股票价格=6)的时候卖出,这笔交易所能获得利润为 6-3 = 3
示例 2: 输入: [1,2,3,4,5]
       输出: 4
       解释: 在第1天(股票价格=1)的时候买入,在第5天(股票价格=5)的时候卖出,这笔交易所能获得利润为 5-1 = 4
            注意不能在第1天和第2天接连购买股票,因为这样属于同时参与了多笔交易.
示例 3: 输入: [7,6,4,3,1]
       输出: 0
       解释: 在这种情况下,没有交易完成,所以最大利润为 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices) - 1):
            p = prices[i + 1] - prices[i]
            if p > 0:
                res += p
        return res

    def maxProfit_dp(self, prices):
        # dp[i][0] 表示第i天卖出的最大利润; dp[i][1] 表示第i天买入的最大利润
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0  # 第一天没有股票可卖 所以利润为0
        dp[0][1] = -prices[0]  # 第一天买入价格为prices[0]的股票
        for i in range(1, n):
            # 可以选择持仓不动或者用前一天买入的最大利润加上当天的股价
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 可以选择持仓不动或者用前一天卖出的最大利润减去当天的股价
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]

    def maxProfit_dp2(self, prices):
        # dp空间优化:在计算第i天买入/卖出收益时,只需要第i-1天的买入/卖出收益即可,更早的都不需要了
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1, n):
            tmp = dp0
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, tmp - prices[i])
        return max(dp0, 0)


s = Solution()
r = s.maxProfit_dp([7, 1, 5, 3, 6, 4])
print(r)
