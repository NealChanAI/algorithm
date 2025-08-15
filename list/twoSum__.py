# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


def two_sum(nums, target):
    """

    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return

    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return l+1, r+1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1

    return

