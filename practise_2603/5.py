# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 11:59
#    @Description   : 
#
# ===============================================================


"""
给你一个字符串 s，找到 s 中最长的 回文 子串。
"""


class Solution:
    def longestPalindrome(self, s):
        """
        写一个辅助函数, 双指针从中间往两边去查找最长回文子串
        """
        if not s:
            return

        res = ''

        for i in range(len(s)):
            sin = self._helper(s, i, i)
            dou = self._helper(s, i, i+1)
            tmp = sin if len(sin) > len(dou) else dou
            res = res if len(res) > len(tmp) else tmp

        return res

    def _helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1: j]