# coding=utf-8
"""
给定一个数组candidates和一个目标数target, 找出candidates中所有可以使数字和为target的组合.
candidates中的每个数字在每个组合中只能使用一次, 所有数字(包括目标数)都是正整数.


示例 1: 输入:candidates = [10,1,2,7,6,1,5], target = 8,
       所求解集为: [[1, 7],
                  [1, 2, 5],
                  [2, 6],
                  [1, 1, 6]]
示例 2: 输入: candidates = [2,5,2,1,2], target = 5,
       所求解集为: [[1, 2, 2],
                  [5]]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        ./docs/组合总和2.png
        去掉一个数组中重复的元素,很容易想到的方案是先对数组升序排序,重复的元素一定不是排好序以后相同的连续数组区域的第1个元素.
        即剪枝发生在: 同一层数值相同的结点第2、3 ... 个结点,因为数值相同的第1个结点已经搜索出了包含了这个数值的全部结果,
        同一层的其它结点, 候选数的个数更少, 搜索出的结果一定不会比第1个结点更多,并且是第1个结点的子集.

        这样做最重要的作用是, 可以让同一层级不出现相同的元素,即:(candidates=[2,5,2,1,2], target=5)
                          1
                         / \
                        2   2       情况1: 这种情况不会发生,但是却允许了不同层级之间的重复
                       /     \
                      5       5

                          1
                         /
                        2           情况2: 这种情况确是允许的
                       /
                      2

        首先 candidates[i] == candidates[i - 1]是用于判定当前元素是否和之前元素相同的语句.
        这个语句能过滤掉情况1,可是如果把所有当前与之前一个元素相同的都过滤掉, 那么情况2也会过滤掉.
        因为当第二个元素2出现的时候, 就和前一个2重复了.
        可以用 i > index 来避免这种情况,可以发现情况1中的两个元素2是处在同一个层级上的,情况2中的两个元素2是处在不同层级上的.
        在一个for循环中, 所有被遍历到的数都是属于一个层级的.
        要让一个层级中, 出现且只出现一个元素2, 那么就放过第一个出现重复的2, 但不放过后面出现的2.
        第一个出现的元素2的特点就是 i == index. 后面出现的元素2特点是 i > index.

        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(index, tmp, remain):
            for i in range(index, len(candidates)):
                c = candidates[i]
                if c == remain:
                    res.append(tmp + [c])
                    return
                if c > remain:
                    return
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, tmp + [c], remain - c)

        candidates.sort()
        res = []
        backtrack(0, [], target)
        # import collections
        # freq = sorted(collections.Counter(candidates).items())
        return res


s = Solution()
r = s.combinationSum2([4, 1, 2, 7, 6, 1, 5, 2, 2], 6)
print(r)
