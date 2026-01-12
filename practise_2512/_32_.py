"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。

左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。



示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
"""


from ast import main
from threading import main_thread
from turtle import mainloop


class Solution:
    def longestValidParentheses(self, s):
        """
        定义dp数组：
            dp[i-1]代表以i为索引的最长有效括号长度
        """

        res = 0 
        left = []
        dp = [0] * (len(s) + 1)
        
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
                dp[i+1] = 0 
            else:
                if not left:
                    dp[i+1] = 0
                else:
                    idx = left.pop()
                    dp[i+1] = i - idx + 1 + dp[idx]
                    res = max(res, dp[i+1])
        
        return res 


if __name__ == '__main__':
    s = "(()"
    # s = ")()())"

    a = Solution()
    print(a.longestValidParentheses(s))