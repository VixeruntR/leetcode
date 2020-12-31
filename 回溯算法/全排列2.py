# coding=utf-8
"""
给定一个可包含重复数字的序列nums, 返回所有不重复的全排列.

示例 1: 输入: nums = [1,1,2]
       输出: [[1,1,2],
             [1,2,1],
             [2,1,1]]
示例 2: 输入:nums = [1,2,3]
       输出：[[1,2,3],[1,3,2],
             [2,1,3],[2,3,1],
             [3,1,2],[3,2,1]]
"""


# https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(nums, res, check):
            n = len(nums)
            if len(res) == n:
                results.append(res)
                return
            for i in range(n):
                if check[i] == 1:  # 剪枝条件1: 用过的元素不能再使用
                    continue
                # 剪枝条件2: 当前元素和前一个元素值相同(此处隐含这个元素的坐标大于0),并且前一个元素未被使用
                '''
                ./docs/全排列2.png
                1. 回溯前先将数组升序排列.
                2. 首先取出第一个元素,这时候无任何重复,除了用过的元素不再使用外,不做剪枝.
                3. 直到遇到第一个重复元素,才需要考虑剪枝,但是考虑剪枝的时候还要考虑跟它重复的元素有没有被使用过.
                   如果该重复元素的前一个位置的重复元素没有使用过,那么在当前重复元素下一层的可选项中一定会存在,也就是图中绿色部分.
                    3.1 例如[1,2,2`]当index访问到元素2`时, 如果第二个元素2已经被使用过, 
                        说明是第一次出现形如[X,2,2`]或者[2,2`,X]的答案.
                    3.2 例如[1,2,2`]当index访问到元素2`时, 如果第二个元素2没有被使用过,
                        说明如果此时不剪枝的话,index为1的元素2会同样经过回溯得到重复答案.
                '''
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                backtrack(nums, res + [nums[i]], check)
                check[i] = 0

        nums.sort()
        results = []
        check = [0] * len(nums)  # 记录每次回溯前nums每个位置的元素使用情况:0/1表示未使用/已使用
        backtrack(nums, [], check)
        return results


s = Solution()
r = s.permuteUnique([1, 2, 2])
print(r)
