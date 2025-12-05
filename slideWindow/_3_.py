# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-04 19:06
#    @Description   : 
#
# ===============================================================


"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""

class Solution:
    def length_of_non_duplicated_string(self, s):
        """
        1. 非空判断
        2. 左右双指针
        """
        if not s:
            return 0

        left, right = 0, 0
        window = {}
        res = 0

        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1
            if c not in window:
                window[c] = 0
            window[c] += 1

            while window[c] > 1 and left < right:
                # 缩小窗口
                d = s[left]
                left += 1

                window[d] -= 1

            res = max(res, right - left)

        return res


if __name__ == '__main__':
    s = 'abc'
    a = Solution()
    print(a.length_of_non_duplicated_string(s))
