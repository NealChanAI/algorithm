# -*- coding: utf-8 -*-
# ===============================================================
#
# ===============================================================


class Solution:
    def reverseWords(self, s):
        strs = []
        for _s in s.split(' '):
            if _s != '':
                strs.append(_s)
        i, j = 0, len(strs) - 1
        while i < j:
            if strs[i] == '':
                i += 1
                continue
            if strs[j] == '':
                j -= 1
                continue
            strs[i], strs[j] = strs[j], strs[i]
            i += 1
            j -= 1
        return ' '.join(strs)


if __name__ == '__main__':
    s = '  hello world  '
    s = "a good   example"
    # print(s.split(' '))
    print(Solution().reverseWords(s))
