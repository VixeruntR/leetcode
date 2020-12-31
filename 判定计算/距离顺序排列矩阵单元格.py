# coding=utf-8
"""
给出R行C列的矩阵, 其中的单元格的整数坐标为(r, c),满足 0 <= r < R 且 0 <= c < C.
另外该矩阵中给出了一个坐标为(r0, c0)的单元格.
返回矩阵中的所有单元格的坐标, 并按到(r0, c0)的距离从最小到最大的顺序排,
其中两单元格(r1, c1)和(r2, c2)之间的距离是曼哈顿距离: |r1 - r2| + |c1 - c2|

示例 1: 输入: R = 1, C = 2, r0 = 0, c0 = 0
       输出: [[0,0],[0,1]]
       解释: 从 (r0, c0) 到其他单元格的距离为[0,1]
示例 2: 输入: R = 2, C = 2, r0 = 0, c0 = 1
       输出: [[0,1],[0,0],[1,1],[1,0]]
       解释: 从(r0, c0) 到其他单元格的距离为[0,1,1,2]
            [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案.
示例 3: 输入: R = 2, C = 3, r0 = 1, c0 = 2
       输出: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
       解释: 从(r0, c0)到其他单元格的距离为[0,1,1,2,2,3]
"""


class Solution(object):
    def allCellsDistOrder_force(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        m = [[i, j] for i in range(R) for j in range(C)]
        m.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return m

    def allCellsDistOrder_dict(self, R, C, r0, c0):
        m_dict = {}
        for i in range(R):
            for j in range(C):
                dist = abs(i - r0) + abs(j - c0)
                if dist not in m_dict:
                    m_dict[dist] = []
                    m_dict[dist].append([i, j])
                else:
                    m_dict[dist].append([i, j])

        res = []
        for i in sorted(m_dict.keys()):
            res.extend(m_dict[i])
        return res

    def allCellsDistOrder_list(self, R, C, r0, c0):
        m_list = [[] for i in range(R + C - 1)]  # 曼哈顿距离最大不超过矩阵的长宽之和-1
        for i in range(R):
            for j in range(C):
                dist = abs(i - r0) + abs(j - c0)
                m_list[dist].append([i, j])

        res = []
        for m in m_list:
            res.extend(m)
        return res


s = Solution()
r = s.allCellsDistOrder_list(R=2, C=3, r0=1, c0=2)
print(r)
