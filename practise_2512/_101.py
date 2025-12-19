# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-19 17:43
#    @Description   : 
#
# ===============================================================


"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。
"""


class Solution:
    def isSummetric(self, root):
        if not root:
            return

        return self._is_symmetric(root.left, root.right)

    def _is_symmetric(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return self._is_symmetric(left.left, right.right) and self._is_symmetric(left.right, right.left)
