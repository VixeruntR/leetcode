# coding=utf-8
"""
老师想给孩子们分发糖果, 有 N个孩子站成了一条直线, 老师会根据每个孩子的表现预先给他们评分.
需要按照以下要求,帮助老师给这些孩子分发糖果：
    每个孩子至少分配到 1 个糖果.
    相邻的孩子中,评分高的孩子必须获得更多的糖果.
那么这样下来老师至少需要准备多少颗糖果?

示例 1: 输入: [1,0,2]
       输出: 5
       解释: 可以分别给这三个孩子分发 2、1、2 颗糖果.
示例 2: 输入: [1,2,2]
       输出: 4
       解释: 可以分别给这三个孩子分发 1、2、1 颗糖果.
            第三个孩子只得到 1 颗糖果,这已满足上述两个条件.
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy_sum = 0
        l = len(ratings)
        temp_left = [1] * l
        temp_right = [1] * l
        for i in range(l - 1):  # 先从左至右遍历数组 右侧值大则右侧值加一
            if ratings[i] < ratings[i + 1]:
                temp_left[i + 1] = temp_left[i] + 1

        candy_sum += temp_left[-1]
        for i in range(l - 1, 0, -1):  # 再从右至左遍历数组 左侧值大则左侧值加一
            if ratings[i] < ratings[i - 1]:
                temp_right[i - 1] = temp_right[i] + 1
            candy_sum += max(temp_left[i - 1], temp_right[i - 1])  # 取左右两数组对应位置的较大值

        return candy_sum


s = Solution()
r = s.candy([1, 2, 3, 4, 1])
print(r)
