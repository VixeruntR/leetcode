# coding=utf-8
"""
给定n个非负整数表示每个宽度为1的柱子的高度图, 计算按此排列的柱子, 下雨之后能接多少雨水.
        ./docs/接雨水.png
示例 1:  输入: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        输出: 6
        解释: 上面是由数组[0,1,0,2,1,0,1,3,2,1,2,1]表示的高度图,在这种情况下可以接6个单位的雨水(蓝色部分表示雨水)
示例 2:  输入: height = [4,2,0,3,2,5]
        输出: 9
"""


class Solution(object):
    def trap_force(self, height):
        """对于每个下标 能接雨水的数量等于它左边最高的柱子与右边最高的柱子中的较小值减去当前下标的柱子高度
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 1:
            return 0
        water = 0
        for i in range(1, n - 1):
            max_left = max(height[0:i])  # 寻找左边最高的柱子
            max_right = max(height[i + 1:])  # 寻找右边最高的柱子
            target_h = min(max_left, max_right)
            if target_h > height[i]:
                water += target_h - height[i]
        return water

    def trap_dp(self, height):
        """
        数组max_ls[i]表示下标i处左边最高柱子的高度, 数组max_rs[i]表示下标i处右边最高柱子的高度.
        """
        n = len(height)
        if n <= 1:
            return 0
        water = 0
        max_ls = [0] * n
        max_rs = [0] * n
        max_ls[0] = height[0]
        max_rs[n - 1] = height[n - 1]
        for i in range(1, n):
            max_ls[i] = max(height[i], max_ls[i - 1])
        for j in range(n - 2, -1, -1):
            max_rs[j] = max(height[j], max_rs[j + 1])
        for i in range(1, n - 1):
            target_h = min(max_ls[i], max_rs[i])
            if target_h > height[i]:
                water += target_h - height[i]
        return water

    def trap_points(self, height):
        n = len(height)
        if n <= 1:
            return 0
        water = 0
        lp, rp = 0, n - 1
        max_l, max_r = height[0], height[n - 1]
        while lp <= rp:
            max_l = max(height[lp], max_l)
            max_r = max(height[rp], max_r)
            if max_l < max_r:
                water += max_l - height[lp]
                lp += 1
            else:
                water += max_r - height[rp]
                rp -= 1
        return water


a = Solution()
r = a.trap_points([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(r)
