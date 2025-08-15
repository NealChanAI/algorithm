# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/14 23:02
#    @Description   : 47. 全排列2
#
# ===============================================================

class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []

    def permuteUnique(self, nums):
        nums.sort()
        self.used = [False] * len(nums)
        self.back_track(nums)
        return self.res

    def back_track(self, nums):
        # 更新结果
        if len(self.track) == len(nums):
            self.res.append(list(self.track).copy())

        for i in range(len(nums)):
            # 跳过重复值
            if nums[i] == nums[i-1] and i > 0 and self.used[i-1] is False:
                continue

            if self.used[i]:
                continue

            self.track.append(nums[i])
            self.used[i] = True
            self.back_track(nums)
            self.used[i] = False
            self.track.pop()
