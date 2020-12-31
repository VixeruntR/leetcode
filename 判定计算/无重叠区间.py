# coding=utf-8
"""
给定一个区间的集合, 区间的终点总是大于它的起点, 找到需要移除区间的最小数量, 使剩余区间互不重叠.

示例 1: 输入: [[1,2], [2,3], [3,4], [1,3]]
       输出: 1
       解释: 移除[1,3]后,剩下的区间没有重叠.
示例 2: 输入: [[1,2], [1,2], [1,2]]
       输出: 2
       解释: 需要移除两个[1,2]来使剩下的区间没有重叠.
示例 3: 输入: [[1,2], [2,3]]
       输出: 0
       解释: 不需要移除任何区间,因为它们已经是无重叠的了.
"""


class Solution(object):
    def eraseOverlapIntervals_end(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        current_end = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            if interval[0] < current_end:
                res += 1
            else:
                current_end = interval[1]
        return res

    def eraseOverlapIntervals_start(self, intervals):
        if not intervals:
            return 0
        intervals.sort()
        res = 0
        current_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= current_end:
                current_end = interval[1]
            else:
                # 如有重叠则将区间终点更新为较小值, 因为终点值大和后续区间冲突可能性也更大
                current_end = min(current_end, interval[1])
                res += 1
        return res


s = Solution()
r = s.eraseOverlapIntervals_start([[1, 100], [11, 22], [1, 11], [2, 12]])
print(r)
