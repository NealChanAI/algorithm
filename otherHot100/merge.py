# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


def merge(nums1, m, nums2, n):
    """

    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    if not nums1 or not nums2:
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

    nums1[:] = new_lst


if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)




