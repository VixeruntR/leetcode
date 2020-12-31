# coding=utf-8
"""
实现pow(x, n), 即计算x的n次幂函数.

示例 1:  输入: 2.00000, 10
        输出: 1024.00000
示例 2:  输入: 2.10000, 3
        输出: 9.26100
示例 3:  输入: 2.00000, -2
        输出: 0.25000
        解释: 2-2 = 1/22 = 1/4 = 0.25
"""


class Solution(object):
    def myPow1(self, x, n):
        """快速幂+递归
        如果计算x**16,可以按照x - x^2 - x^4 - x^8 - x^16的顺序,从x开始直接把上一次的结果平方
                    这样计算4次就可以得到最终结果, 而不需要对x进行15次连乘.
        如果计算x**39,可以按照x - x^2 - x^4 - x^9 - x^19 - x^39的顺序,
                    其中有几个步骤是直接对上一次的结果平方,其余几个步骤还要额外乘以一次x.
        此时从右往左(高位往地位)计算,利用分治算法:
        1.当计算x^n时,可以先递归地计算出 y=x^[n/2],其中[n/2]表示对a进行下取整.
        2.根据递归计算的结果,如果n为偶数,那么x^n = y^2; 如果n为奇数,那么x^n = y^2 * x.
        3.递归的边界为n=0,任意数的0次方均为1.
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0.0:
            return 0.0

        def son_pow(sn):
            if sn == 0:
                return 1.0
            y = son_pow(sn // 2)
            return y * y if sn % 2 == 0 else y * y * x

        return son_pow(n) if n >= 0 else 1.0 / son_pow(-n)

    def myPow(self, x, n):
        # 快速幂+循环
        if x == 0.0:
            return 0.0
        if n < 0:
            x, n = 1.0 / x, -n

        y = 1.0
        while n:
            if n % 2 == 1:
                y *= x
            x *= x
            n = n // 2
        return y


a = Solution()
r = a.myPow(2.0, 7)
print(r)
