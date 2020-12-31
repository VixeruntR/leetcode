# coding=utf-8

import heapq


def min_k(arr, k):
    heap = [-x for x in arr[:k]]
    heapq.heapify(heap)
    print(heap)
    for i in range(k, len(arr)):
        if -arr[i] > heap[0]:
            print(arr[i])
            heapq.heappop(heap)
            heapq.heappush(heap, -arr[i])
            print(heap)
    return [-x for x in heap]


def max_k(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
    return heap


data = [4, 5, 1, 16, 2, 7, 3, 6]
r = max_k(data, 4)
print(r)
