# coding=utf-8
"""
给定一个包括n个整数的数组nums和一个目标值target.
找出nums中的三个整数, 使得它们的和与target最接近, 返回这三个数的和.假定每组输入只存在唯一答案.

示例: 输入：nums = [-1,2,1,-4], target = 1
     输出：2
     解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if not nums or n < 3:
            return None
        nums.sort()
        distance = 10 ** 4
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l_p = i + 1
            r_p = n - 1
            while l_p < r_p:
                current_sum = nums[i] + nums[l_p] + nums[r_p]
                if current_sum == target:
                    return current_sum
                distance = current_sum if (abs(current_sum - target) < abs(distance - target)) else distance
                if current_sum > target:
                    while l_p < r_p and nums[r_p] == nums[r_p - 1]:
                        r_p = r_p - 1
                    r_p = r_p - 1
                else:
                    while l_p < r_p and nums[l_p] == nums[l_p + 1]:
                        l_p = l_p + 1
                    l_p = l_p + 1
        return distance


a = Solution()
r = a.threeSumClosest([1, 1, 1, 0], -100)
print(r)
