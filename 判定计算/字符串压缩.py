# coding=utf-8
"""
字符串压缩, 利用字符重复出现的次数, 实现基本的字符串压缩功能.
比如字符串aabcccccaaa会变为a2b1c5a3. 若“压缩”后的字符串没有变短则返回原先的字符串.
假设字符串中只包含大小写英文字母(a至z)

示例1:   输入："aabcccccaaa"
        输出："a2b1c5a3"

示例2:   输入："abbccd"
        输出："abbccd"
        解释："abbccd"压缩后为"a1b2c2d1", 比原字符串长度更长。
"""


class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # if not S:
        #     return ""
        # ch = S[0]
        # res = ''
        # c_num = 0
        # for c in S:
        #     if c == ch:
        #         c_num += 1
        #     else:
        #         res += ch + str(c_num)
        #         ch = c
        #         c_num = 1
        # res += ch + str(c_num)
        # return res if len(res) < len(S) else S

        import itertools
        return min(S, "".join(k + str(len(list(v))) for k, v in itertools.groupby(S)), key=len)


a = Solution()
r = a.compressString('aabcccccaaa')
print(r)
