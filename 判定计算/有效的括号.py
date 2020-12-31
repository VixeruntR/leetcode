# coding=utf-8
"""
给定一个只包括 '(', ')', '{', '}', '[', ']' 这6种括号的字符串, 判断字符串是否有效.

有效字符串需满足: 左括号必须用相同类型的右括号闭合.
               左括号必须以正确的顺序闭合.
            注意空字符串可被认为是有效字符串。

示例 1:  输入: "()"
        输出: true
示例 2:  输入: "()[]{}"
        输出: true
示例 3:  输入: "(]"
        输出: false
示例 4:  输入: "([)]"
        输出: false
示例 5:  输入: "{[]}"
        输出: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 满足全部成组, 则长度一定是偶数
        if len(s) % 2 == 1:
            return False
        pairs = {")": "(",
                 "]": "[",
                 "}": "{"}
        stack = list()
        for ch in s:
            if ch in pairs:
                # 如果栈非空, 且栈尾元素与当前字符(闭括号)对应的开括号, 则出栈
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # 如果为开括号, 则将其入栈
                stack.append(ch)
        # 遍历完后, 栈非空, 则表示开括号没有全部成组
        return not stack


a = Solution()
r = a.isValid("(([])){[]}")
print(r)
