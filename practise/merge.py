# -*- coding: utf-8 -*-
# ===============================================================
#

#
# ===============================================================


class Solution:
    def merge(self, nums1, m, nums2, n):
        # 非空判断
        if m <= 0 or n <= 0 or not nums1 or not nums2:
            return

        p1, p2 = 0, 0
        new_lst = []
        while p1 < m or p2 < n:
            if p1 == m:
                new_lst.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                new_lst.append(nums1[p1])
                p1 += 1
            elif nums1[p1] <= nums2[p2]:
                new_lst.append(nums1[p1])
                p1 += 1
            else:
                new_lst.append(nums2[p2])
                p2 += 1

        nums1[:] = [i for i in new_lst]

