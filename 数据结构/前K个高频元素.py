# coding=utf-8
"""
给定一个非空的整数数组, 返回其中出现频率前k高的元素.

示例 1:  输入: nums = [1,1,1,2,2,3], k = 2
        输出: [1,2]

示例 2:  输入: nums = [1], k = 1
        输出: [1]

注意: 1 ≤ k ≤ 数组中不相同的元素的个数.
     算法的时间复杂度必须优于O(n log n), n是数组的大小.
"""


class SolutionOld(object):
    def topKFrequent_force(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = {}
        no_repeat_nums = list(set(nums))
        for num in no_repeat_nums:
            nums_dict[num] = nums.count(num)

        nums_dict = sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)  # 字典根据value排序
        res = [r[0] for r in nums_dict[:k]]
        return res

    def topKFrequent(self, nums, k):
        from collections import Counter
        nums_dict = Counter(nums)
        return [item[0] for item in nums_dict.most_common(k)]


class Solution(object):
    def topKFrequent_small_k(self, nums, k):
        """
        优先队列: 维护大小为k的堆(当k比较小时合适) 时间复杂度O(nlogk)
        从m个元素中通过堆选出最大的k个数: k大小的堆-小根堆
        堆满后若新加的数大于堆首数, 则弹出堆首元素(弹出了m-k个最小的)
        """
        from collections import Counter
        import heapq

        res = []
        heap = []
        lookup = Counter(nums)
        for num, freq in lookup.items():
            if len(heap) == k:  # 如果堆满了(k个元素)
                if heap[0][0] < freq:  # 弹出最小频率的元组
                    heapq.heapreplace(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res

    def topKFrequent_big_k(self, nums, k):
        """
        优先队列: 维护大小为k的堆(当k比较大时合适) 时间复杂度O(nlog(n-k))
        从m个元素中通过堆选出最大的k个数: m-k大小的堆-大根堆
        堆满后若新加的数小于堆首数, 堆首元素加入结果, 否则新加的数加入结果(选了k次最大的)
        """
        from collections import Counter
        import heapq

        res = []
        heap = []
        lookup = Counter(nums)
        n = len(lookup)
        for num, freq in lookup.items():
            if len(heap) == n - k:
                if heap and -heap[0][0] > freq:
                    res.append(heapq.heapreplace(heap, (-freq, num))[1])
                else:
                    res.append(num)
            else:
                heapq.heappush(heap, (-freq, num))
        return res

    def topKFrequent(self, nums, k):
        if k > len(nums) / 2:
            return self.topKFrequent_big_k(nums, k)
        else:
            return self.topKFrequent_small_k(nums, k)


a = Solution()
r = a.topKFrequent([8, 8, 2, 3, 3, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9], 3)
print(r)
