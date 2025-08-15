# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/18 13:25
#    @Description   : 最长回文子串
#
# ===============================================================


def longest_palindrome(s):
    """
    最长回文子串
        中间指针技巧
    :param s:
    :return:
    """
    def _palindrome(s, l, r):
        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]

    res = ""
    for i in range(len(s)):
        s1 = _palindrome(s, i, i)
        s2 = _palindrome(s, i, i+1)
        res = res if res > len(s1) else s1
        res = res if res > len(s2) else s2

    return res


if __name__ == '__main__':
    s = "babad"
    print(longest_palindrome(s))