# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/17 23:56
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def subsets(self, nums):
        """
        back_track
        :param nums:
        :return:
        """
        if not nums:
            return

        self.back_track(nums, 0)
        return self.res

    def back_track(self, nums, start):
        # 更新结果
        self.res.append(self.path.copy())

        # 遍历选择
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.back_track(nums, i+1)
            self.path.pop()


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))


