# coding=utf-8
"""
给定一个字符串, 找出其中不含有重复字符的‘最长子串’的长度.

示例 1:  输入: "abcabcbb"
        输出: 3
        解释: 因为无重复字符的最长子串是 "abc", 所以其长度为 3。

示例 2:  输入: "bbbbb"
        输出: 1
        解释: 因为无重复字符的最长子串是 "b", 所以其长度为 1。

示例 3:  输入: "pwwkew"
        输出: 3
        解释: 因为无重复字符的最长子串是 "wke", 所以其长度为3。
             注意答案必须是'子串'的长度, "pwke"是一个子序列,不是子串。
"""


class Solution(object):
    def lengthOfLongestSubstring_force(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        str_len = len(s)
        max_len = 1
        for i in range(str_len - 1):
            for j in range(i + 2, str_len + 1):
                current_str = s[i:j]
                # print(i, j, current_str)
                current_str_len = len(current_str)
                if current_str_len != len(set(current_str)):
                    break
                else:
                    if current_str_len > max_len:
                        max_len = current_str_len
        return max_len

    def lengthOfLongestSubstring(self, s):
        """
        依次递增地枚举子串的起始位置, 那么子串的结束位置也是递增的.
        假设选择字符串中的第k个字符作为起始位置, 并且得到了不包含重复字符的最长子串的结束位置为rk​.
        那么当选择第k+1个字符作为起始位置时, 首先从k+1到rk​的字符显然是不重复的，
        并且由于少了原本的第k个字符, 可以尝试继续增大rk​, 直到右侧出现了重复字符为止。
        """
        occ = set()
        n = len(s)
        right, max_len = 0, 0
        for left in range(n):
            while right < n and s[right] not in occ:
                occ.add(s[right])
                right += 1
            if len(occ) > max_len:
                max_len = len(occ)
                # max_len_str = s[left:right]
            occ.remove(s[left])
        return max_len


a = Solution()
r = a.lengthOfLongestSubstring('pwwkew')
print(r)
