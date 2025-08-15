# -*- coding: utf-8 -*-
# ===============================================================

#    @Description   : 151. 反转字符串中的单词
#
# ===============================================================


def reverseWords(s):
    """

    :param s:
    :return:
    """
    if not s:
        return s

    def reverse(_s):
        res = []
        for i in range(len(_s)):
            res.append(_s[(len(_s)-1 - i)])
        return "".join(res)



    res = []
    for i, item in enumerate(s.split(" ")):
        if i == " " or i == "":
            continue
        res.append(reverse(i.strip()))
    return " ".join(res)


if __name__ == '__main__':
    s = "abc"
    print(s[:,-1])
