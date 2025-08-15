# -*- coding: utf-8 -*-
# ===============================================================



def remove_element(nums, val):
    """
    快慢指针
    :param nums:
    :return:
    """

    if len(nums) == 0:
        return

    s, f = -1, 0
    while f < len(nums):
        if nums[f] != val:
            s += 1
            nums[s] = nums[f]
        f += 1

    return s + 1


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    print(remove_element(nums, val))
