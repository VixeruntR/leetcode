# coding=utf-8
"""
有一堆石头,每块石头的重量都是正整数.每一回合从中选出两块最重的石头,然后将它们一起粉碎.
假设石头的重量分别为 x和 y,且 x <= y.那么粉碎的结果如下:
    如果 x == y,那么两块石头都会被完全粉碎；
    如果 x != y,那么重量为 x 的石头将会完全粉碎,而重量为 y 的石头新重量为 y-x.
最后最多只会剩下一块石头.返回此石头的重量.如果没有石头剩下,就返回 0.

示例: 输入: [2,7,4,1,8,1]
     输出: 1
     解释: 先选出7和8,得到1,数组转换为 [2,4,1,1,1],
          再选出2和4,得到2,数组转换为 [2,1,1,1],
          接着是2和1,得到1,数组转换为 [1,1,1],
          最后选出1和1,得到0,最终数组转换为 [1],这就是最后剩下那块石头的重量.
"""


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        h = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            a, b = heapq.heappop(h), heapq.heappop(h)
            if a != b:
                heapq.heappush(h, a - b)
        return -h[0] if h else 0


s = Solution()
r = s.lastStoneWeight([2, 7, 4, 1, 8, 1])
print(r)
