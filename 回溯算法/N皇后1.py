# coding=utf-8
"""
n皇后问题研究的是如何将n个皇后放置在n×n的棋盘上,并且使皇后彼此之间不能相互攻击.
皇后彼此不能相互攻击的条件: 任何两个皇后都不能处于同一条横行或纵行或斜线上.
./docs/N皇后(8皇后).png (图为8皇后问题的一种解法)

给定一个整数n, 返回所有不同的n皇后问题的解决方案.
每一种解法包含一个明确的n皇后问题的棋子放置方案,该方案中'Q'和'.'分别代表了皇后和空位.

示例: 输入: 4
     输出: [
            [".Q..",
            "...Q",
            "Q...",
            "..Q."],  // 解法1
            ["..Q.",
            "Q...",
            "...Q",
            ".Q.."]   // 解法2
         ]
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 4:
            return []


a = Solution()
r = a.solveNQueens(4)
print(r)
