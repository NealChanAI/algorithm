# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/14 21:56
#    @Description   : 77. 组合
#
# ===============================================================

class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def combine(self, n, k):
        self.back_track(n, 1, k)
        return self.res

    def back_track(self, n, start, k):
        """
        回溯算法
        :param n:
        :param k:
        :return:
        """
        if len(self.track) == k:
            self.res.append(list(self.track))
            return

        for i in range(start, n+1):
            self.track.append(i)
            self.back_track(n, i + 1, k)
            self.track.pop()


if __name__ == '__main__':
    a = Solution()
    print(a.combine(3, 2))

