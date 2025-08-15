# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 15:31
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def subsets(self, nums):
        """回溯"""

        def _back_track(nums, start):
            # 更新结果
            self.res.append(self.track.copy())

            for i in range(start, len(nums)):
                self.track.append(nums[i])
                _back_track(nums, i + 1)
                self.track.pop()

        _back_track(nums, 0)
        return self.res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
