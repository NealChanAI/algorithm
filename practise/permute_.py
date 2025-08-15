# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 15:23
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []

    def permute(self, nums):
        """
        回溯
        :param nums:
        :return:
        """
        if not nums:
            return

        self.used = [False] * len(nums)

        def _back_track(nums):
            # 更新结果
            if len(self.track) == len(nums):
                self.res.append(self.track.copy())

            for i in range(len(nums)):
                if self.used[i]:
                    continue
                self.track.append(nums[i])
                self.used[i] = True
                _back_track(nums)
                self.used[i] = False
                self.track.pop()

        _back_track(nums)
        return self.res

