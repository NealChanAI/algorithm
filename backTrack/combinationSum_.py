# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/17 22:46
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.sum = 0
        self.path = []

    def combinationSum(self, candidates, target):
        """
        back track algo.

        :param nums:
        :return:
        """
        # 非空判断
        if not candidates:
            return self.res

        def back_track(candidates, start, target):
            if self.sum > target:
                return

            if self.sum == target:
                self.res.append(self.path.copy())
                return

            for i in range(start, len(candidates)):
                self.path.append(candidates[i])
                self.sum += candidates[i]
                back_track(candidates, i, target)
                self.path.pop()
                self.sum -= candidates[i]

        back_track(candidates, 0, target)
        return self.res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    print(Solution().combinationSum(candidates, 7))
