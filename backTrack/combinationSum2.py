# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/14 22:47
#    @Description   : 40. 组合2
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.track_sum = 0

    def combinationSum2(self, candidates, target):
        if not candidates:
            return self.res

        candidates.sort()
        self.back_track(candidates, 0, target)
        return self.res

    def back_track(self, candidates, start, target):
        # base case
        if self.track_sum == target:
            self.res.append(list(self.track))
            return
        if self.track_sum > target:
            return

        for i in range(start, len(candidates)):
            if candidates[i] == candidates[i-1] and i > start:
                continue

            self.track.append(candidates[i])
            self.track_sum += candidates[i]
            self.back_track(candidates, i + 1, target)
            self.track_sum -= candidates[i]
            self.track.pop()



