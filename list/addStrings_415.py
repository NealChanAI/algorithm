# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/8 21:19
#    @Description   : #415
#
# ===============================================================


"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
"""


class Solution:
    def addStrings(self, nums1, nums2):
        if not nums1 or not nums2:
            return

        l1, l2 = len(nums1)-1, len(nums2)-1
        res = ''
        carry = 0
        while l1 >= 0 or l2 >= 0:
            n1 = int(nums1[l1]) if l1 >= 0 else 0
            n2 = int(nums2[l2]) if l2 >= 0 else 0
            _sum = n1 + n2
            # _sum = int(nums1[l1]) + int(nums2[l2])
            tmp = _sum + carry
            carry = tmp // 10
            digit = tmp % 10
            res = str(digit) + res

            l1 -= 1
            l2 -= 1

        if carry == 1:
            res = '1' + res

        return res


if __name__ == '__main__':
    nums1 = '456'
    nums2 = '77'
    res = Solution().addStrings(nums1, nums2)
    print(res)




