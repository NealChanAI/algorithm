# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 15:25
#    @Description   : 
#
# ===============================================================


class Solution:
    def longestValidParentheses(self, s):
        """
        dp数组：dp[i]记录以s[i-1]为结尾的最长合法括号子串长度
        :param s:
        :return:
        """

        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        left = []  # 存储左括号的索引

        for i in range(len(s)):
            # 判断是否为左括号
            if s[i] == '(':
                left.append(i)
                dp[i + 1] = 0
            else:
                if left:
                    left_index = left.pop()
                    len_sub = 1 + i - left_index + dp[left_index]
                    dp[i + 1] = len_sub
                else:
                    dp[i + 1] = 0

        res = 0
        for i in dp:
            res = max(res, i)

        return res


