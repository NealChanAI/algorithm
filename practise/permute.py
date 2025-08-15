# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.used = []
        self.track = []

    def permute(self, nums):
        if not nums:
            return

        self.used = [False] * len(nums)

        def back_track(nums):
            if len(self.track) == len(nums):
                self.res.append(self.track.copy())
                return

            for i in range(len(nums)):
                if self.used[i]:
                    continue
                self.used[i] = True
                self.track.append(nums[i])
                back_track(nums)
                self.track.pop()
                self.used[i] = False

        back_track(nums)
        return self.res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))