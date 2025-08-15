# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 21:49
#    @Description   : 46. 全排列
#
# ===============================================================

class Solution:
    def __init__(self):
        self.used = []
        self.res = []
        self.path = []

    def permute(self, nums):
        """
        back track

        :param nums:
        :return:
        """
        if not nums:
            return

        self.used = [False] * len(nums)
        self.back_track(nums)
        return self.res

    def back_track(self, nums):
        # 更新结果
        if len(self.path) == len(nums):
            self.res.append(self.path.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            self.used[i] = True
            self.path.append(nums[i])
            self.back_track(nums)
            self.used[i] = False
            self.path.pop()



