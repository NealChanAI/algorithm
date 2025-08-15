# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/14 22:19
#    @Description   : 90. 子集
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def subsets_with_dup(self, nums):
        nums.sort()
        self.back_track(nums, 0)
        return self.res

    def back_track(self, nums, start):
        # 添加元素
        self.res.append(list(self.track).copy())

        # 遍历
        for i in range(start, len(nums)):
            if nums[i] == nums[i-1] and i > start:
                continue
            self.track.append(nums[i])
            self.back_track(nums, i + 1)
            self.track.pop()


if __name__ == '__main__':
    a = Solution()


