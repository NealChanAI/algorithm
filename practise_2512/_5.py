# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/13 09:46
#    @Description   : 
#
# ===============================================================


"""
给你一个字符串 s，找到 s 中最长的 回文 子串。
"""


class Solution:
    def longestPalindrome(self, s):
        """
        1. 非空判断
        2. 遍历s，以每个字符或每两个字符为中心向两边移动，查找最长的回传子串
        """
        if not s:
            return

        res = ''

        for i in range(len(s)):
            single_res = self.find_palindrome(s, i, i)
            res = res if len(res) > len(single_res) else single_res
            double_res = self.find_palindrome(s, i, i+1)
            res = res if len(res) > len(double_res) else double_res

        return res

    def find_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]
