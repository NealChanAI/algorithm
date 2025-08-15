"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


def remove_element(nums, val):
    """
    使用快慢指针对数组中的特定元素值进行删除
        1. 由fast指针在前面探路，若遇到val值，则fast往前走一步
    :param nums:
    :param val:
    :return: 移除数组后的元素长度 e.g. 5
    """
    # 合理性判断
    if not nums:
        return 0

    # 定义快慢指针
    slow, fast = 0, 0

    while fast < len(nums):
        # 若快指针指向的值不等于val
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


if __name__ == '__main__':
    nums = [1, 2, 4, 2, 3, 4, 3]
    val = 4
    print(remove_element(nums, val))
