# coding=utf-8
"""
给定一个由正整数组成且不存在重复数字的数组, 找出和为给定目标正整数的组合的个数.

示例: nums = [1, 2, 3]
     target = 4
     所有可能的组合为(顺序不同的序列被视作不同的组合):
     (1, 1, 1, 1)
     (1, 1, 2)
     (1, 2, 1)
     (1, 3)
     (2, 1, 1)
     (2, 2)
     (3, 1)
     因此输出为7.
"""


# https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]


s = Solution()
r = s.combinationSum4([1, 2, 3], 4)
print(r)
