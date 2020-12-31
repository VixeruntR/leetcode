# coding=utf-8
"""
给定四个包含整数的数组列表A, B, C, D,计算有多少个元组(i, j, k, l),使得A[i] + B[j] + C[k] + D[l] = 0.
所有的 A, B, C, D具有相同的长度N,且 0 ≤ N ≤ 500.

示例1: 输入: A = [ 1, 2]
           B = [-2,-1]
           C = [-1, 2]
           D = [ 0, 2]
      输出: 2
      解释: 两个元组如下:
            1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
            2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        import collections
        countAB = collections.Counter(u + v for u in A for v in B)

        res = 0
        for u in C:
            for v in D:
                if -u - v in countAB:
                    res += countAB[-u - v]
        return res


s = Solution()
r = s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])
print(r)
