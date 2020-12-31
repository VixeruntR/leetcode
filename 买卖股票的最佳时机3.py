# coding=utf-8
"""
给定一个整数数组 prices,它的第 i 个元素 prices[i] 是一支给定的股票在第 i天的价格.
设计一个算法来计算所能获取的最大利润.你最多可以完成 k 笔交易.
注意不能同时参与多笔交易(必须在再次购买前出售掉之前的股票).

示例 1: 输入: k = 2, prices = [2,4,1]
       输出: 2
       解释: 在第1天(股票价格=2)的时候买入,在第2天(股票价格=4)的时候卖出.
示例 2: 输入: k = 2, prices = [3,2,6,5,0,3]
       输出: 7
       解释: 在第2天(股票价格=2)的时候买入,在第3天(股票价格=6)的时候卖出,这笔交易所能获得利润为 6-2 = 4
            随后在第5天(股票价格=0)的时候买入,在第6天(股票价格=3)的时候卖出,这笔交易所能获得利润为 3-0 = 3
"""



class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # for i in range(len(prices)):
        #     if

s = Solution()
r = s.maxProfit(2, [3, 2, 6, 5, 0, 3])
print(r)
