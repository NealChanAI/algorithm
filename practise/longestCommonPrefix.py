# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 20:53
#    @Description   : 
#
# ===============================================================


class Solution:
    def longestCommonPrefix(self, strs):
        """

        :param strs:
        :return:
        """
        if not strs or len(strs) == 0:
            return ''

        if len(strs) == 1 or strs[0] == '':
            return strs[0]

        res = ''

        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i:
                    return res
                if strs[j][i] != c:
                    return res if res else ''
            res += c

        return res


if __name__ == '__main__':
    strs = ["flower","flower","flower","flower"]
    print(Solution().longestCommonPrefix(strs))
