# coding=utf-8
"""
找出所有相加之和为n的k个数的组合. 组合中只允许含有1-9的正整数,并且每种组合中不存在重复的数字.
所有数字都是正整数, 解集不能包含重复的组合.

示例 1: 输入: k = 3, n = 7
       输出: [[1,2,4]]
示例 2: 输入: k = 3, n = 9
       输出: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def backtrack(index, used, remain):
            for i in range(index, 10):
                if i > remain:
                    return
                if i == remain and len(used) == k - 1:
                    res.append(used + [i])
                    return
                if i < remain and len(used) >= k:
                    break
                backtrack(i + 1, used + [i], remain - i)

        res = []
        backtrack(1, [], n)
        return res


s = Solution()
r = s.combinationSum3(3, 9)
print(r)
