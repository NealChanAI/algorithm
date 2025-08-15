# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/16 22:16
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = float("-inf")

    def maxPathSum(self, root):
        if not root:
            return

        def max_gain(root):
            if not root:
                return 0

            left_max = max(max_gain(root.left), 0)
            right_max = max(max_gain(root.right), 0)

            tmp_res = root.val + left_max + right_max
            self.res = max(self.res, tmp_res)

            return root.val + max(left_max, right_max)