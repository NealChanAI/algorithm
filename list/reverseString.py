# -*- coding: utf-8 -*-
# ===============================================================

#    @Description   : 反转数组
#
# ===============================================================


def reverse_string(s):
    """
    双指针
    :param s:
    :return:
    """
    left, right = 0, len(s)-1
    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1




