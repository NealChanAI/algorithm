# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []

    def permuteUnique(self, nums):
        if not nums:
            return

        self.used = [False] * len(nums)

        def _back_track(nums):
            # 更新结果
            if len(self.track) == len(nums):
                self.res.append(self.track.copy())

            for i in range(len(nums)):
                # 如果重复，则跳过
                if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
                    continue
                # 如果之前使用过，则跳过
                if self.used[i]:
                    continue

                self.used[i] = True
                self.track.append(nums[i])
                _back_track(nums)
                self.used[i] = False
                self.track.pop()

        nums.sort()
        _back_track(nums)

        return self.res


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
