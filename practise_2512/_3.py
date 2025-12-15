# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/12 20:29
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
        if not s:
            return 0

        res = 0
        window = {}
        l, r = 0, 0

        while r < len(s):
            # 扩大窗口
            c = s[r]
            r += 1

            if c not in window:
                window[c] = 0
            window[c] += 1

            while window[c] > 1 and l < r:
                # 缩小窗口
                d = s[l]
                l += 1
                window[d] -= 1

            # 更新结果
            res = max(res, r - l)

        return res
