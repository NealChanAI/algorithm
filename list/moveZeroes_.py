# -*- coding: utf-8 -*-



def move_zeroes(nums):
    """

    :param nums:
    :return:
    """

    if len(nums) == 0:
        return

    s, f = -1, 0
    while f < len(nums):
        if nums[f] != 0:
            s += 1
            nums[s] = nums[f]
        f += 1

    for i in range(s+1, len(nums)):
        nums[i] = 0


if __name__ == '__main__':
    nums = [0,1,0,3,12]
