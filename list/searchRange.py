# -*- coding: utf-8 -*-

#
# ===============================================================


def search_range(nums, target):
    """
    双指针：
        基础版的二分搜索
    :param hums:
    :param target:
    :return:
    """
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1

