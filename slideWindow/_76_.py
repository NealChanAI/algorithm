# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-04 19:20
#    @Description   : 
#
# ===============================================================


"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""

class Solution:
    def minWindow(self, s, t):
        """
        1. 非空判断
        2. 左右双指针
        """
        if not s or not t:
            return ''

        window, need = {}, {}
        valid = 0
        res_len = float('inf')
        l, r = 0, 0
        start = 0

        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        idx = 0
        while r < len(s):
            if idx == 10:
                print(idx)
            idx += 1
            # 扩大窗口
            c = s[r]
            r += 1

            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

                while l < r and len(need) == valid:
                    # 更新结果
                    if r - l < res_len:
                        res_len = r - l
                        start = l

                    # minimize window
                    d = s[l]
                    l += 1
                    if d in need:
                        if window[d] == need[d]:
                            valid -= 1
                        window[d] -= 1

        return '' if res_len == float('inf') else s[start: start+res_len]


if __name__ == '__main__':
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "cabwefgewcwaefgcf"
    t = "cae"
    a = Solution()
    res = a.minWindow(s, t)
    print(res)