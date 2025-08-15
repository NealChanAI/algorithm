# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/16 17:41
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = float("-inf")

    def findKthLargest(self, nums, k):
        """
        :param nums:
        :return:
        """
        if not nums or k > len(nums):
            return

        def quick_sort_helper(nums, start, end):
            if start > end:
                return
            l, r = start, end
            pivot = nums[l]
            while l < r:
                while l < r and nums[r] >= pivot:
                    r -= 1
                nums[l] = nums[r]

                while l < r and nums[l] < pivot:
                    l += 1
                nums[r] = nums[l]

            nums[l] = pivot

            if len(nums) - k == l:
                self.res = pivot
                return
            elif len(nums) - k > l:
                quick_sort_helper(nums, l + 1, end)
            else:
                quick_sort_helper(nums, start, l - 1)

        quick_sort_helper(nums, 0, len(nums) - 1)
        print(nums)
        return self.res


if __name__ == "__main__":
    nums = [6, 3, 4, 2, 5, 1]
    print(Solution().findKthLargest(nums, 2))
