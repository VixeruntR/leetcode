# coding=utf-8
"""
给定一个整数数组A, 如果它是有效的山脉数组就返回true, 否则返回false.
如果A满足下述条件, 那么它是一个山脉数组:
    A.length >= 3
    在 0 < i < A.length - 1 条件下，存在 i 使得：
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[A.length - 1]

示例 1:  输入：[2,1]
        输出: false
示例 2:  输入：[3,5,5]
        输出: false
示例 3:  输入：[0,3,2,1]
        输出: true
"""


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n < 3:
            return False
        index = 0
        for i in range(n - 1):
            if A[i] < A[i + 1]:
                index = i + 1
            else:
                break
        if index == 0 or index == n - 1:
            return False
        for j in range(index, n - 1):
            if A[j] <= A[j + 1]:
                return False
        return True


a = Solution()
r = a.validMountainArray(
    [14, 82, 89, 84, 79, 70, 70, 68, 67, 66, 63, 60, 58, 54, 44, 43, 32, 28, 26, 25, 22, 15, 13, 12, 10, 8, 7, 5, 4, 3])
print(r)
