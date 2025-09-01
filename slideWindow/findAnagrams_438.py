# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : chenyongming
#    @Create Time   : 2025-09-01 15:47
#    @Description   : 
#
# ===============================================================


"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
"""

class Solution:
    def find_anagrams(self, s, t):
        """
        1. 非空判断
        2. slow/fast pointers, sliding windows
        """
        # 非空判断
        if not s or not t:
            return

        need, window = {}, {}
        valid = 0

        # 将所需的字符存储到need字典中
        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        left, right = 0, 0
        res = []

        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1

            # 更新数据
            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1

                if need[c] == window[c]:
                    valid += 1

            while right - left >= len(t):
                # 更新结果
                if len(need) == valid:
                    res.append(left)

                # 缩小窗口
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res

