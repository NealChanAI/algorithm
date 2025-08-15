# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/17 12:11
#    @Description   : 
#
# ===============================================================

def longestPalindrome(s):
    """
    判断回文子串
    :param s:
    :return:
    """
    def is_palindrome(_s, l, r):
        while l >= 0 and r < len(_s) and _s[l] == _s[r]:
            l -= 1
            r += 1
        return _s[l+1: r]

    res = ""
    for i in range(len(s)-1):
        res = res if len(res) > is_palindrome(s, s[i], s[i]) else is_palindrome(s, s[i], s[i])
        res = res if len(res) > is_palindrome(s, s[i], s[i+1]) else is_palindrome(s, s[i], s[i+1])

    return res