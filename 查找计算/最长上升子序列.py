# coding=utf-8
"""
给定一个无序的整数数组,找到其中最长上升子序列的长度.

示例: 输入: [10,9,2,5,3,7,101,18]
     输出: 4
     解释: 最长的上升子序列是 [2,3,7,101],它的长度是4.
"""


class Solution(object):
    def lengthOfLIS_dp(self, nums):
        """
        1.定义dp[i]表示以第i个数字结尾的最长上升子序列的长度,注意 nums[i]必须被选取,最终答案为 max(dp)
        2.定义dp[i]表示前i个数字中最长上升子序列的长度,注意 nums[i]不一定被选取,最终答案为 dp[-1]
        以上有两种定义方式,这里选第一种:
        在计算dp[i]之前,已经计算出 dp[0, 1, ……, i−1]的值,即考虑往dp[0, 1, ……, i−1]中最长的上升子序列后面再加一个 nums[i].
        由于dp[j]代表 nums[0, 1, ……, j]中以 nums[j]结尾的最长上升子序列, 所以如果能从 dp[j]状态转移到 dp[i],
        那么 nums[i]必然要大于 nums[j]. 则状态转移方程为:
                dp[i] = max(dp[j]) + 1 (其中0 ≤ j < i, nums[j] < nums[i])

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * len(nums)
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

    def lengthOfLIS(self, nums):
        """
        一个简单的贪心,如果要使上升子序列尽可能长,则需要让序列上升得尽可能慢,因此要在每次上升子序列最后加上的数尽可能小.
        基于上面的贪心思路,维护一个数组d[i], 表示长度为i+1的最长上升子序列的末尾元素的最小值, 起始时len=1, d[0]=nums[0].
        """
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)


s = Solution()
r = s.lengthOfLIS([10, 9, 2, 5, 1, 7, 101, 18])
print(r)
