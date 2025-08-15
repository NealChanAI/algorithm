# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


def two_sum(nums, target):
    """
    0. 非空判断
    1. 左右双指针往移动
    :param nums:
    :param target:
    :return:
    """
    # 非空判断
    if len(nums) <= 1 or nums is None:
        return

    left, right = 0, len(nums) - 1
    while left < right:
        _sum = nums[left] + nums[right]
        if _sum == target:
            return [left+1, right+1]
        elif _sum > target:
            right -= 1
        else:
            left += 1
    return


