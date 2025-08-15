# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 12:38
#    @Description   : 
#
# ===============================================================


class Solution:
    def longestPalindrome(self, s: str):
        """

        :param s:
        :return:
        """

        def is_palindrome(sub_s, l, r):
            while l >= 0 and r < len(sub_s) and sub_s[l] == sub_s[r]:
                l -= 1
                r += 1
            return sub_s[l + 1: r]

        res = ''
        for i in range(len(s)):
            res = res if len(is_palindrome(s, i, i)) < len(res) else is_palindrome(s, i, i)
            res = res if len(is_palindrome(s, i, i + 1)) < len(res) else is_palindrome(s, i, i + 1)

        return res


if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))
