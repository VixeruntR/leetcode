# coding=utf-8
"""
0-1背包问题: 给定n个重量为 w1,w2,w3,...,wn, 价值为 v1,v2,v3,...,vn​ 的物品和容量为C的背包,
            求这些物品中一个最有价值的子集,使得在满足背包的容量的前提下,包内物品的总价值最大.

递归: 用F(n,C)表示将前n个物品放进容量为C的背包里,得到的最大价值.
用自顶向下的角度来看,假如已经进行到了最后一步(即已经将n-1个物品放到背包里获得了最大价值),
此时便有两种选择:
 1.不放第n个物品, 此时总价值为F(n−1, C)
 2.放置第n个物品, 此时总价值为F(n−1, C−wn) + vn

两种选择中总价值最大的方案就是最终方案,递推式(也称状态转移方程)如下:
    F(i, C) = max(F(i−1, C), F(i−1, C−wi) + vi)
"""


# https://www.cnblogs.com/mfrank/p/10533701.html
def bag01(n, c, w, v):
    """
    :param n: 物品的数量(int type)
    :param c: 背包的容量(int type)
    :param w: 每个物品的重量(list type)
    :param v: 每个物品的价值(list type)
    """
    # value[i][j]的定义: 对于前i个物品,当前背包的容量为j,这种情况下可以装的最大价值是value[i][j]
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if j < w[i - 1]:  # 背包剩余容量小于第i件物品的重量, 则第i个物品不选
                value[i][j] = value[i - 1][j]
            if j >= w[i - 1]:  # 背包剩余容量大于等于第i件物品的重量
                # 剩余容量j-wt[i-1]能装的最大价值与第i个物品的价值v[i-1]之和
                value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])
    for v in value:
        print(v)
    return value


def bag01_show(n, c, w, value):
    flags = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            flags[i - 1] = True
            j -= w[i - 1]

    for i in range(len(flags)):
        if flags[i]:
            print('第', i + 1, '个  ', end='')


def bag01_plus(n, c, w, v):
    # bag01算法时间复杂度为O(cn), 已经无法再优化, 但空间复杂度O(cn)可以优化为O(c)
    value = [0] * (c + 1)
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            if j >= w[i - 1]:
                value[j] = max(value[j], value[j - w[i - 1]] + v[i - 1])
    print(value)
    return value


result = bag01(4, 10, [2, 3, 5, 5], [2, 4, 3, 7])
# bag01_show(4, 10, [2, 3, 5, 5], result)
bag01_plus(4, 10, [2, 3, 5, 5], [2, 4, 3, 7])


