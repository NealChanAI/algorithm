# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/16 17:31
#    @Description   : 
#
# ===============================================================


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        滑动窗口
        :param s:
        :return:
        """
        # 非空判断
        if not s:
            return ""

        l, r = 0, 0
        window = dict()
        res = 0

        while r < len(s):
            c = s[r]
            r += 1
            if c not in window:
                window[c] = 0
            window[c] += 1

            while window[c] > 1 and l < r:

                d = s[l]
                l += 1
                if d in window:
                    window[d] -= 1
            # 更新窗口
            res = max(res, r - l)

        return res


if __name__ == '__main__':
    s = "abcc"
    print(Solution().lengthOfLongestSubstring(s))





