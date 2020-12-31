# coding=utf-8
"""
给定一个数组nums和一个值val, 原地移除所有数值等于val的元素, 并返回移除后数组的新长度.
不要使用额外的数组空间, 必须仅使用O(1)额外空间并原地修改输入数组.
元素的顺序可以改变, 不需要考虑数组中超出新长度后面的元素。

示例 1:  给定 nums = [3,2,2,3], val = 3,
        函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

示例 2:  给定 nums = [0,1,2,2,3,0,4,2], val = 2,
        函数应该返回新的长度5, 并且nums中的前五个元素为 0, 1, 3, 0, 4
"""


class Solution(object):
    def removeElement_1(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == val:
                nums[i] = nums[l - 1]
                l -= 1
            else:
                i += 1
        return l


a = Solution()
r = a.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(r)
