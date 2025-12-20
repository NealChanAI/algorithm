# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-19 17:52
#    @Description   : 
#
# ===============================================================


"""
给定一个二叉树，判断它是否是 平衡二叉树
"""


class Solution:
    def __init__(self):
        self.res = True

    def isBalanced(self, root):
        """
        子函数计算子树的最大深度
        """
        self._max_depth(root)

        return self.res

    def _max_depth(self, root):
        # base case
        if not root:
            return 0

        left = self._max_depth(root.left)
        right = self._max_depth(root.right)

        left = left if left else 0
        right = right if right else 0

        if left - right > 1 or right - left > 1:
            self.res = False
            return

        return 1 + max(left, right)