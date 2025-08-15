# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Description   : 
#
# ===============================================================

"""
给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。
"""


def two_sum(nums, target):
    """
    左右指针技巧
    :param nums:
    :param target:
    :return:
    """
    # 合理性判断
    if not nums:
        return

    # 若数组为非升序数组，将其做一下升序
    nums.sort()

    left, right = 0, len(nums)-1
    while left < right:
        _sum = nums[left] + nums[right]
        if _sum == target:
            return [left, right]
        elif _sum > target:
            right -= 1
        else:
            left += 1
    return


def _two_sum(nums, target):
    """
    使用字典的方式处理,key为具体值，value为索引号
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return

    _dic = dict()

    for i, num in enumerate(nums):
        if target - num in _dic:
            return [_dic[target - nums[i]], i]
        _dic[nums[i]] = i

    return


if __name__ == '__main__':
    nums = [3, 2, 4]
    print(_two_sum(nums, 6))