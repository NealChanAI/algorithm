# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


def check_inclusion(s1, s2):
    """
    滑动窗口
    1. 非空判断
    2. 左右双指针，右指针先滑动
    :param s1:
    :param s2:
    :return:
    """
    # 非空判断
    if len(s1) == 0 or len(s2) == 0:
        return

    # 定义滑动窗口相关变量
    left, right = 0, 0
    need, window = dict(), dict()
    valid = 0

    for i in s1:
        if i not in need:
            need[i] = 0
        need[i] += 1

    while right < len(s2):
        c = s2[right]
        right += 1

        if c in need:
            if c not in window:
                window[c] = 0
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(set(s1)) and left < right:
            if right - left == len(s1):
                return True

            # 收缩窗口
            d = s2[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidboaoo"
    print(check_inclusion(s1, s2))

