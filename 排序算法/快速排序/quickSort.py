# coding=utf-8
"""
快速排序(Quicksort)是对冒泡排序的一种改进, 它在排序效率在同为O(N*logN)的几种排序方法中效率较高.
它的基本思想(分治+递归): 通过一趟排序将要排序的数据分割成独立的两部分, 其中一部分的所有数据都比另外一部分的所有数据都要小,
然后再按此方法对这两部分数据分别进行快速排序, 整个排序过程可以递归进行, 以此达到整个数据变成有序序列.

快速排序算法通过多次比较和交换来实现排序, 其排序流程如下:
(1) 首先设定一个分界值, 通过该分界值将数组分成左右两部分.
(2) 将大于等于分界值的数据集中到数组右边, 小于分界值的数据集中到数组的左边.
    此时左边部分中各元素都小于分界值, 而右边部分中各元素都大于等于分界值.
(3) 对左边和右边的数据做独立排序. 对于左侧的数组又可以取一个分界值, 将该部分数据分成左右两部分,
    同样在左边放置较小值, 右边放置较大值. 右侧的数组数据做相同处理.
(4) 重复上述过程. 可以看出这是一个递归定义, 通过递归将左侧部分排好序后, 再递归排好右侧部分的顺序.
    当左右两个部分各数据排序完成后, 整个数组的排序也就完成了.
"""


def quick_sort1(data_list):
    if len(data_list) < 2:
        return data_list
    mid = data_list[len(data_list) // 2]  # 选取基准值(可任选)
    left, right = [], []  # 定义基准值左右两侧的列表
    data_list.remove(mid)  # 原始列表中删除基准值
    for data in data_list:
        if data >= mid:
            right.append(data)
        else:
            left.append(data)
    return quick_sort1(left) + [mid] + quick_sort1(right)


def quick_sort3(data_list):
    if len(data_list) < 2:
        return list
    tmp = data_list[0]
    left = [x for x in data_list[1:] if x <= tmp]
    right = [x for x in data_list[1:] if x > tmp]
    return quick_sort3(left) + [tmp] + quick_sort3(right)


def quick_sort2(data_list, start, end):
    if not start < end:
        return

    mid = data_list[start]  # 选定第一个数当作基准数
    lp = start  # lp来标记左侧从有向左找比mid大的数的位置
    rp = end  # rp来标记从右侧向左找比mid小的数的位置

    while lp < rp:
        while lp < rp and data_list[rp] > mid:
            rp -= 1
        # rp下标对应的数字就是从右向左找第一个比mid小的数
        data_list[lp] = data_list[rp]
        # 从lp向右找第一个比mid大的数
        while lp < rp and data_list[lp] <= mid:
            lp += 1
        # lp下标对应的数字就是从左向右找第一个比mid大的数
        data_list[rp] = data_list[lp]

    data_list[lp] = mid
    # 此时mid左侧的数都比mid小 mid右侧的数都比mid大
    # 再对mid两侧的数组分别进行迭代排序
    quick_sort2(data_list, start, lp - 1)
    quick_sort2(data_list, lp + 1, end)


if __name__ == '__main__':
    a = [19, 97, 9, 17, 1, 8, 27]
    quick_sort2(a, 0, len(a) - 1)
    print(a)
