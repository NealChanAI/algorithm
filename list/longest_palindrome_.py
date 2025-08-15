# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/8 11:03
#    @Description   : 
#
# ===============================================================


def longest_palindrome_(s):
    """
    双指针
    :param s:
    :return:
    """
    if not s:
        return

    def _palindrome(sub_s, l, r):
        """
        判断是否为回文串，若是，返回最长的回文子串
        :param sub_s:
        :return:
        """
        while l >= 0 and r < len(sub_s) and sub_s[l] == sub_s[r]:
            l -= 1
            r += 1
        return sub_s[l+1: r]

    res = ""
    for i in range(len(s)):
        res = res if len(res) > len(_palindrome(s, i, i)) else _palindrome(s, i, i)
        res = res if len(res) > len(_palindrome(s, i, i+1)) else _palindrome(s, i, i+1)

    return res


if __name__ == '__main__':
    s = "babad"
    print(longest_palindrome_(s))
