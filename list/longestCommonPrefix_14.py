# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025/9/1 23:40
#    @Description   : #14
#
# ===============================================================


"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        多指针，以第一个字符为基准
        """
        if not strs:
            return

        res = ''
        for i, c in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if len(strs[j]) < i+1:
                    return res
                if strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

