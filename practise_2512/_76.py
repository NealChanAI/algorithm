# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-19 16:48
#    @Description   : 
#
# ===============================================================


"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""


class Solution:
    def minWindow(self, s, t):
        """
        滑动窗口
        """

        windows, need = {}, {}
        valid = 0
        l, r = 0, 0
        start = -1
        length = float('inf')

        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        while r < len(s):
            # 扩大窗口
            c = s[r]
            r += 1

            if c in need:
                if c not in windows:
                    windows[c] = 0
                windows[c] += 1

                if windows[c] == need[c]:
                    valid += 1

                while valid == len(need) and l <= r:
                    # 更新结果
                    if r - l < length:
                        start = l
                        length = r - l

                    # 缩小窗口
                    d = s[l]
                    l += 1

                    if d in need:
                        if windows[d] == need[d]:
                            valid -= 1
                        windows[d] -= 1

        return "" if length == float('inf') else s[start: start+length]
