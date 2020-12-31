# coding=utf-8
"""
给出一个区间的集合,合并所有重叠的区间.

示例 1: 输入: intervals = [[1,3], [2,6], [8,10], [15,18]]
       输出: [[1,6], [8,10], [15,18]]
       解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2: 输入: intervals = [[1,4], [4,5]]
       输出: [[1,5]]
       解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间.
"""


class Solution(object):
    def merge(self, intervals):
        """
        将列表中的区间按照左端点升序排序,然后将第一个区间加入结果数组中,并按顺序依次考虑之后的每个区间:
        ->如果当前区间的左端点在结果数组中最后一个区间的右端点之后, 那么它们不重合, 直接将这个区间加入结果数组的末尾;
        ->否则它们重合, 用当前区间的右端点更新结果数组中最后一个区间的右端点, 将其置为二者的较大值.
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


s = Solution()
r = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print(r)
