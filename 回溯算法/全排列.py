# coding=utf-8
"""
给定一个没有重复数字的序列, 返回其所有可能的全排列.

示例: 输入: [1,2,3]
     输出: [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
          ]
"""


# https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

class Solution(object):
    def permute_force(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        return list(itertools.permutations(nums))

    def permute_backtrack1(self, nums):
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        res = []
        backtrack(nums, [])
        return res

    def permute_backtrack2(self, nums):
        def backtrack(nums, res, check):
            n = len(nums)
            if len(res) == n:
                results.append(res)
                return
            for i in range(n):
                if check[i] == 1:  # 剪枝条件: 用过的元素不能再使用
                    continue
                check[i] = 1  # 取出该位置的元素 则将check对应坐标置1
                backtrack(nums, res + [nums[i]], check)
                check[i] = 0  # 本次回溯结束 将check对应坐标重新置0

        results = []
        check = [0] * len(nums)  # 记录每次回溯前nums每个位置的元素使用情况:0/1表示未使用/已使用
        backtrack(nums, [], check)
        return results


s = Solution()
r = s.permute_backtrack2([1, 2, 3])
print(r)
