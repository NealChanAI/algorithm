# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 10:24
#    @Description   : 
#
# ===============================================================


class Solution:
    def minWindow(self, s, t):
        """最小覆盖子串"""
        """
        1. need, window, valid
        2. 快慢指针
        3. start, length
        """
        if not s or not t:
            return ''

        need, window = dict(), dict()
        valid = 0
        start = -1
        length = float('inf')
        slow, fast = 0, 0

        # 将t字符串的数据存储到need中
        for i in t:
            if i not in need:
                need[i] = 0
            need[i] += 1

        while fast < len(s):
            # 扩大窗口
            c = s[fast]
            fast += 1
            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            while slow < fast and valid == len(need):
                # 更新结果
                if fast - slow < length:
                    start = slow
                    length = fast - slow

                # 缩小窗口
                d = s[slow]
                slow += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return '' if length == float('inf') else s[start: start + length]

