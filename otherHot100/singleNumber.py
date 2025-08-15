# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


class Solution:
    def singleNumber(self, nums):
        """

        :param nums:
        :return:
        """
        if not nums:
            return

        res = 0
        for num in nums:
            # print("===" * 10)
            # print("befor:", res, "num:", num)
            res ^= num
            # print("after:", res)
        return res


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    Solution().singleNumber(nums)
