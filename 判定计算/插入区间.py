# coding=utf-8
"""
给出一个无重叠的, 按照区间起始端点排序的区间列表.
在列表中插入一个新的区间, 确保列表中的区间仍然有序且不重叠(如有必要可以合并区间).

示例 1: 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
       输出: [[1,5],[6,9]]

示例 2: 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
       输出: [[1,2],[3,10],[12,16]]
       解释: 新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠.
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        n = len(intervals)
        res = []

        new_l, new_r = newInterval[0], newInterval[1]
        while i < n and new_l > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            new_l = min(new_l, intervals[i][0])
            new_r = max(new_r, intervals[i][1])
            i += 1
        res.append([new_l, new_r])
        while i < n:
            res.append(intervals[i])
            i += 1
        return res


s = Solution()
r = s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
print(r)
