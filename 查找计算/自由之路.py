# coding=utf-8
"""
视频游戏“辐射4”中, 任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘, 并使用表盘拼写特定关键词才能开门.
给定一个字符串ring, 表示刻在外环上的编码; 给定另一个字符串 key, 表示需要拼写的关键词. 算出能够拼写关键词中所有字符的最少步数.
最初ring的第一个字符与12:00方向对齐, 需要顺时针或逆时针旋转ring以使key的一个字符在12:00方向对齐,然后按下中心按钮以逐个拼写完key中的所有字符.

旋转ring拼出key字符key[i]的阶段中:
    可以将ring顺时针或逆时针旋转一个位置, 计为1步.旋转的最终目的是将字符串ring的一个字符与12:00方向对齐, 并且这个字符等于字符key[i].
    如果字符key[i]已经对齐到12:00方向, 需要按下中心按钮进行拼写, 这也算作1步. 按完之后继续拼写key的下一个字符直至完成所有拼写。

示例: ./docs/自由之路.jpg
     输入: ring = "godding", key = "gd"
     输出: 4
     解释: 对于key的第一个字符'g', 已经在正确的位置, 只需要1步来拼写这个字符.
          对于key的第二个字符'd', 需要逆时针旋转ring "godding" 2步使它变成 "ddinggo".
          这里仍然需要1步进行拼写, 因此最终的输出是4.
"""


class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """

        # 求x位置到y位置的最小旋转步数, 就是正向和反向的最小值加上按中心的一步
        def dis(x, y):
            if x > y:
                x, y = y, x
            return min(y - x, x + n - y) + 1

        n = len(ring)
        now_set = [0]  # 记录当前所在的所有可能位,初始在0位
        res = [0]  # 记录对应位置的最优值
        for c in key:
            new_set = []  # 开始计算下一个位置所有可能的位置
            new_res = []  # 对应的最优值
            m = len(now_set)
            for i in range(n):
                if ring[i] == c:
                    new_set.append(i)
                    new_res.append(float('inf'))
                    for j in range(m):
                        new_res[-1] = min(new_res[-1], res[j] + dis(i, now_set[j]))

            now_set = new_set
            res = new_res
        return min(res)


s = Solution()
r = s.findRotateSteps(ring="godding", key="gd")
print(r)
