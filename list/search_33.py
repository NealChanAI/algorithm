# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-02 13:36
#    @Description   : #33
#
# ===============================================================


"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
"""


class Solution:
    def serach(self, nums, target):
        """
        1. 确定断崖在左半段还是右半段
        2. 确定后再调整做指针或右指针
        """
        if not nums:
            return

        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:  # 在左半段找
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 在右半段找
                if nums[mid] > target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


if __name__ == '__main__':
    """
    输入：nums = [4,5,6,7,0,1,2], target = 0
    输出：4
    示例 2：
    
    输入：nums = [4,5,6,7,0,1,2], target = 3
    输出：-1
    示例 3：
    
    输入：nums = [1], target = 0
    输出：-1
    """
    # nums = [4,5,6,7,0,1,2]
    # target = 0

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3

    nums = [1]
    target = 0


    res = Solution().serach(nums, target)
    print(res)
