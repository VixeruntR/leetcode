# coding=utf-8
"""
堆的特点:
    1.内部数据是有序的
    2.可以弹出堆顶的元素,大顶堆就是弹出最大值,小顶堆就是弹出最小值
    3.每次加入新元素或者弹出堆顶元素后,调整堆使之重新有序仅需要O(logN)的时间
堆的本质:
    1.堆是一个完全二叉树
    2.可以用一个数组实现堆

./堆的实现.jpg
将二叉树和数组关联, 给树的结点编号, 结点的编号就是元素在数组中的下标.
已知一个结点的编号为 index, 可发现:
它的父节点编号为 father_index = (index − 1) // 2
左孩子节点编号为  left_index = index * 2 + 1​
右孩子节点编号为 right_index = index * 2 + 2

调整堆:
1. 添加元素
    - 把新数据添加到树的末端,也就是数组的末尾
    - 把末尾节点向上调整
2. 弹出堆顶
    - 交换根节点与最后一个节点
    - 删除最后一个节点(原先的根节点)
    - 把根节点向下调整
"""


class MyHeapq(object):
    # 小顶堆父节点元素更大,大顶堆父节点元素更小
    def __init__(self, desc=False):
        self.heap = []
        self.desc = desc  # 默认创建一个小顶堆

    @property
    def size(self):  # 返回堆的大小
        return len(self.heap)

    def top(self):  # 返回堆顶元素
        if self.size:
            return self.heap[0]
        return None

    def push(self, item):  # 添加一个元素
        self.heap.append(item)
        self._sift_up(self.size - 1)

    def pop(self):  # 弹出堆顶元素
        item = self.heap[0]  # 记录堆顶元素的值
        self._swap(0, self.size - 1)  # 交换堆顶元素与末尾元素
        self.heap.pop()  # 删除数组末尾元素
        self._sift_down(0)  # 新的堆顶元素向下调整
        return item

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _compare(self, lhs, rhs):
        return lhs > rhs if self.desc else lhs < rhs

    def _sift_up(self, index):
        while index:
            father_index = (index - 1) // 2
            if self._compare(self.heap[father_index], self.heap[index]):
                break
            self._swap(father_index, index)
            index = father_index

    def _sift_down(self, index):
        while index * 2 - 1 < self.size:
            min_index = index
            left_index = index * 2 + 1
            right_index = index * 2 + 2
            if self._compare(self.heap[left_index], self.heap[min_index]):
                min_index = left_index
            if right_index < self.size and self._compare(self.heap[right_index], self.heap[min_index]):
                min_index = right_index
            if min_index == index:
                break
            self._swap(index, min_index)
            index = min_index


if __name__ == '__main__':
    heap = MyHeapq()

    data = [12, 8, 10, 2, 4, 7, 9]
    for d in data:
        heap.push(d)
    print(heap.heap)
    heap.pop()
    print(heap.heap)
