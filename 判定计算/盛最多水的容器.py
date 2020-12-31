# coding=utf-8
"""
给定n个非负整数 a1，a2，...，an, 每个数代表坐标中的一个点(i, ai)。
在坐标内画n条垂直线, 垂直线i的两个端点分别为(i, ai)和(i, 0)。
找出其中的两条线, 使得它们与x轴共同构成的容器可以容纳最多的水。
            ./docs/盛最多水的容器.png
说明：不能倾斜容器, 且n的值至少为 2。

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
解释: (1, 8)和(8, 7)两个点 --> 7*(8-1)=49
"""


class Solution(object):
    def maxArea_force(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        max_area = 0
        for i in range(l - 1):
            for j in range(i + 1, l):
                box_height = min(height[i], height[j])
                s = box_height * (j - i)
                if s > max_area:
                    max_area = s
        return max_area

    def maxArea_double_pointer(self, height):
        max_area = 0
        left_p, right_p = 0, len(height) - 1
        while left_p < right_p:
            if height[left_p] <= height[right_p]:
                s = height[left_p] * (right_p - left_p)
                max_area = max(s, max_area)
                left_p += 1
            else:
                s = height[right_p] * (right_p - left_p)
                max_area = max(s, max_area)
                right_p -= 1
        return max_area


a = Solution()
r = a.maxArea_double_pointer([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(r)
