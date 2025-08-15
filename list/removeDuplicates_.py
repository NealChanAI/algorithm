# -*- coding: utf-8 -*-
# ===============================================================



def removeDuplicates(nums):
    """
    双指针
    :param nums:
    :return:
    """
    if not nums:
        return

    l, r = 0, 1
    while r < len(nums):
        if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]
        r += 1

    return r + 1
