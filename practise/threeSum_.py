# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 11:49
#    @Description   : 
#
# ===============================================================


class Solution:
    def threeSum(self, nums):
        """
        两数据之和，再使用遍历
        :param nums:
        :return:
        """
        if not nums:
            return

        res = []

        def two_sum(_nums, target):
            sub_res = []
            left, right = 0, len(_nums) - 1
            while left < right:
                _sum = _nums[left] + _nums[right]
                if _sum > target:
                    right -= 1
                elif _sum < target:
                    left += 1
                else:
                    sub_res.append([_nums[left], _nums[right]])
                    while left < right and _nums[left] == _nums[left+1]:
                        left += 1
                    left += 1
                    while left < right and _nums[right] == _nums[right-1]:
                        right -= 1
                    right -= 1
            return sub_res

        nums.sort()
        for i in range(len(nums)-2):
            # 跳过重复值
            if i > 0 and nums[i] == nums[i-1]:
                continue
            sub_res = two_sum(nums[i+1:], - nums[i])
            if sub_res:
                for c in sub_res:
                    tmp = [nums[i]].extend(c)
                    res.append(tmp)

        return res








