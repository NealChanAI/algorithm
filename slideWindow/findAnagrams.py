"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
"""


def find_anagrams(s, p):
    """
    滑动窗口，先扩大窗口，再缩小窗口
    :param s:
    :param p:
    :return:
    """
    # 非空判断

    # 初始化变量
    left, right = 0, 0
    need, window = dict(), dict()
    valid = 0
    res = []

    for i in p:
        if i not in need:
            need[i] = 0
            window[i] = 0
        need[i] += 1

    # 扩大窗口
    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        # 缩小窗口
        while valid == len(need):
            # 更新数据
            if right - left == len(p):
                res.append(left)
            d = s[left]
            left += 1
            if d in need:
                if need[d] == window[d]:
                    valid -= 1
                window[d] -= 1
    return res


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(find_anagrams(s, p))
