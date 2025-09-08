# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-08 9:57
#    @Description   : 
#
# ===============================================================


"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""


class Solution:
    def length_of_longest_substring(self, s):
        """
        sliding window:
        """
        if not s:
            return

        l, r = 0, 0
        res = 0
        window = {}

        while r < len(s):
            # 扩大窗口
            c = s[r]
            r += 1

            if c not in window:
                window[c] = 0
            window[c] += 1

            while window[c] > 1 and l <= r:
                # 缩小窗口
                d = s[l]
                l += 1

                if d in window:
                    window[d] -= 1

            res = max(res, l-r)

        return res
