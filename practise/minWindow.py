# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


class Solution:
    def min_window(self, s, t):
        """
        滑动窗口
        :param s:
        :param t:
        :return:
        """
        # 非空判断
        if not s or not t:
            return ''

        # 初始化相关变量
        left, right = 0, 0
        start, length = -1, float('inf')
        need, window = dict(), dict()
        valid = 0

        # 将t的字符存储到字典中
        for i in t:
            if i not in need:
                need[i] = 0
            need[i] += 1

        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1
            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while left < right and len(need) == valid:
                # 更新结果
                if right - left < length:
                    length = right - left
                    start = left

                # 收缩窗口
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return '' if length == float('inf') else s[start: start + length]


if __name__ == '__main__':
    s, t = 'ADOBECODEBANC', 'ABC'
    Solution().min_window(s, t)