# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/7 23:35
#    @Description   : 
#
# ===============================================================


def find_anagrams(s, p):
    """
    滑动窗口
    0. 非空判断
    :param s:
    :param p:
    :return:
    """

    # 非空判断
    if len(s) == 0 or len(p) == 0:
        return

    # 定义滑动窗口相关参数
    left, right = 0, 0
    valid = 0
    need, window = dict(), dict()
    res = []

    for i in p:
        if i not in need:
            need[i] = 0
        need[i] += 1

    while right < len(s):
        c = s[right]
        right += 1

        if c in need:
            if c not in window:
                window[c] = 0
            window[c] += 1

            if window[c] == need[c]:
                valid += 1

        while valid == len(set(p)) and right > left:
            if right - left == len(p):
                res.append(left)

            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return res







