# -*- coding: utf-8 -*-
# ===============================================================
#

#    @Description   : 
#
# ===============================================================


def removeElement(nums, val):
    if not nums:
        return

    l, r = -1, 0
    while r < len(nums):
        if nums[r] != val:
            l += 1
            nums[l] = nums[r]
        r += 1

    return l + 1
