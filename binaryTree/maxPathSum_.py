# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 22:30
#    @Description   : 
#
# ===============================================================


class Solution:
    def maxPathSum(self, root):
        """
        递归子函数：返回结点的最大贡献值
        :param root:
        :return:
        """

        res = float("-inf")

        def max_gain(self, root):
            # base case
            if not root:
                return 0

            left_gain = max(max_gain(root.left), 0)
            right_gain = max(max_gain(root.right), 0)

            global res
            res = max(res, root.val + left_gain + right_gain)

            return root.val + max(left_gain, right_gain)

        max_gain(root)
        return res
