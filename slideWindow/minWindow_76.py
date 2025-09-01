# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-28 18:06
#    @Description   : #76
#
# ===============================================================

"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""


class Solution:
    def min_window(self, s, t):
        """
        double pointers
        """
        # 非空判断
        if not s or not t:
            return

        start = 0
        length = float('inf')
        need, window = {}, {}
        valid = 0

        # 将t中的字符存储到need中
        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        l, r = 0, 0
        while r < len(s):
            # 扩大窗口
            c = s[r]
            r += 1

            if c not in window:
                window[c] = 0
            window[c] += 1

            if window[c] == need[c]:
                valid += 1

            # 满足条件
            while l < r and valid == len(need):
                # 更新结果
                if r - l > length:
                    length = r - l
                    start = l
                # 缩小窗口
                d = s[l]
                l += 1

                if d in need:
                    valid -= 1
                window[d] -= 1

        return s[start: start+length] if length != float('inf') else ''



