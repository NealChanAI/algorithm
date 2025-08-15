# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/6/7 15:53
#    @Description   : 
#
# ===============================================================


def min_window(s, t):
    """
    滑动窗口
    :param s:
    :param t:
    :return:
    """
    window, need = dict(), dict()
    valid = 0
    left, right = 0, 0
    start, length = -1, float('inf')

    for c in t:
        if c not in need:
            need[c] = 0
        need[c] += 1

    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            if c not in window:
                window[c] = 0
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(need) and left < right:
            # 更新最大长度

            if right - left < length:
                length = right - left
                start = left

            d = s[left]
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

            left += 1

    return "" if length == float('inf') else s[start: start+length]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"
    print(min_window(s, t))
