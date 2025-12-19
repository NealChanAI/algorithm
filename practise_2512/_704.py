"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果 target 存在返回下标，否则返回 -1。
"""

class Solution:
    def search(self, nums, target):
        """
        1. 非空判断
        2. 二分查找
        """
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    # nums = [-1,0,3,5,9,12]
    # target = 2
    a = Solution()
    res = a.search(nums, target)
    print(res)
