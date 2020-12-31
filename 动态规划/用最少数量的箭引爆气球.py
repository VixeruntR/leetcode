# coding=utf-8
"""
在二维空间中有许多球形的气球,对于每个气球,提供的输入是水平方向上气球直径的开始和结束坐标,开始坐标总是小于结束坐标.
由于它是水平的,所以纵坐标并不重要,因此只要知道开始和结束的横坐标就足够了.
一支弓箭可以沿着x轴任意点完全垂直地射出.在坐标x处射出一支箭,若有一个气球的直径的开始和结束坐标为xstart, xend,且满足 xstart ≤ x ≤ xend,
则该气球会被引爆,可以射出的弓箭的数量没有限制.弓箭一旦被射出之后,可以无限地前进.想找到使得所有气球全部被引爆,所需的弓箭的最小数量.
给你一个数组points, 其中points[i] = [xstart, xend],返回引爆所有气球所必须射出的最小弓箭数.
 
示例 1: 输入: points = [[10,16],[2,8],[1,6],[7,12]]
       输出: 2
       解释: 对于该样例, x=6可以射爆[2,8],[1,6]两个气球, 以及x=11射爆另外两个气球
示例 2: 输入: points = [[1,2],[3,4],[5,6],[7,8]]
       输出: 4
示例 3: 输入: points = [[1,2],[2,3],[3,4],[4,5]]
       输出: 2
示例 4: 输入: points = [[1,2]]
       输出: 1
示例 5: 输入: points = [[2,3],[2,3]]
       输出: 1
"""


class Solution(object):
    """
    开始时需要先对points升序排序, 可以根据start排序, 也可以根据end排序, 这里用end排序更好.
    start排序: 如果两个区间完全无交集,需多用一根箭,如果两个区间有交集就无需多用一根箭;
              但三个及以上区间有交集时就需要注意这些区间的最小end,如果下一个区间的start大于这个最小end,
              那就算该区间与这些区间有交集也需多加一根箭.
                        Λ
                [-------|-]
                   [----|------]        //前两个气球一箭就够
                     [--|--------]      //前三个气球一箭也够
                        |  [-------]    //第四个气球的start大于第一个气球的end了,需要多加一根箭

    end排序: 排序后列表里第一个气球的end是最小的end,此时只有一种情况需要多加箭,即next_start > current_end.
                       Λ
                 [-----|]
               [-------|---]
                    [--|---]
                       |  [-----]       // 只有此时需要再加一根箭
    """

    def findMinArrowShots_start(self, points):
        if not points:
            return 0

        points = sorted(points, key=lambda x: x[0])
        res = 1
        start, end = points[0][0], points[0][1]
        for point in points[1:]:
            if point[0] > end:
                end = point[1]
                res += 1
            else:
                current_end = point[1]
                if current_end < end:
                    end = current_end
        return res

    def findMinArrowShots_end(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        res = 1
        points = sorted(points, key=lambda x: x[1])
        current_end = points[0][1]
        for point in points[1:]:
            if point[0] > current_end:
                current_end = point[1]
                res += 1
        return res

    def findMinArrowShots_dp(self, points):
        if not points:
            return 0
        points.sort()
        dp = [1] * len(points)
        common = points[0]  # 每个阶段区间重叠的范围,初始设为第一个区间
        for i in range(1, len(dp)):
            if common[1] >= points[i][0]:
                dp[i] = dp[i - 1]
                common[0], common[1] = max(common[0], points[i][0]), min(common[1], points[i][1])
            else:
                dp[i] = dp[i - 1] + 1
                common = points[i]
        return dp[-1]


s = Solution()
r = s.findMinArrowShots_dp([[10, 16], [2, 8], [4, 6], [7, 12]])
print(r)
