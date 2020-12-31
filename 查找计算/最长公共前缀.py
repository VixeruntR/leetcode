# coding=utf-8
"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀, 返回空字符串 ""。

示例 1:  输入: ["flower","flow","flight"]
        输出: "fl"
示例 2:  输入: ["dog","racecar","car"]
        输出: ""
        解释: 输入不存在公共前缀.
说明:所有输入只包含小写字母a-z.
"""


class Solution(object):
    def longestCommonPrefix_force(self, strs):
        """横向扫描"""

        def find_common_str(str1, str2):
            cut_index = 0
            while cut_index < min(len(str1), len(str2)) and str1[cut_index] == str2[cut_index]:
                cut_index += 1
            return str1[:cut_index]

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        common_str = strs[0]
        for i in range(1, len(strs)):
            common_str = find_common_str(common_str, strs[i])
            if not common_str:
                return ""
        return common_str

    def longestCommonPrefix2(self, strs):
        """纵向扫描"""

        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""
        minLength = min(len(s) for s in strs)
        cut_index = 0
        for son_l in range(1, minLength + 1):
            if isCommonPrefix(son_l):
                cut_index = son_l
            else:
                return strs[0][:son_l - 1]
        return strs[0][:cut_index]

    def longestCommonPrefix(self, strs):
        """二分查找
        显然最长公共前缀的长度不会超过字符串数组中的最短字符串的长度。
        用minLength表示字符串数组中的最短字符串的长度,
        则可以在 [0, minLength]的范围内通过二分查找得到最长公共前缀的长度。
        每次取查找范围的中间值 mid, 判断每个字符串的长度为mid的前缀是否相同，
        如果相同则最长公共前缀的长度一定大于或等于 mid, 如果不相同则最长公共前缀的长度一定小于mid,
        通过上述方式将查找范围缩小一半, 直到得到最长公共前缀的长度。
        """

        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""
        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1
        return strs[0][:low]

    def longestCommonPrefix_dict(self, strs):
        """只需对列表排序后找出列表中字典序最小和最大的字符串, 则最长公共前缀即为这两个字符串的公共前缀.
        string比较采用的是 ”字典序“, 即比较当前字符大小.
        若当前字符小则此字符串较小,若相等则继续往后比较,直到某一字符不相等或某一字符串比较结束,前面的字符都相等,则长度小的字符串较小.
        e.g: [a, bc, aac]这三个字符串, 第一个字符分别是a,b,a, 则第二个字符串bc最大;
             再次比较第二个字符, 此时第一个字符串已经空了, 由于a的长度小于aac的长度, 所以a小于aac.
             所以最小字符串为a, 最大字符串为bc, 则其公共前缀为"".
        """
        if not strs:
            return ""
        strs.sort()
        str0, str1 = strs[0], strs[-1]
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

    def longestCommonPrefix_zip(self, strs):
        ans = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


a = Solution()
r = a.longestCommonPrefix_zip(["flower", "flow", "flight"])
print(r)
