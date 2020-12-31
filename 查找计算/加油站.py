# coding=utf-8
"""
在一条环路上有 N个加油站,其中第 i个加油站有汽油 gas[i]升.
有一辆油箱容量无限的的汽车,从第 i个加油站开往第 i+1个加油站需要消耗汽油 cost[i]升.
从其中的一个加油站出发,开始时油箱为空.
如果可以绕环路行驶一周,则返回出发时加油站的编号,否则返回 -1.

示例 1: 输入: gas  = [1,2,3,4,5]
            cost = [3,4,5,1,2]
       输出: 3
解释: 从 3号加油站(索引为 3处)出发,可获得 4升汽油,此时油箱有 0 + 4 = 4升汽油
     开往 4号加油站,此时油箱有 4 - 1 + 5 = 8升汽油
     开往 0号加油站,此时油箱有 8 - 2 + 1 = 7升汽油
     开往 1号加油站,此时油箱有 7 - 3 + 2 = 6升汽油
     开往 2号加油站,此时油箱有 6 - 4 + 3 = 5升汽油
     开往 3号加油站,需要消耗 5升汽油,足够返回到 3号加油站.
     因此 3可为起始索引.

示例 2: 输入: gas  = [2,3,4]
            cost = [3,4,3]
       输出: -1
解释: 不能从 0号或 1号加油站出发,因为没有足够的汽油可以行驶到下一个加油站.
     从 2号加油站出发,可以获得 4升汽油,此时油箱有 0 + 4 = 4升汽油
     开往 0号加油站,此时油箱有 4 - 3 + 2 = 3升汽油
     开往 1号加油站,此时油箱有 3 - 3 + 3 = 3升汽油
     无法返回 2号加油站,因为返程需要消耗 4升汽油,但是油箱只有 3升汽油.
     因此无论怎样,都不可能绕环路行驶一周.
"""
import pysnooper


class Solution(object):
    @pysnooper.snoop()
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        mod = len(gas)
        start, end = 0, 0
        oil = gas[0]

        while (end + 1) % mod != start:  # 当 cur + 1 == start 时说明到了终点
            if oil < cost[end]:  # 油不够开往下一节点
                start = (start - 1) % mod  # 将start前移一位作为新的起始节点
                oil += gas[start] - cost[start]  # 新的起始点到达旧的起始点时剩余的油量
            else:
                oil -= cost[end]  # 减去消耗的油
                end = (end + 1) % mod  # 去下一个节点
                oil += gas[end]  # 加上新节点的油

        # 返回时判断一下在终点时的油能否开到起点
        return start if oil - cost[end] >= 0 else -1


s = Solution()
r = s.canCompleteCircuit(gas=[1, 2, 3, 4, 5],
                         cost=[3, 4, 5, 1, 2])
print(r)
