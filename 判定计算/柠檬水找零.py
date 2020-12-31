# coding=utf-8
"""
在柠檬水摊上,每一杯柠檬水的售价为 5美元.顾客排队购买柠檬水,(按账单 bills支付的顺序)一次购买一杯.
每位顾客只买一杯柠檬水,然后向你付 5美元、10美元或 20美元.必须给每个顾客正确找零,也就是说净交易是每位顾客向你支付 5美元.
注意,一开始手头没有任何零钱.如果能给所有顾客正确找零,返回 true,否则返回 false.

示例 1: 输入: [5,5,5,10,20]
       输出: true
       解释: 前 3位顾客那里, 按顺序收取 3张 5美元的钞票.
            第 4位顾客那里, 收取一张 10美元的钞票,并返还 5美元.
            第 5位顾客那里, 找还一张 10美元的钞票和一张 5美元的钞票.
            由于所有客户都得到了正确的找零,所以输出true.
示例 2: 输入: [5,5,10]
       输出: true
示例 3: 输入: [10,10]
       输出: false
示例 4: 输入: [5,5,10,10,20]
       输出: false
       解释: 前 2位顾客那里, 按顺序收取 2张 5美元的钞票.
            对于接下来的 2位顾客, 收取一张 10美元的钞票,然后返还 5美元.
            对于最后一位顾客, 无法退回 15美元, 因为现在只有两张 10美元的钞票.
            由于不是每位顾客都得到了正确的找零, 所以答案是false.
"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] != 5:
            return False
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            if b == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            if b == 20:
                # 有10元的优先扣除10元的
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


s = Solution()
r = s.lemonadeChange([5, 5, 5, 10, 20])
print(r)
