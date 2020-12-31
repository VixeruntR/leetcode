# coding=utf-8
"""
给你一个包含n个整数的数组nums, 判断nums中是否存在三个元素 a,b,c, 使得 a + b + c = 0
找出所有满足条件且不重复的三元组, 答案中不可以包含重复的三元组。

示例1: 给定数组 nums = [-1, 0, 1, 2, -1, -4]
      满足要求的三元组集合为: [[-1, 0, 1],
                           [-1, -1, 2]]
示例2: 给定数组 nums = [0, 0, 0, 0, 0, 0]
      满足要求的三元组集合为: [[0, 0, 0]]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        1. 对于数组长度n, 如果数组为null或者数组长度小于3, 返回[].
        2. 对数组进行排序, 数组起点值大于0或者末尾值小于0则返回[].
        3. 遍历排序后对数组进行循环：
          3.1 若nums[i]>0: 因为已经排序好, 所以后面不可能有三个数和等于0, 直接返回结果.
          3.2 对于重复元素: 跳过避免出现重复解.
          3.3 令左指针L=i+1, 右指针R=n−1, 当L<R时执行循环:
                当nums[i]+nums[L]+nums[R] == 0,执行循环判断左界和右界是否和下一位置重复, 去除重复解, 并同时将L和R移到下一位置.
                当nums[i]+nums[L]+nums[R] > 0, 说明nums[R]太大, R左移.
                当nums[i]+nums[L]+nums[R] < 0, 说明nums[L]太小, L右移.
        """
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:  # 列表必须有正有负或者全0
            return []

        res = []
        for i in range(n):
            if nums[i] > 0:  # 每次循环的起点值都不能大于0
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1
                else:
                    L = L + 1
        return res


a = Solution()
r = a.threeSum([-5, 0, 1, 4])
print(r)
