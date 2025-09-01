# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-28 17:07
#    @Description   : #283
#
# ===============================================================


class Solution:
    def move_zeros(self, nums):
        """
        1. 非空判断
        2. 快慢指针
        3. 补0
        """

        # 非空判断
        if not nums:
            return

        # 快慢指针
        s, f = 0, 0
        while f < len(nums):
            if nums[f] != 0:
                nums[s] = nums[f]  # 将指针f对应的值赋值给nums[s]
                s += 1  # 向右移动
            f += 1
        # 补0
        for i in range(s, len(nums)):
            nums[i] = 0

        return nums


if __name__ == '__main__':
    nums = [0, 1, 4, 0, 2]
    print(Solution().move_zeros(nums))
