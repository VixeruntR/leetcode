# coding=utf-8
"""
给定一个未排序的整数数组, 找出其中没有出现的最小的正整数.

示例 1: 输入: [1,2,0]
       输出: 3
示例 2: 输入: [3,4,-1,1]
       输出: 2
示例 3: 输入: [7,8,9,11,12]
       输出: 1
"""


class Solution(object):
    def firstMissingPositive_force(self, nums):
        """
        对于一个长度为N的数组,其中没有出现的最小正整数只能在[1,N+1]中.
        因为如果[1,N]都出现了,那么答案就是N+1,否则答案是[1,N]中没有出现的最小正整数.
        :type nums: List[int]
        :rtype: int
        """
        # tar = [num for num in nums if num > 0]
        # n = len(tar)
        # for i in range(1, n + 1):
        #     if i not in tar:
        #         return i
        # return n + 1

        return min(set(range(1, len(nums) + 2)) - set(nums))

    def firstMissingPositive(self, nums):
        n = len(nums)
        for num in nums:
            while 0 < num <= n and nums[num - 1] != num:
                nums[num - 1], num = num, nums[num - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


s = Solution()
r = s.firstMissingPositive([1, 2, -3, 6, -5, 4, 10])

print(r)
