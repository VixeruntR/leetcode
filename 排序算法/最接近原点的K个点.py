# coding=utf-8
"""
有一个由平面上的点组成的列表points.需要从中找出K个距离原点(0, 0)最近的点(平面上两点之间的距离是欧几里德距离).

示例 1: 输入: points = [[1,3],[-2,2]], K = 1
       输出: [[-2,2]]
       解释: (1, 3)和原点之间的距离为 sqrt(10),
            (-2,2)和原点之间的距离为 sqrt(8),
            由于 sqrt(8) < sqrt(10), (-2, 2)离原点更近。

示例 2: 输入: points = [[3,3],[5,-1],[-2,4]], K = 2
       输出: [[3,3],[-2,4]]
"""


class Solution(object):
    def kClosest_force(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]

    def kClosest_queue(self, points, K):
        import heapq
        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(q)
        n = len(points)
        for i in range(K, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))

        res = [points[identity] for (_, identity) in q]
        return res

    def kClosest_quickSort(self, points, K):
        import random

        def random_select(left, right, K):
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[right], points[pivot_id] = points[pivot_id], points[right]
            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]

            # [left, i-1] 都小于等于 pivot, [i+1, right] 都大于 pivot
            if K < i - left + 1:
                random_select(left, i - 1, K)
            elif K > i - left + 1:
                random_select(i + 1, right, K - (i - left + 1))

        n = len(points)
        random_select(0, n - 1, K)
        return points[:K]


s = Solution()
r = s.kClosest_quickSort([[1, 3], [-2, 2]], 1)
print(r)
