# coding=utf-8
"""
给定一个数组nums,编写一个函数将所有0移动到数组的末尾, 同时保持非零元素的相对顺序(在原数组上操作).

示例: 输入: [0,1,0,3,12]
     输出: [1,3,12,0,0]
"""
import pysnooper


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_num = 0
        lp, rp = 0, len(nums) - 1
        while lp < rp - zero_num:
            if nums[lp] == 0:
                nums.append(0)
                del nums[lp]
                zero_num += 1
            else:
                lp += 1
        print(nums)

    def moveZeroes_exchange1(self, nums):
        # 不断地互换前排0元素与后排非零元素
        # i指向第一个0元素, j指向i后面第一个非0元素
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                continue
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

    @pysnooper.snoop()
    def moveZeroes_exchange2(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        print(nums)


s = Solution()
s.moveZeroes_exchange2([0, 1, 0, 3, 12])
