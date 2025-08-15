# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 10:34
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s):
        """
        滑动窗口
        :param s:
        :return:
        """
        # 非空判断
        if not s:
            return 0

        window = dict()
        left, right = 0, 0
        res = 0

        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1
            if c not in window:
                window[c] = 0
            window[c] += 1

            # 缩小窗口
            while left < right and window[c] > 1:
                d = s[left]
                if d in window:
                    window[d] -= 1
                left += 1

            # 更新结果
            res = max(res, right - left)

        return res


if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))

