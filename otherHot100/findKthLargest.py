# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


def find_kth_largest(nums, k):
    """
    快速排序
    :param nums:
    :return:
    """
    if not nums or len(nums) < k:
        return
    global res
    res = float("-inf")

    def quick_sort(_nums, start, end):
        global res
        if start > end:
            return

        low, high = start, end
        pivot = _nums[low]
        while low < high:
            while low < high and _nums[high] >= pivot:
                high -= 1
            _nums[low] = _nums[high]
            while low < high and _nums[low] < pivot:
                low += 1
            _nums[high] = _nums[low]
        _nums[low] = pivot
        if len(_nums) - low == k:
            # print(1111)
            res = pivot
            return
        quick_sort(_nums, start, low-1)
        quick_sort(_nums, low+1, end)

    quick_sort(nums, 0, len(nums) - 1)
    # print("res:", res)
    return res


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    # nums = [-1,2,0]
    k = 2
    print(find_kth_largest(nums, 2))
