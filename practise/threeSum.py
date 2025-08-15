# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/16 18:02
#    @Description   : 
#
# ===============================================================


class Solution:
    def threeSum(self, nums):
        """
        先实现two_sum，然后再遍历实现three_sum
        :param nums:
        :return:
        """
        if not nums:
            return

        res = []

        def two_sum(nums, target):
            two_res = []
            l, r = 0, len(nums) - 1
            _sum = nums[l] + nums[r]
            while l < r:
                if _sum > target:
                    r -= 1
                elif _sum < target:
                    l += 1
                else:
                    two_res.append([nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
            return two_res

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmp_res = two_sum(nums[i+1:], -nums[i])




