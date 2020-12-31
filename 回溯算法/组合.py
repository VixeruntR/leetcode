# coding=utf-8
"""
给定两个整数n和k, 返回 1 ... n 中所有可能的k个数的组合.

示例: 输入: n = 4, k = 2
     输出:  [[2,4],
            [3,4],
            [2,3],
            [1,2],
            [1,3],
            [1,4]]
"""


class Solution(object):
    def combine_backtrack1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def backtrack(nums, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for index, num in enumerate(nums):
                if index <= N - k + 2:
                    backtrack(nums[index + 1:], tmp + [num])

        nums = list(range(1, n + 1))
        res = []
        N = len(nums)
        backtrack(nums, [])
        return res

    def combine_backtrack2(self, n, k):
        def backtrace(tmp, index):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(index, n + 1):
                backtrace(tmp + [i], i + 1)

        res = []
        for i in range(1, n + 2 - k):
            backtrace([i], i + 1)
        return res

    def combine_backtrack3(self, n, k):
        def backtrack(tmp, length):
            if length == k:
                res.append(tmp)
                return
            '''
            搜索起点和当前还需要选几个数有关, 而当前还需要选几个数与已经选了几个数有关, 即与tmp的长度相关. 
            可以归纳出: 搜索起点的上界 + 接下来要选择的元素个数 - 1 = n, 其中接下来要选择的元素个数 = k - len(tmp)
            整理得到: 搜索起点的上界 = n - (k - depth) + 1 
            '''
            for i in range(tmp[-1] + 1, n + 2 + length - k):
                backtrack(tmp + [i], length + 1)

        res = []
        for i in range(1, n + 2 - k):
            backtrack([i], 1)
        return res

    def combine(self, n, k):
        import itertools
        return list(itertools.combinations(range(1, n + 1), k))


s = Solution()
r = s.combine_backtrack3(5, 3)
print(r)
