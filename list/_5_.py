# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-05 18:13
#    @Description   : 
#
# ===============================================================


"""
给你一个字符串 s，找到 s 中最长的 回文 子串。
"""


class Solution:

    def is_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]

    def longestPalindrome(self, s):
        """
        回文子串, 可能是以某个字符为中间节点, 然后向两边扩散开, 也可以是两个相同的字符
        1. 非空判断
        2. 写一个子函数, 分别从i和(i, i+1)向两边扩散
        """
        if not s:
            return

        res = ''

        for i in range(len(s)):
            sin = self.is_palindrome(s, i, i)
            res = res if len(sin) < len(res) else sin
            dou = self.is_palindrome(s, i, i+1)
            res = res if len(dou) < len(res) else dou

        return res


