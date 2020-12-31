# coding=utf-8
"""
给定一个无重复元素的数组candidates和一个目标数target, 找出candidates中所有可以使数字和为target的组合
candidates中的数字可以无限制重复被选取. 所有数字(包括target)都是正整数且解集不能包含重复的组合.

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为:  [[7],
            [2,2,3]]
示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为:  [[2,2,2,2],
            [2,3,3],
            [3,5]]
"""


# TODO DFS + 递归 + 剪枝
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        变量意义：use表示已经使用过的数的列表, remain表示与target的差值.
        1. 对candidates升序排序, 以方便根据remain的大小使用return减小搜索空间.
        2. 递归寻找可能的组合.每次递归时对所有candidates做一次遍历,情况有3种:
            2.1 当前use的值和当前元素的和等于remain, 则加入结果列表
            2.2 当前use的值和当前元素的和小于remain, 则继续递归
            2.3 当前use的值和当前元素的和大于remain, 则退出本此循环
        3. 注意每层递归都对candidates整体做遍历, 则会产生如[2,2,3], [3,2,2]这样的重复结果.
           这是因为发生了“往前选择”的情况, 于是每次往更深层递归时candidates都往后递进一个起点,
           强制函数只能“往后选择”, 这样就不会出现重复结果.
        """

        def backtrack(index, used, remain):
            for i in range(index, len(candidates)):
                c = candidates[i]
                if c > remain:
                    return
                if c == remain:
                    res.append(used + [c])
                    return
                if c < remain:
                    backtrack(i, used + [c], remain - c)

        candidates = list(set(candidates))
        candidates.sort()
        res = []
        backtrack(0, [], target)
        return res

    def combinationSum_backtrack(self, candidates, target):
        def backtrack(candidates, tmp):
            if sum(tmp) > target:
                return
            if sum(tmp) == target:
                result.append(tmp)
                return
            for i in range(len(candidates)):
                print(i, candidates[i:], tmp + [candidates[i]])
                backtrack(candidates[i:], tmp + [candidates[i]])
            return result

        result = []
        return backtrack(candidates, [])

    def combinationSum_dp(self, candidates, target):
        # https://leetcode-cn.com/problems/combination-sum/solution/chao-qiang-gifzhu-ni-shi-yong-dong-tai-gui-hua-qiu/
        dp = {i: [] for i in range(target + 1)}
        for i in sorted(candidates, reverse=True):  # TODO 这里一定要将candidates降序排列
            print('----------------------- ', 'i=', i, ' ------------------------')
            for j in range(i, target + 1):
                print('---------- ', 'j=', j, ' -----------')
                if j == i:
                    dp[j] = [[i]]
                    print('==== ', dp)
                else:
                    dp[j].extend([x + [i] for x in dp[j - i]])
                    print('**** ', dp)
            print()
        return dp[target]


a = Solution()
r = a.combinationSum([1, 1, 2, 3], 4)
print(r)
