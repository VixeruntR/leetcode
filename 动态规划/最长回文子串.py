# coding=utf-8
"""
给定一个字符串s, 找到s中最长的回文子串.可以假设s的最大长度为 1000.

示例 1： 输入: "babad"
        输出: "bab"
        注意: "aba" 也是一个有效答案。

示例 2： 输入: "cbbd"
        输出: "bb"
"""


class Solution(object):
    def longestPalindrome_dp(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_str = ''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(0, j + 1):
                length = j - i + 1
                if length == 1:
                    dp[i][j] = True
                    if length > len(max_str):
                        max_str = s[i: j + 1]
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                    if length > len(max_str):
                        max_str = s[i: j + 1]
                if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    if length > len(max_str):
                        max_str = s[i: j + 1]
        return max_str

    def longestPalindrome_center(self, s):
        """
        遍历子串长度为1或2时 枚举每一种情况 从对应的子串开始不断地向两边扩展
        如果两边的字母相同 就继续扩展 例如从P(i+1,j−1)扩展到P(i,j)如果两边的字母不同 就停止扩展
        """

        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = expandAroundCenter(s, i, i)
            left2, right2 = expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


a = Solution()
r = a.longestPalindrome_dp('babad')
print(r)
