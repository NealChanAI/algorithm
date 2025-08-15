"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""


def min_window(s, t):
    """
    使用滑动窗口处理
    1. 定义双指针、所需要的字符的字典、滑动窗口字典、用于判断窗口中的字符串数是否满足所需字符的变量、目标字符串索引起始位置、长度等

    :param s:
    :param t:
    :return:
    """
    left, right = 0, 0
    valid = 0
    window, need = dict(), dict()
    start, length = 0, float('inf')
    for i in t:  # 将子串T的字符存储到need字典中
        if i not in need:
            need[i] = 0
        need[i] += 1

    while right < len(s):
        # 扩大窗口
        c = s[right]
        right += 1
        # 若属于目标字符，则将其添加到window中
        if c in need:
            if c not in window:
                window[c] = 0
            window[c] += 1
            # 判断相关的字符是否已经满足要求了
            if need[c] == window[c]:
                valid += 1

        # 判断window中的字符是否已经满足need了
        while valid == len(need):
            # 更新最小覆盖子串
            if right - left < length:
                start = left
                length = right - left

            # 缩小窗口
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return '' if length == float('inf') else s[start: start+length]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "bbaa"
    # t = "aba"
    # s = "aa"
    # t = "aa"
    print(min_window(s, t))
