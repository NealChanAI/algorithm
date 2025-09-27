# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/25 19:05
#    @Description   : 
#
# ===============================================================


class Solution:
    """
    给你一个字符串 s，找到 s 中最长的 回文 子串。

    示例 1：

    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。
    示例 2：

    输入：s = "cbbd"
    输出："bb"

    """
    def __init__(self):
        self.res = ''

    def longestPalindrome_helper(self, s, i, j):
        """
        辅助函数
        """
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1: j]

    def longestPalindrome(self, s):
        """
        1. 非空判断
        2. 辅助函数
        """
        if not s:
            return

        for i in range(len(s)-1):
            single_res = self.longestPalindrome_helper(s, i, i)  # 以i为中心向两边扩散
            double_res = self.longestPalindrome_helper(s, i, i+1)  # 以i, j为中心向两边扩散
            self.res = single_res if len(single_res) > len(self.res) else self.res
            self.res = double_res if len(double_res) > len(self.res) else self.res

        return self.res


if __name__ == '__main__':
    s = 'babad'
    s = "cbbd"
    a = Solution()
    res = a.longestPalindrome(s)
    print(res)


