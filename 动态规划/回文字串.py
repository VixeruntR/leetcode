# coding=utf-8
"""
给定一个字符串, 计算这个字符串中有多少个回文子串
具有不同开始位置或结束位置的子串, 即使是由相同的字符组成, 也会被视作不同的子串.

示例 1： 输入："abc"
        输出：3
        解释：三个回文子串: "a", "b", "c"

示例 2： 输入："aaa"
        输出：6
        解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""


class Solution(object):
    def countSubstrings_force(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = len(s)
        if len(s) > 1 and s == s[::-1]:
            num += 1
        for l in range(2, len(s)):  # 从长度为2的子字符串开始遍历
            for i in range(len(s) - l + 1):
                current_str = s[i:i + l]
                if current_str == current_str[::-1]:
                    num += 1
        return num

    def countSubstrings(self, s: str) -> int:
        # dp[i][j]代表子串s[i:j+1]是否是一个回文串
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(0, j + 1):  # 枚举所有可能 因为代表子串 所以 i<=j
                length = j - i + 1  # 子串长度
                if length == 1:  # 只有一个字符是回文串
                    dp[i][j] = True
                    count += 1
                if length == 2 and s[i] == s[j]:  # 两个字符只有相等才是回文串
                    dp[i][j] = True
                    count += 1
                # 超过两个字符 首位相同且除去首尾的子串是回文串 才是回文串
                if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    count += 1
        return count


a = Solution()
r = a.countSubstrings('abcde')
print(r)
