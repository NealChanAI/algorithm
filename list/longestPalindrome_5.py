# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-28 17:23
#    @Description   : #5
#
# ===============================================================


"""
给你一个字符串 s，找到 s 中最长的 回文 子串。
"""


class Solution:
    def is_palindrome(self, s, l, r):
        # 防止索引越界
        while l >= 0  and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]

    def longestPalindrome(self, s):
        """
        double pointers
        1. 遍历s, 以当前遍历的字符为中心(奇数), 向两边扩散
        2. 更新答案
        """
        res = ''

        for i in range(len(s)):
            s1 = self.is_palindrome(s, i, i)  # 奇数
            s2 = self.is_palindrome(s, i, i+1)  # 偶数

            res = res if len(s1) < len(res) else s1  # 奇数
            res = res if len(s2) < len(res) else s2  # 偶数

        return res
