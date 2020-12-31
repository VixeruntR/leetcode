"""
给定一个整数数组nums和一个目标值target, 请你在该数组中找出和为目标值的那'两个'整数, 并返回他们的数组下标.
你可以假设每种输入只会对应一个答案. 但是数组中‘同一个(指同一个数字用两遍 并非指两个相等的值)’元素不能使用两遍.

示例: 给定 nums = [2, 7, 11, 15], target = 9
     因为 nums[0] + nums[1] = 2 + 7 = 9
     所以返回 [0, 1]
"""


class Solution(object):
    def twoSum_force(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def twoSum(self, nums, target):
        """模拟哈希表: 建立完字典后查找"""
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index

        for current_index, num in enumerate(nums):
            find_index = hashmap.get(target - num)
            if find_index is not None and current_index != find_index:
                return [current_index, find_index]
        return None

    def twoSum_2(self, nums, target):
        """模拟哈希表: 边建立边查找"""
        hashmap = {}
        for current_index, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap.get(target - num), current_index]
            hashmap[num] = current_index
        return None

        # hashmap = {}
        # for current_index, num in enumerate(nums):
        #     if (target - num) in hashmap:
        #         return [hashmap[target - num], current_index]
        #     hashmap[num] = current_index


a = Solution()
s = a.twoSum_2(nums=[2, 2, 3, 4, 5], target=4)
print(s)
