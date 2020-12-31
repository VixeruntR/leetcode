# coding=utf-8
"""
给定一群人的一个队列, 要求重新排序.
排完后队列中每个人可以由一个整数对(h, k)表示,其中h是每个人的身高,
k表示在新队列中排在每个人前面且身高大于或等于h的人数.

示例1: 输入: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
      输出: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        考虑将这群人依次加入新队列中,加入时需符合k的要求.
        一个人的k值实际上与身高更矮的人的位置无关,所以如果身高比之更高的人已经排好队了,
        那么这个人加入这个新队列的位置就可以根据k值确定了,因此身高较高的人应该先加入,先对队列按身高降序排序.
        此外对于相同身高的人,k值较小的人位置在前,优先加入.
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) <= 1:
            return people
        # 对队列排序: 先按h降序,再按k升序
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        new_people = [people[0]]
        for i in people[1:]:
            new_people.insert(i[1], i)
        return new_people


s = Solution()
r = s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
print(r)
