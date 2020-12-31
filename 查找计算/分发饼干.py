# coding=utf-8
"""
有一位家长想要给孩子们一些小饼干, 但是每个孩子最多只能给一块饼干.
对每个孩子 i,都有一个胃口值 g[i],这是能让孩子满足胃口的饼干的最小尺寸;
对每块饼干 j,都有一个尺寸值 s[j].如果 s[j] >= g[i],则将这个饼干 j分配给孩子 i.
目标是尽可能满足越多数量的孩子,并输出这个最大数值.

示例 1: 输入: g = [1,2,3], s = [1,1]
       输出: 1
       解释: 有三个孩子和两块小饼干,3个孩子的胃口值分别是:1,2,3.
            虽然有两块小饼干,由于他们的尺寸都是1,所以只能让胃口值是1的孩子满足.
示例 2: 输入: g = [1,2], s = [1,2,3]
       输出: 2
"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1

        return count


s = Solution()
r = s.findContentChildren(g=[1, 2], s=[1, 2, 3])
print(r)
