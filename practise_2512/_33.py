# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/14 17:03
#    @Description   : 
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
        二分法
            1. 获取mid之后判断是在左半段还是右半段
            2. 再拿target, mid和端值进行比较，来判断左指针还是右指针应该进行收缩
        """
        if not nums:
            return
        l, r = 0, len(nums) - 1
        l_bound, r_bound = nums[0], nums[-1]

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= l_bound:  # 在左半段
                if target >= l_bound and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # 在右半段
                if target < l_bound and nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    a = Solution()
    res = a.serach(nums, target)
    print(res)
