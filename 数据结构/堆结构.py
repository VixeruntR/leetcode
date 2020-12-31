# coding=utf-8
"""
堆是一种特殊的树形数据结构, 每个节点都有一个值, 通常所说的堆数据结构指的是二叉树.
堆的特点是根节点的值最大(或者最小), 而且根节点的两个孩子结点也能与其孩子节点组成子树.
堆分为两种, 大根堆(小根堆)是一棵每一个节点的键值都不小于(大于)其孩子节点的键值的树, 但不是严格排序.
无论是大根堆还是小根堆(前提是二叉堆)都可以看成是一颗完全二叉树. Python只有默认的小根堆.
注意, 堆结构虽然不是严格排序的, 但必须保证一点:
位置i处的元素总是大于位置i//2处的元素(反过来说就是小于位置 2*i和2*i+1 处的元素). 这是底层堆算法的基础,称为堆特征(heap property)
        ./docs/堆结构.png
"""
import heapq

t = [12, 8, 10, 4, 6, 7, 9]
# t.sort()  # 排序后生成的heap变了 堆结构不是严格排序
heap = []
for i in t:
    heapq.heappush(heap, i)
print(heap)  # 小根堆

max_num = heapq.nlargest(3, heap)  # 从堆中找出最大的N个数
min_num = heapq.nsmallest(3, heap)  # 从堆中找出最大的N个数
print(max_num, min_num)

data_dict = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
r = heapq.nlargest(1, data_dict, key=lambda x: x[1])
print(r)
