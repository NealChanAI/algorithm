# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:48
#    @Description   : 
#
# ===============================================================


"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        双指针, 从右往左
        第三个指针用于维护整体的
        """
        l1, l2 = m - 1, n - 1
        p = m + n - 1

        while l1 >= 0 and l2 >= 0:
            if nums1[l1] >= nums2[l2]:
                nums1[p] = nums1[l1]
                l1 -= 1
            else:
                nums1[p] = nums2[l2]
                l2 -= 1
            p -= 1

        while l2 >= 0:
            nums1[l2] = nums2[l2]
            l2 -= 1
