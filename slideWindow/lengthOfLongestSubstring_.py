# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/7 23:53
#    @Description   : 
#
# ===============================================================


def length_of_longest_substring(s):
    """
    滑动窗口
    :param s:
    :return:
    """
    if not s:
        return 0

    l, r = 0, 0
    res = 0
    window = dict()
    while r < len(s):
        c = s[r]
        r += 1
        if c not in window:
            window[c] = 0
        window[c] += 1

        while window[c] > 1 and l < r:
            # 缩小窗口
            d = s[l]
            l += 1
            if d in window:
                window[d] -= 1
        res = max(res, r - l)
    return res


if __name__ == '__main__':
    s = "abcabcbb"
    s = " "
    print(length_of_longest_substring(s))



