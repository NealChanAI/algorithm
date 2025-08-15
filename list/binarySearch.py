# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/18 11:49
#    @Description   :  简单版本二分搜索
#
# ===============================================================


def binary_search(nums, target):
    """
    简单版二分搜索，使用左右指针技巧
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return -1

    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + (left - right)) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            left += 1
        else:
            right -= 1

    return -1


if __name__ == '__main__':
    pass
