"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""


def move_zeroes(nums):
    """
    使用双指针处理
    :param nums:
    :return:
    """
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            tmp = nums[right]
            nums[right] = nums[left]
            nums[left] = tmp
            left += 1
        right += 1
