# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/15 17:39
#    @Description   : 删除有序数组中的重复项
#
# ===============================================================


def remove_duplicates(nums):
    """
    数组为升序排序，需要原地删除数组中的重复元素
    方法：
        1. 使用快慢指针技巧，双指针起始位置均为0，快指针在前探路
        2. 若快指针所指的值和慢指针的不一样，则慢指针索引加一，将快指针的值给到慢指针
        3. 快指针遍历完即结束，可以返回慢指针的索引号+1
    :param nums:
    :return: 去重后的数据长度
    """
    if len(nums) == 0:
        return

    slow, fast = 0, 1

    # 遍历快指针
    while fast <= len(nums) - 1:

        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1

    return slow+1


if __name__ == '__main__':
    nums = [0, 0, 0, 1, 1, 3, 4]
    print(remove_duplicates(nums))

