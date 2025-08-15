# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/13 23:24
#    @Description   : 
#
# ===============================================================
import random


def quick_sort(nums):
    """
    快速排序
    0. 合理性判断
    1. 以第一个元素为锚定点
    :param nums:
    :return:
    """

    if not nums:
        return

    # 对数组进行随机打乱
    rdm = random.Random()
    for i in range(len(nums)):
        j = rdm.randrange(0, len(nums))
        nums[i], nums[j] = nums[j], nums[i]

    def quick_sort_helper(nums, start, end):
        if start >= end:
            return
        low, high = start, end
        pivot = nums[low]
        while low < high:
            # 从左边开始找
            while high > low and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            # 从右边开始找
            while high > low and nums[low] < pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot

        quick_sort_helper(nums, start, low-1)
        quick_sort_helper(nums, low+1, end)

    return quick_sort_helper(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    a_lst = [1, 4, 2, 5, 7]
    a_lst = [5,2,3,1]
    quick_sort(a_lst)
    print(a_lst)