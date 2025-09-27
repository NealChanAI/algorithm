# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/15 19:07
#    @Description   : 
#
# ===============================================================


"""
［3，2, 4,3, 5, 2,2,3, 4, 5, 3］
线段［3，2, 4,3, 5, 2,2,3, 4, 5, 3］中有多少个合法的连续子序列？合法连续子序列的定义是线段中的任何一个点，它相邻的点要么都比它大，要么都比它小，
如果一条线段只有两个点，比如［3，2］，也算一个合法的连续子序列。
"""


class Solution:
    def continues_sub_seq(self, nums):
        """
        1. 非空判断
        2.
        """
        n = len(nums)
        if n < 2:
            return 0

        res = 0

        for i in range(n):
            for j in range(i+1, n):
                sub_seq = nums[i: j+1]
                cur_len = len(sub_seq)

                if cur_len < 2:  # 长度小于2
                    continue

                if cur_len == 2:
                    res += 1
                    continue

                is_valid = True
                for k in range(1, cur_len-1):
                    cur_val = sub_seq[k]
                    left_val = sub_seq[k-1]
                    right_val = sub_seq[k+1]

                    if not ((left_val > cur_val and right_val > cur_val) or (left_val < cur_val or right_val < cur_val)):
                        is_valid = False
                        break

                if is_valid:
                    res += 1

        return res


if __name__ == '__main__':
    a = Solution()
    nums = [3, 2, 4, 3, 5, 2, 2, 3, 4, 5, 3]
    # nums = [3, 2]
    res = a.continues_sub_seq(nums)
    print(res)



