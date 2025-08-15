# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/8 01:23
#    @Description   : 
#
# ===============================================================


def is_palindrome(s):
    """
    回文串判断
    :param s:
    :return:
    """
    if len(s) <= 2 or s is None:
        return False

    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        return True


