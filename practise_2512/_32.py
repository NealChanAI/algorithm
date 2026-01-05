# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026/1/4 21:26
#    @Description   : 
#
# ===============================================================


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


class Solution:
    def longestValidParentheses(self, s):
        """
        非空判断
        dp数组定义：
            dp[i]代表以s[i-1]为结尾的最长有效括号子串的长度
        """
        if not s:
            return 0

        stk = []
        dp = [0] * (len(s) + 1)
        res = 0

        for i in range(len(s)):
            if s[i] == '(':
                dp[i+1] = 0  # 左括号不可能是合法括号的子串
                stk.append(i)  # 遇到左括号，记录索引
            else:
                if stk:
                    l_idx = stk.pop()
                    dp[i + 1] = i - l_idx + 1 + dp[l_idx]
                    res = max(res, dp[i+1])
                else:
                    dp[i+1] = 0

        return res
