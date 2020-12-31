# coding=utf-8
"""
将一个给定字符串根据给定的行数, 以从上往下、从左到右进行 Z 字形排列.
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时排列如下：
                                        L   C   I   R
                                        E T O E S I I G
                                        E   D   H   N
之后输出需要从左往右逐行读取, 产生出一个新的字符串 "LCIRETOESIIGEDHN"。


示例 1:  输入: s = "LEETCODEISHIRING", numRows = 3
        输出: "LCIRETOESIIGEDHN"

示例 2:  输入: s = "LEETCODEISHIRING", numRows = 4
        输出: "LDREOEIIECIHNTSG"
        解释:    L     D     R
                E   O E   I I
                E C   I H   N
                T     S     G
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        # 每组'|/型'字符串的长度(从第0行开头折返到第1行结尾)
        group_str_len = 2 * numRows - 2
        res = ['' for _ in range(numRows)]
        for i in range(len(s)):
            c = s[i]
            insert_i = i % group_str_len
            if insert_i < numRows:  # '|/型的 | 部分'
                res[insert_i] += c
            else:  # '|/型的 / 部分'
                res[group_str_len - insert_i] += c
        return ''.join(res)


a = Solution()
r = a.convert(s="LEETCODEISHIRING", numRows=4)
print(r)
