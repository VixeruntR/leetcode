# coding=utf-8
"""
给定一个非负整数 N,找出小于或等于 N的最大的整数,同时这个整数需要满足其各个位数上的数字是单调递增.
当且仅当每个相邻位数上的数字 x和 y满足 x <= y时, 才称这个整数是单调递增的.

示例 1: 输入: N = 10
       输出: 9
示例 2: 输入: N = 1234
       输出: 1234
示例 3: 输入: N = 332
       输出: 299
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        将 N从高位往低位遍历,遍历过程中做两件事:
         1.记录遇到的最大值和最大值所在位置, 分别记为 max_num和max_index
         2.比较相邻数字, 一旦遇到后一位数比当前数小(非递增), 则提前退出遍历
        此时将max_index位置的数减 1,并将max_index位置后的数都置为 9,所得出的数就是想要的结果
        :type N: int
        :rtype: int
        """
        sn = list(str(N))
        length = len(sn)
        if length <= 1:
            return N
        max_index = 0
        max_num = -1
        is_result = True
        for i in range(1, length):
            cur_num = int(sn[i])
            pre_num = int(sn[i - 1])
            if pre_num > max_num:
                max_index = i - 1
                max_num = pre_num
            if pre_num > cur_num:
                is_result = False
                break
        if is_result:
            return N

        sn[max_index] = str(int(sn[max_index]) - 1)
        for i in range(max_index + 1, length):
            sn[i] = '9'

        return int("".join(sn))



s = Solution()
r = s.monotoneIncreasingDigits(3324)
print(r)
