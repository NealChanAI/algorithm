# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : chenyongming
#    @Create Time   : 2025-09-01 16:10
#    @Description   : #3
#
# ===============================================================


"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        1. 非空判断
        2. sliding windows
        """
        if not s:
            return 0

        window = {}
        res = 0

        left, right = 0, 0
        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1

            # 更新数据
            if c not in window:
                window[c] = 0
            window[c] += 1

            while window[c] > 1 and left < right:

                d = s[left]
                left += 1

                window[d] -= 1

            # 更新结果
            res = max(res, right-left)

        return res
