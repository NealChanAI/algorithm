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

        res = 0
        windows = {}

        l, r = 0, 0
        while r < len(s):
            # 扩大窗口
            c = s[r]
            r += 1

            if c not in windows:
                windows[c] = 0
            windows[c] += 1

            while windows[c] > 1 and l < r:
                # 缩小窗口
                d = s[l]
                l += 1
                if d in windows:
                    windows[d] -= 1

            res = max(res, r - l)

        return res


if __name__ == '__main__':
    s = 'abc'
    s = 'abbc'
    a = Solution()
    print(a.length_of_longest_substring(s))



