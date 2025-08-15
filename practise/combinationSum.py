# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 15:59
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.track_sum = 0

    def combinationSum(self, candidates, target):
        """
        回溯算法
        :param candidates:
        :param target:
        :return:
        """
        if not candidates:
            return

        def _back_track(candidates, target, start):
            # 更新结果
            if self.track_sum == target:
                self.res.append(self.track.copy())
                return

            if self.track_sum > target:
                return

            for i in range(start, len(candidates)):
                self.track.append(candidates[i])
                self.track_sum += candidates[i]
                _back_track(candidates, target, i)
                self.track_sum -= candidates[i]
                self.track.pop()

        _back_track(candidates, target, 0)
        return self.res


