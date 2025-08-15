# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/17 23:36
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.used = []

    def permuteUnique(self, nums):
        if not nums:
            return

        self.used = [False] * len(nums)
        nums.sort()
        self.back_track(nums)
        return self.res

    def back_track(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i-1]:
                continue

            self.used[i] = True
            self.path.append(nums[i])
            self.back_track(nums)
            self.used[i] = False
            self.path.pop()


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
