# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 11:21
#    @Description   : 
#
# ===============================================================


class Solution:
    def checkInclusion(self, s1, s2):
        """
        判断s2的字符是否被包含在s1中
        滑动窗口
        :param s1:
        :param s2:
        :return:
        """
        # 非空判断
        if not s1 or not s2:
            return

        window, need = dict(), dict()
        left, right = 0, 0
        valid = 0

        # 将s1的字符存储到valid中
        for i in s1:
            if i not in need:
                need[i] = 0
            need[i] += 1

        while right < len(s2):
            # 扩大窗口
            c = s2[right]
            right += 1

            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            while left < right and valid == len(need):
                # 更新结果
                if right - left == len(s1):
                    return True

                # 收缩窗口
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return False
