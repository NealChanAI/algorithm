# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-01 15:30
#    @Description   : #567
#
# ===============================================================


class Solution:
    def check_inclusion(self, t, s):
        """
        1. 非空判断
        2. fast slow pointers/sliding windows
        """
        # 非空判断
        if not t or not s:
            return

        need, window = {}, {}
        valid = 0

        # 将t的字符保存到need字典中
        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        # define slow and fast pointers
        left, right = 0, 0
        while right < len(s):

            # 扩大窗口
            c = s[right]
            right += 1

            # 更新数据
            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            while right - left > len(t):
                # 更新结果
                if valid == len(need):
                    return True

                # 缩小窗口
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return False



