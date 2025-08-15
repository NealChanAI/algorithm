"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""


def length_of_longest_substring(s):
    """
    滑动窗口技巧
    :param s:
    :return:
    """
    # 非空判断
    if not s:
        return 0

    left, right = 0, 0
    window = dict()
    res = 0  # 定义最长子串的长度

    while right < len(s):
        # 扩大窗口
        c = s[right]
        right += 1

        if c not in window:  # 将字符串计数到窗口中
            window[c] = 0
        window[c] += 1

        while window[c] > 1:
            # 缩小窗口
            d = s[left]
            left += 1
            if d in window:
                window[d] -= 1
        # 更新结果
        if right - left > res:
            res = right - left - 1
    return res


if __name__ == '__main__':
    s = " "
    print(length_of_longest_substring(s))

