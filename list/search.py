# -*- coding: utf-8 -*-
# ===============================================================
#

#
# ===============================================================


def search(nums, target):
    """
    二分搜索法
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return

    left, right = 0, len(nums)-1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right -= 1
        elif nums[mid] < target:
            left += 1

    return -1


