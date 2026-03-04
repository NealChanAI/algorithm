# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-02 11:04
#    @Description   : 
#
# ===============================================================


"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""


class Solution:
    def length_of_longest_substring(self, s):
        """
        滑动窗口
        """

        l, r = 0, 0
        window = {}
        max_len = 0

        while r < len(s):
            # 扩大窗口
            c = s[r]
            r += 1

            if c not in window:
                window[c] = 0
            window[c] += 1

            while l < r and window[c] > 1:
                # 缩小窗口
                d = s[l]
                l += 1

                window[d] -= 1

            # 更新结果
            max_len = max(max_len, r - l)

        return max_len


