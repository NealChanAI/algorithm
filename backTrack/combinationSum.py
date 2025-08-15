# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 09:12
#    @Description   : 39. 组合总和
#
# ===============================================================

class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.track_sum = 0

    def combinationSum(self, candidates, target):
        if not candidates:
            return
        self.back_track(candidates, 0, target)
        return self.res

    def back_track(self, candidates, start, target):
        if self.track_sum > target:
            return
        if self.track_sum == target:
            self.res.append(self.track.copy())
            return

        for i in range(start, len(candidates)):
            self.track_sum += candidates[i]
            self.track.append(candidates[i])
            self.back_track(candidates, i, target)
            self.track_sum -= candidates[i]
            self.track.pop()
