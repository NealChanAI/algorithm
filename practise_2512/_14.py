# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-25 10:56
#    @Description   : 
#
# ===============================================================


"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        双层for循环
        """
        if not strs:
            return ''

        std = strs[0]
        res = ''

        for i, c in enumerate(std):
            for j in range(1, len(strs)):
                if len(strs[j]) < i + 1:
                    return res
                if strs[j][i] != c:
                    return res
            res += c

        return res


if __name__ == '__main__':
    # 输入：strs = ["flower", "flow", "flight"]
    # 输出："fl"
    # 示例
    # 2：
    #
    # 输入：strs = ["dog", "racecar", "car"]
    # 输出：""
    # 解释：输入不存在公共前缀。
    strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    a = Solution()
    print(a.longestCommonPrefix(strs))
